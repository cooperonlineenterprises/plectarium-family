#!/usr/bin/env python3
"""Validate and finalize the Standalone Capability Family Packet v1."""
from __future__ import annotations
import argparse, hashlib, json, re, subprocess, sys, zipfile
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any

try:
    import yaml
except ImportError as exc:
    raise SystemExit("PyYAML is required") from exc
try:
    from jsonschema import Draft202012Validator
    from referencing import Registry, Resource
except ImportError as exc:
    raise SystemExit("jsonschema is required") from exc

PACKET_NAME = "standalone-capability-family-packet-v1"
PACKET_VERSION = "1.2.0"
FAMILY_ID = "standalone-capability-family"
MANIFEST = "PACKET-MANIFEST.json"
CHECKSUMS = "PACKET-CHECKSUMS.sha256"
CAPABILITY_IDS = [
    "universal-code-audit","verification-assurance","specification-conformance",
    "supply-chain-intelligence","runtime-investigation","api-contract-assurance",
    "ui-browser-assurance","database-migration-assurance","infrastructure-assurance",
    "release-assurance"
]
CANONICAL_CHARACTER_IDENTITIES = {
    "universal-code-audit": "Verity",
    "verification-assurance": "Titra",
    "specification-conformance": "Ortha",
    "supply-chain-intelligence": "Genea",
    "runtime-investigation": "Echo",
    "api-contract-assurance": "Harmia",
    "ui-browser-assurance": "Iris",
    "database-migration-assurance": "Janus",
    "infrastructure-assurance": "Atlas",
    "release-assurance": "Sibyl",
}
CAPABILITY_PRODUCT_NAMES = {
    "universal-code-audit": "Universal Code Audit",
    "verification-assurance": "Verification Assurance",
    "specification-conformance": "Specification Conformance",
    "supply-chain-intelligence": "Supply-Chain Intelligence",
    "runtime-investigation": "Runtime Investigation",
    "api-contract-assurance": "API / Contract Assurance",
    "ui-browser-assurance": "UI / Browser Assurance",
    "database-migration-assurance": "Database / Migration Assurance",
    "infrastructure-assurance": "Infrastructure Assurance",
    "release-assurance": "Release Assurance",
}
CAPABILITY_REPOSITORIES = {
    "universal-code-audit": "verity",
    "verification-assurance": "titra",
    "specification-conformance": "ortha",
    "supply-chain-intelligence": "genea",
    "runtime-investigation": "echo",
    "api-contract-assurance": "harmia",
    "ui-browser-assurance": "iris",
    "database-migration-assurance": "janus",
    "infrastructure-assurance": "atlas",
    "release-assurance": "sibyl",
}
DOWNSTREAM_PROVENANCE_FIELDS = [
    "family_git_commit", "packet_version", "packet_manifest_sha256", "seed_paths"
]
DISALLOWED_CHARACTER_ALIASES = {"Vera", "Tit", "Ort", "Gen", "Harmony"}
SEED_FILES = {
    "README.md","CHARTER-SEED.md","ARCHITECTURE-SEED.md","PRODUCT-BOUNDARY.md",
    "CAPABILITY-MODEL.md","EVIDENCE-MODEL-SEED.md","SECURITY-SEED.md",
    "INTERFACES-SEED.md","AGENT-SKILL-SEED.md","EVALUATION-SEED.md",
    "RELEASE-CRITERIA-SEED.md","ROADMAP-SEED.md","OPEN-QUESTIONS.md",
    "PROJECT-GENERATION-PROMPT.md","SOURCE-MAP.md","RESEARCH-AGENDA.md","capability.yaml"
}
REQUIRED = {
    "README.md","FAMILY-CHARTER.md","ARCHITECTURE.md","SECURITY.md","ROADMAP.md",
    "DECISIONS.md","OPEN-QUESTIONS.md","RELEASE-CRITERIA.md","INTEGRITY-REPORT.md","INTEGRITY-REPORT.md",
    "spec/family-invariants.md","spec/canonical-character-identities.md","spec/terminology.md","spec/authority-model.md",
    "spec/lifecycle.md","spec/evidence-conventions.md","spec/completion-conventions.md",
    "spec/result-envelope.md","spec/interface-conventions.md","spec/skill-conventions.md",
    "spec/capability-family-matrix.md","spec/capability-family-matrix.yaml",
    "spec/provisional-manifest.md","spec/imported-evidence.md","spec/planning-conventions.md",
    "spec/capability-classes.md","spec/project-seed-contract.md",
    "spec/family-identity-and-repository-map.md","spec/portfolio-source-ownership.md",
    "spec/migrations/provisional-family-namespace-1.2.0.md",
    "architecture/emerging-architecture.md","architecture/capability-relationship-graph.md",
    "architecture/capability-relationship-graph.yaml","architecture/project-seed-dependency-graph.md",
    "architecture/project-seed-dependency-graph.yaml","integrations/octon-mini.md",
    "integrations/generic-harness.md","agent/BUILD-DIRECTIVE.md","agent/authority.md",
    "agent/family-workstreams.md","agent/family-workstreams.yaml","agent/change-control.md",
    "agent/project-generation-guide.md","design/decision-ledger.md","design/decisions.yaml",
    "evals/FAMILY-EVALUATION-SPEC.md","evals/capability-seed-quality-gates.md",
    "evals/project-generation-validation.md","evals/claim-proof-matrix.md",
    "research/source-register.md","research/research-agenda.md","research/licensing.md",
    "reference/conversation-thread.md","reference/transcript-coverage.md",
    "reference/conversation-decision-map.md","reference/source-map.md",
    "reference/internal-consistency-review.md","docs/standalone-capability-pattern.md",
    "docs/new-capability-criteria.md","docs/future-shared-sdk-policy.md",
    "docs/family-creation-sequence.md","fixtures/README.md","scripts/validate-packet.py",
    "scripts/render-projections.py","design/adr/ADR-013.md",
    "fixtures/provisional-contracts/manifest.valid.json",
    "fixtures/provisional-contracts/result-envelope.valid.json",
    "fixtures/provisional-contracts/result-reference.valid.json",
    "fixtures/provisional-contracts/imported-result.valid.json",
    "fixtures/provisional-contracts/manifest.legacy.invalid.json",
    "fixtures/provisional-contracts/result-envelope.legacy.invalid.json",
    "fixtures/provisional-contracts/result-reference.legacy.invalid.json",
    "reference/related-packets/README.md",
    "reference/related-packets/uca-full-product-build-packet-v1.zip",
    "reference/related-packets/uca-full-product-build-packet-v1.manifest.json",
    "reference/related-packets/uca-full-product-build-packet-v1.zip.sha256",
    MANIFEST,CHECKSUMS
}
SCHEMAS = {
    "standalone-capability-manifest.v0.schema.json","result-envelope.v0.schema.json",
    "completion.v0.schema.json","permission-set.v0.schema.json",
    "result-reference.v0.schema.json","imported-result.v0.schema.json"
}

@dataclass
class Finding:
    level: str
    code: str
    message: str
    path: str|None=None
    def as_dict(self): return {"level":self.level,"code":self.code,"message":self.message,"path":self.path}

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()

def files(root: Path, include_integrity=True):
    out=[]
    for p in root.rglob("*"):
        rel=p.relative_to(root).as_posix()
        if p.is_symlink() or not p.is_file() or any(x in {".git","__pycache__"} for x in p.relative_to(root).parts) or p.suffix==".pyc": continue
        if not include_integrity and rel in {MANIFEST,CHECKSUMS}: continue
        out.append(p)
    return sorted(out,key=lambda p:p.relative_to(root).as_posix())

def safe_relative_path(value: Any) -> bool:
    if not isinstance(value,str) or not value: return False
    path=PurePosixPath(value)
    return not path.is_absolute() and "." not in path.parts and ".." not in path.parts

def strict_json(path: Path):
    def hook(pairs):
        d={}
        for k,v in pairs:
            if k in d: raise ValueError(f"duplicate key {k}")
            d[k]=v
        return d
    with path.open(encoding="utf-8") as f: return json.load(f,object_pairs_hook=hook)

def yload(path: Path):
    with path.open(encoding="utf-8") as f: return yaml.safe_load(f)

def classify(rel: str):
    if rel.startswith("spec/schemas/") or rel.endswith(".yaml"): return "machine-readable"
    if rel.startswith("capabilities/"): return "capability-project-seed"
    if rel.startswith("spec/") or rel in {"FAMILY-CHARTER.md","RELEASE-CRITERIA.md"}: return "normative-or-provisional-specification"
    if rel.startswith("design/") or rel.startswith("agent/") or rel in {"DECISIONS.md","OPEN-QUESTIONS.md","ROADMAP.md"}: return "governance"
    if rel.startswith("research/") or rel.startswith("reference/"): return "research-or-historical-reference"
    if rel.startswith("evals/") or rel.startswith("fixtures/"): return "verification"
    if rel.startswith("integrations/"): return "integration-boundary"
    if rel.startswith("architecture/") or rel.startswith("docs/") or rel=="ARCHITECTURE.md": return "reference-architecture"
    if rel=="SECURITY.md": return "security-governance"
    if rel.startswith("scripts/"): return "validation-tooling"
    if rel in {MANIFEST,CHECKSUMS}: return "packet-integrity"
    return "project-context"

def decision_counts(root: Path):
    data=yload(root/"design/decisions.yaml")
    items=data.get("decisions",[])
    return len(items),dict(Counter(x.get("status") for x in items))

def build_manifest(root: Path):
    inventory=[]
    for p in files(root,include_integrity=False):
        rel=p.relative_to(root).as_posix()
        inventory.append({"path":rel,"sha256":sha256(p),"bytes":p.stat().st_size,"classification":classify(rel)})
    matrix=yload(root/"spec/capability-family-matrix.yaml")
    graph=yload(root/"architecture/capability-relationship-graph.yaml")
    decisions,statuses=decision_counts(root)
    oq=(root/"OPEN-QUESTIONS.md").read_text(encoding="utf-8").count("## FQ-")
    turns=len(re.findall(r"^## Turn \d{3}\s*$",(root/"reference/conversation-thread.md").read_text(encoding="utf-8"),re.M))
    return {
        "schema_version":"standalone-capability-family-packet-manifest.v1",
        "packet":{"name":PACKET_NAME,"version":PACKET_VERSION,"generated_date":"2026-08-31",
                  "purpose":"Canonical family constitution, shared emerging architecture, and project-generation seeds for independent specialist capabilities."},
        "family_id":FAMILY_ID,
        "authority_hierarchy":["FAMILY-CHARTER.md","spec/family-invariants.md","spec/canonical-character-identities.md","shared provisional contracts","capability constitution","capability invariants/specifications","accepted ADRs","capability matrix/release criteria","workstreams/tasks","agent implementation choices"],
        "counts":{"content_files":len(inventory),"capabilities":len(matrix.get("capabilities",[])),"decisions":decisions,
                  "decision_statuses":statuses,"open_questions":oq,"adrs":len(list((root/"design/adr").glob("ADR-*.md"))),
                  "provisional_schemas":len(list((root/"spec/schemas").glob("*.schema.json"))),"conversation_turns":turns,
                  "relationship_edges":len(graph.get("edges",[]))},
        "capability_ids":[x["id"] for x in matrix.get("capabilities",[])],
        "capability_repositories":CAPABILITY_REPOSITORIES,
        "source_thread_coverage":{"transcript":"reference/conversation-thread.md","coverage_statement":"reference/transcript-coverage.md",
                                  "visible_turns_represented":turns,"excludes":["system messages","developer messages","hidden reasoning","raw tool calls"]},
        "key_relationships":[
            {"from":"FAMILY-CHARTER.md","to":"spec/family-invariants.md","meaning":"Family constitution governs binding invariants."},
            {"from":"spec/family-invariants.md","to":"capabilities/","meaning":"Seeds refine but cannot silently violate established family invariants."},
            {"from":"spec/result-envelope.md","to":"capabilities/*/EVIDENCE-MODEL-SEED.md","meaning":"Shared envelope is provisional; payload semantics remain capability-specific."},
            {"from":"architecture/capability-relationship-graph.yaml","to":"spec/imported-evidence.md","meaning":"Cross-capability evidence preserves provenance and completion."},
            {"from":"design/adr/ADR-013.md","to":"spec/portfolio-source-ownership.md","meaning":"Plectarium, family, capability, workspace, and harness source ownership remain separate."},
            {"from":"spec/family-identity-and-repository-map.md","to":"spec/schemas/","meaning":"Provisional discovery and result identities carry the canonical family namespace."},
            {"from":"capabilities/*/PROJECT-GENERATION-PROMPT.md","to":"future separate repositories","meaning":"Each seed generates an independent capability build packet."}
        ],
        "validation":{"script":"scripts/validate-packet.py","status":"pending until validator writes manifest"},
        "integrity":{"manifest_scope":"All files except manifest and checksum ledger.","checksums_scope":"All files except checksum ledger, including manifest.","algorithm":"SHA-256"},
        "files":inventory
    }

def write_checksums(root: Path):
    lines=[]
    for p in files(root,include_integrity=True):
        if p.relative_to(root).as_posix()==CHECKSUMS: continue
        lines.append(f"{sha256(p)}  {p.relative_to(root).as_posix()}")
    (root/CHECKSUMS).write_text("\n".join(lines)+"\n",encoding="utf-8")

def validate(root: Path, allow_pending_manifest=False):
    fs=[]
    for path in root.rglob("*"):
        if path.is_symlink():
            fs.append(Finding("error","symlink","Packet contents must not use symlinks",path.relative_to(root).as_posix()))
    if fs: return fs
    version_surfaces={"README.md":f"**Packet version:** {PACKET_VERSION}","INTEGRITY-REPORT.md":f"**Packet version:** `{PACKET_VERSION}`"}
    for rel,marker in version_surfaces.items():
        path=root/rel
        if path.is_file() and marker not in path.read_text(encoding="utf-8"):
            fs.append(Finding("error","packet-version",f"Expected packet version marker {marker!r}",rel))
    for rel in sorted(REQUIRED):
        if not (root/rel).is_file(): fs.append(Finding("error","required-file","Missing required file",rel))
    actual_capability_dirs=sorted(p.name for p in (root/"capabilities").iterdir() if p.is_dir()) if (root/"capabilities").is_dir() else []
    if actual_capability_dirs != sorted(CAPABILITY_IDS):
        fs.append(Finding("error","capability-dir-set",f"Expected exactly {sorted(CAPABILITY_IDS)}, got {actual_capability_dirs}","capabilities"))
    for cid in CAPABILITY_IDS:
        d=root/"capabilities"/cid
        if not d.is_dir():
            fs.append(Finding("error","capability-dir","Missing capability directory",str(d.relative_to(root))))
            continue
        for name in SEED_FILES:
            p=d/name
            if not p.is_file(): fs.append(Finding("error","seed-file","Missing seed file",p.relative_to(root).as_posix()))
            elif p.stat().st_size < (1800 if name=="PROJECT-GENERATION-PROMPT.md" else 450):
                fs.append(Finding("error","seed-substance",f"Seed file too small ({p.stat().st_size} bytes)",p.relative_to(root).as_posix()))
        try:
            cap=yload(d/"capability.yaml")
            if cap.get("id") != cid:
                fs.append(Finding("error","seed-id",f"capability.yaml id {cap.get('id')!r} does not match directory {cid!r}",(d/"capability.yaml").relative_to(root).as_posix()))
            if cap.get("family_id") != FAMILY_ID:
                fs.append(Finding("error","seed-family-id",f"Expected family_id {FAMILY_ID!r}, got {cap.get('family_id')!r}",(d/"capability.yaml").relative_to(root).as_posix()))
            family_packet=cap.get("family_packet",{})
            if family_packet.get("name") != PACKET_NAME or family_packet.get("version") != PACKET_VERSION:
                fs.append(Finding("error","seed-packet-identity",f"Expected {PACKET_NAME} version {PACKET_VERSION}",(d/"capability.yaml").relative_to(root).as_posix()))
            if family_packet.get("downstream_provenance_required") != DOWNSTREAM_PROVENANCE_FIELDS:
                fs.append(Finding("error","seed-provenance-contract",f"Expected downstream provenance fields {DOWNSTREAM_PROVENANCE_FIELDS}",(d/"capability.yaml").relative_to(root).as_posix()))
            expected_repository=CAPABILITY_REPOSITORIES[cid]
            expected_repository_metadata={
                "name":expected_repository,
                "owner":"cooperonlineenterprises",
                "url":f"https://github.com/cooperonlineenterprises/{expected_repository}.git",
                "default_branch":"main",
                "status":"ESTABLISHED",
            }
            if "working_repository" in cap:
                fs.append(Finding("error","stale-working-repository","capability.yaml retains obsolete working_repository after exact repository identity establishment",(d/"capability.yaml").relative_to(root).as_posix()))
            if cap.get("repository") != expected_repository_metadata:
                fs.append(Finding("error","seed-repository",f"Expected exact repository metadata {expected_repository_metadata}, got {cap.get('repository')!r}",(d/"capability.yaml").relative_to(root).as_posix()))
            expected_identity=CANONICAL_CHARACTER_IDENTITIES[cid]
            if "working_name" in cap:
                fs.append(Finding("error","stale-working-name","capability.yaml retains obsolete working_name after character identity establishment",(d/"capability.yaml").relative_to(root).as_posix()))
            if cap.get("canonical_character_identity") != expected_identity:
                fs.append(Finding("error","seed-character-identity",f"Expected canonical character identity {expected_identity!r}, got {cap.get('canonical_character_identity')!r}",(d/"capability.yaml").relative_to(root).as_posix()))
            product_name=str(cap.get("product_name", ""))
            if product_name != CAPABILITY_PRODUCT_NAMES[cid]:
                fs.append(Finding("error","seed-product-name",f"Expected descriptive product_name {CAPABILITY_PRODUCT_NAMES[cid]!r}, got {product_name!r}",(d/"capability.yaml").relative_to(root).as_posix()))
            prompt=(d/"PROJECT-GENERATION-PROMPT.md").read_text(encoding="utf-8")
            required_prompt_phrases=["Full Product Build Packet", "Product Constitution", "Executable Specification", "AI Build Packet", "Mature v1", "Family Constitution"]
            for phrase in required_prompt_phrases:
                if phrase.lower() not in prompt.lower():
                    fs.append(Finding("error","generation-prompt-contract",f"Missing required prompt concept: {phrase}",(d/"PROJECT-GENERATION-PROMPT.md").relative_to(root).as_posix()))
            if product_name.lower() not in prompt.lower():
                fs.append(Finding("error","generation-prompt-name","Project-generation prompt does not identify the descriptive product name",(d/"PROJECT-GENERATION-PROMPT.md").relative_to(root).as_posix()))
            prompt_provenance_markers=[
                "exact published family Git commit", "packet version `1.2.0`",
                "`PACKET-MANIFEST.json`", "every family and seed path actually used",
            ]
            for marker in prompt_provenance_markers:
                if marker not in prompt:
                    fs.append(Finding("error","generation-prompt-provenance",f"Missing downstream provenance requirement: {marker}",(d/"PROJECT-GENERATION-PROMPT.md").relative_to(root).as_posix()))
            required_prompt_headings=[
                "## Established character identity","## Authoritative inputs","## Product definition",
                "## Mandatory architecture","## Subject, evidence, and conclusion specifications",
                "## Durable result","## Permissions and security","## External tool and standards research",
                "## Interfaces","## Agent Skill","## Evaluation and release proof","## AI-team build packet",
                "## Open questions","## Critical boundary",
            ]
            for heading in required_prompt_headings:
                match=re.search(rf"^{re.escape(heading)}\s*$\n(.*?)(?=^## |\Z)",prompt,re.M|re.S)
                if not match or len(match.group(1).strip())<200:
                    fs.append(Finding("error","generation-prompt-section",f"Missing or insubstantial required prompt section: {heading}",(d/"PROJECT-GENERATION-PROMPT.md").relative_to(root).as_posix()))
            identity_surfaces={
                "seed README": (d/"README.md",f"**Canonical character identity:** **{expected_identity}**"),
                "charter seed": (d/"CHARTER-SEED.md",f"**{expected_identity}** is the established character identity."),
                "project-generation prompt": (d/"PROJECT-GENERATION-PROMPT.md",f"The canonical character identity is **{expected_identity}**."),
                "Agent Skill seed": (d/"AGENT-SKILL-SEED.md",f"**{expected_identity}** is the established character identity for this capability."),
                "evaluation seed": (d/"EVALUATION-SEED.md",f"Identity tests MUST verify exact use of {expected_identity},"),
                "release criteria seed": (d/"RELEASE-CRITERIA-SEED.md",f"canonical character identity **{expected_identity}** propagated without aliases or authority expansion"),
                "source map": (d/"SOURCE-MAP.md","`../../spec/canonical-character-identities.md`"),
                "seed family identity": (d/"README.md",f"**Family ID:** `{FAMILY_ID}`"),
                "seed repository identity": (d/"README.md",f"**Repository:** `{expected_repository}` — `https://github.com/cooperonlineenterprises/{expected_repository}.git` (`ESTABLISHED`)"),
            }
            for surface,(path,marker) in identity_surfaces.items():
                if marker not in path.read_text(encoding="utf-8"):
                    fs.append(Finding("error","identity-surface",f"{surface} does not declare the exact canonical character mapping for {expected_identity!r}",path.relative_to(root).as_posix()))
        except Exception as e:
            fs.append(Finding("error","seed-metadata",str(e),(d/"capability.yaml").relative_to(root).as_posix()))
    schema_names={p.name for p in (root/"spec/schemas").glob("*.schema.json")}
    for name in sorted(SCHEMAS-schema_names): fs.append(Finding("error","schema-missing","Missing provisional schema",f"spec/schemas/{name}"))
    # Parse JSON/YAML and schema structural checks.
    for p in files(root):
        rel=p.relative_to(root).as_posix()
        try:
            if p.suffix==".json": strict_json(p)
            elif p.suffix in {".yaml",".yml"}: yload(p)
        except Exception as e: fs.append(Finding("error","parse",str(e),rel))
    for p in (root/"spec/schemas").glob("*.schema.json"):
        try: Draft202012Validator.check_schema(strict_json(p))
        except Exception as e: fs.append(Finding("error","schema",str(e),p.relative_to(root).as_posix()))
    # Positive and negative namespace fixtures exercise the affected provisional contracts.
    try:
        schema_dir=root/"spec/schemas"
        schemas={p.name:strict_json(p) for p in schema_dir.glob("*.schema.json")}
        registry=Registry().with_resources(
            (schema["$id"],Resource.from_contents(schema))
            for schema in schemas.values() if schema.get("$id")
        )
        fixture_cases={
            "fixtures/provisional-contracts/manifest.valid.json":("standalone-capability-manifest.v0.schema.json",True),
            "fixtures/provisional-contracts/result-envelope.valid.json":("result-envelope.v0.schema.json",True),
            "fixtures/provisional-contracts/result-reference.valid.json":("result-reference.v0.schema.json",True),
            "fixtures/provisional-contracts/imported-result.valid.json":("imported-result.v0.schema.json",True),
            "fixtures/provisional-contracts/manifest.legacy.invalid.json":("standalone-capability-manifest.v0.schema.json",False),
            "fixtures/provisional-contracts/result-envelope.legacy.invalid.json":("result-envelope.v0.schema.json",False),
            "fixtures/provisional-contracts/result-reference.legacy.invalid.json":("result-reference.v0.schema.json",False),
        }
        for rel,(schema_name,should_pass) in fixture_cases.items():
            schema=schemas[schema_name]
            instance=strict_json(root/rel)
            errors=sorted(Draft202012Validator(schema,registry=registry).iter_errors(instance),key=lambda e:list(e.absolute_path))
            if should_pass and errors:
                fs.append(Finding("error","schema-fixture",f"Expected valid fixture; first error: {errors[0].message}",rel))
            elif not should_pass and not errors:
                fs.append(Finding("error","schema-negative-fixture","Legacy unnamespaced fixture unexpectedly validated",rel))
    except Exception as e:
        fs.append(Finding("error","schema-fixture-run",str(e),"fixtures/provisional-contracts"))
    # IDs and graph references.
    try:
        matrix=yload(root/"spec/capability-family-matrix.yaml")
        matrix_capabilities=matrix.get("capabilities",[])
        if matrix.get("family_id") != FAMILY_ID:
            fs.append(Finding("error","matrix-family-id",f"Expected family_id {FAMILY_ID!r}","spec/capability-family-matrix.yaml"))
        ids=[x["id"] for x in matrix_capabilities]
        if ids!=CAPABILITY_IDS: fs.append(Finding("error","capability-ids",f"Expected {CAPABILITY_IDS}, got {ids}","spec/capability-family-matrix.yaml"))
        if len(ids)!=len(set(ids)): fs.append(Finding("error","capability-duplicate","Duplicate capability IDs"))
        matrix_identities={x.get("id"):x.get("canonical_character_identity") for x in matrix_capabilities}
        if matrix_identities != CANONICAL_CHARACTER_IDENTITIES:
            fs.append(Finding("error","matrix-character-identities",f"Expected {CANONICAL_CHARACTER_IDENTITIES}, got {matrix_identities}","spec/capability-family-matrix.yaml"))
        if len(set(matrix_identities.values())) != len(CANONICAL_CHARACTER_IDENTITIES):
            fs.append(Finding("error","character-identity-duplicate","Canonical character identities must be one-to-one","spec/capability-family-matrix.yaml"))
        matrix_repositories={x.get("id"):x.get("repository",{}).get("name") for x in matrix_capabilities}
        if matrix_repositories != CAPABILITY_REPOSITORIES:
            fs.append(Finding("error","matrix-repositories",f"Expected {CAPABILITY_REPOSITORIES}, got {matrix_repositories}","spec/capability-family-matrix.yaml"))
        if any("working_repository" in x for x in matrix_capabilities):
            fs.append(Finding("error","matrix-stale-repository","Matrix retains obsolete working_repository metadata","spec/capability-family-matrix.yaml"))
        graph=yload(root/"architecture/capability-relationship-graph.yaml")
        if graph.get("family_id") != FAMILY_ID:
            fs.append(Finding("error","relationship-family-id",f"Expected family_id {FAMILY_ID!r}","architecture/capability-relationship-graph.yaml"))
        known=set(ids)
        node_ids=[n.get("id") for n in graph.get("nodes",[])]
        if set(node_ids) != known or len(node_ids) != len(set(node_ids)):
            fs.append(Finding("error","relationship-nodes",f"Graph nodes must uniquely equal capability matrix IDs; got {node_ids}","architecture/capability-relationship-graph.yaml"))
        graph_identities={n.get("id"):n.get("canonical_character_identity") for n in graph.get("nodes",[])}
        if graph_identities != CANONICAL_CHARACTER_IDENTITIES:
            fs.append(Finding("error","graph-character-identities",f"Expected {CANONICAL_CHARACTER_IDENTITIES}, got {graph_identities}","architecture/capability-relationship-graph.yaml"))
        dependency_graph=yload(root/"architecture/project-seed-dependency-graph.yaml")
        if dependency_graph.get("family_id") != FAMILY_ID:
            fs.append(Finding("error","dependency-family-id",f"Expected family_id {FAMILY_ID!r}","architecture/project-seed-dependency-graph.yaml"))
        dependency_nodes=dependency_graph.get("nodes",[])
        dependency_ids=[n.get("id") for n in dependency_nodes]
        if set(dependency_ids) != known or len(dependency_ids) != len(set(dependency_ids)):
            fs.append(Finding("error","dependency-nodes",f"Dependency graph nodes must uniquely equal capability matrix IDs; got {dependency_ids}","architecture/project-seed-dependency-graph.yaml"))
        dependency_identities={n.get("id"):n.get("canonical_character_identity") for n in dependency_nodes}
        if dependency_identities != CANONICAL_CHARACTER_IDENTITIES:
            fs.append(Finding("error","dependency-character-identities",f"Expected {CANONICAL_CHARACTER_IDENTITIES}, got {dependency_identities}","architecture/project-seed-dependency-graph.yaml"))
        dependency_repositories={n.get("id"):n.get("repository") for n in dependency_nodes}
        if dependency_repositories != CAPABILITY_REPOSITORIES:
            fs.append(Finding("error","dependency-repositories",f"Expected {CAPABILITY_REPOSITORIES}, got {dependency_repositories}","architecture/project-seed-dependency-graph.yaml"))
        readme_text=(root/"README.md").read_text(encoding="utf-8")
        matrix_markdown=(root/"spec/capability-family-matrix.md").read_text(encoding="utf-8")
        architecture_text=(root/"ARCHITECTURE.md").read_text(encoding="utf-8")
        relationship_markdown=(root/"architecture/capability-relationship-graph.md").read_text(encoding="utf-8")
        charter_text=(root/"FAMILY-CHARTER.md").read_text(encoding="utf-8")
        bold_identities=[f"**{CANONICAL_CHARACTER_IDENTITIES[cid]}**" for cid in [
            "universal-code-audit","verification-assurance","specification-conformance","supply-chain-intelligence",
            "runtime-investigation","api-contract-assurance","ui-browser-assurance","infrastructure-assurance",
            "database-migration-assurance","release-assurance",
        ]]
        charter_marker="The family uses the canonical character identities " + ", ".join(bold_identities[:-1]) + ", and " + bold_identities[-1]
        if charter_marker not in charter_text or "`spec/canonical-character-identities.md` governs the exact mapping" not in charter_text:
            fs.append(Finding("error","identity-charter","Family charter does not preserve the canonical identity set and exact mapping authority","FAMILY-CHARTER.md"))
        for order,cid in enumerate(CAPABILITY_IDS,1):
            product=CAPABILITY_PRODUCT_NAMES[cid]; identity=CANONICAL_CHARACTER_IDENTITIES[cid]
            projection_markers={
                "README.md":f"| {order} | {product} | **{identity}** | `{CAPABILITY_REPOSITORIES[cid]}` |",
                "spec/capability-family-matrix.md":f"| {cid} | {product} | **{identity}** |",
                "ARCHITECTURE.md":f"[{identity}<br/>{product}]",
                "architecture/capability-relationship-graph.md":f"[{identity}<br/>{product}]",
            }
            projection_texts={
                "README.md":readme_text,
                "spec/capability-family-matrix.md":matrix_markdown,
                "ARCHITECTURE.md":architecture_text,
                "architecture/capability-relationship-graph.md":relationship_markdown,
            }
            for rel,marker in projection_markers.items():
                if marker not in projection_texts[rel]:
                    fs.append(Finding("error","identity-projection",f"Missing exact {product!r} to {identity!r} projection",rel))
        for e in graph.get("edges",[]):
            if e.get("from") not in known or e.get("to") not in known:
                fs.append(Finding("error","relationship-ref",f"Unknown relationship endpoint: {e}","architecture/capability-relationship-graph.yaml"))
        hard=[e for e in graph.get("edges",[]) if e.get("type")=="hard_dependency"]
        # Simple DFS cycle check for hard edges.
        adj={x:[] for x in ids}
        for e in hard: adj[e["from"]].append(e["to"])
        visiting=set(); visited=set()
        def dfs(n):
            if n in visiting: return True
            if n in visited: return False
            visiting.add(n)
            if any(dfs(m) for m in adj[n]): return True
            visiting.remove(n); visited.add(n); return False
        if any(dfs(x) for x in ids): fs.append(Finding("error","hard-cycle","Circular hard dependency"))
    except Exception as e: fs.append(Finding("error","matrix-graph",str(e)))
    try:
        identity_spec=(root/"spec/canonical-character-identities.md").read_text(encoding="utf-8")
        rows=re.findall(r"^\| ([^|\n]+) \| \*\*([^*\n]+)\*\* \|$",identity_spec,re.M)
        observed={product.strip():identity.strip() for product,identity in rows}
        expected={CAPABILITY_PRODUCT_NAMES[cid]:CANONICAL_CHARACTER_IDENTITIES[cid] for cid in CAPABILITY_IDS}
        if len(rows)!=len(expected) or observed!=expected:
            fs.append(Finding("error","identity-spec",f"Expected exact canonical table {expected}, got {observed}","spec/canonical-character-identities.md"))
    except Exception as e:
        fs.append(Finding("error","identity-spec",str(e),"spec/canonical-character-identities.md"))
    # Decision and ADR IDs.
    try:
        dec=yload(root/"design/decisions.yaml").get("decisions",[])
        dids=[x.get("id") for x in dec]
        if len(dids)!=len(set(dids)): fs.append(Finding("error","decision-duplicate","Duplicate decision ID"))
        identity_decision=next((x for x in dec if x.get("id")=="FAM-034"),None)
        if not identity_decision or identity_decision.get("status")!="ESTABLISHED":
            fs.append(Finding("error","identity-decision","FAM-034 must establish the canonical character identities","design/decisions.yaml"))
        elif identity_decision.get("canonical_character_identities")!=CANONICAL_CHARACTER_IDENTITIES or "without aliases or authority expansion" not in identity_decision.get("decision",""):
            fs.append(Finding("error","identity-decision","FAM-034 must preserve the exact mapping, no-alias rule, and authority boundary","design/decisions.yaml"))
        ownership_decision=next((x for x in dec if x.get("id")=="FAM-035"),None)
        namespace_decision=next((x for x in dec if x.get("id")=="FAM-036"),None)
        if not ownership_decision or ownership_decision.get("status")!="ESTABLISHED":
            fs.append(Finding("error","ownership-decision","FAM-035 must establish Plectarium relationship and portfolio source ownership","design/decisions.yaml"))
        if not namespace_decision or namespace_decision.get("status")!="ESTABLISHED" or namespace_decision.get("family_id")!=FAMILY_ID or namespace_decision.get("repository_mappings")!=CAPABILITY_REPOSITORIES:
            fs.append(Finding("error","namespace-decision","FAM-036 must establish exact family_id and repository mappings","design/decisions.yaml"))
        adr13=root/"design/adr/ADR-013.md"
        adr13_text=adr13.read_text(encoding="utf-8") if adr13.is_file() else ""
        for marker in ["**Status:** Accepted",FAMILY_ID,"Plectarium","published family commit","packet-manifest digest"]:
            if marker not in adr13_text:
                fs.append(Finding("error","adr-013-contract",f"ADR-013 missing required marker {marker!r}","design/adr/ADR-013.md"))
        adrids=[p.stem for p in (root/"design/adr").glob("ADR-*.md")]
        if len(adrids)!=len(set(adrids)): fs.append(Finding("error","adr-duplicate","Duplicate ADR ID"))
    except Exception as e: fs.append(Finding("error","governance-parse",str(e)))
    alias_scan_exclusions={
        "spec/canonical-character-identities.md","scripts/validate-packet.py",
        "reference/conversation-thread.md",MANIFEST,CHECKSUMS,
    }
    for path in files(root):
        rel=path.relative_to(root).as_posix()
        if rel in alias_scan_exclusions or rel.startswith("reference/related-packets/") or path.suffix.lower() not in {".md",".yaml",".yml",".json",".py"}: continue
        content=path.read_text(encoding="utf-8")
        for alias in DISALLOWED_CHARACTER_ALIASES:
            if re.search(rf"\b{re.escape(alias)}\b",content):
                fs.append(Finding("error","character-alias",f"Disallowed character alias {alias!r}",rel))
    atlas_scan_exclusions={"scripts/validate-packet.py","reference/conversation-thread.md",MANIFEST,CHECKSUMS}
    atlas_tool_context=re.compile(r"\b(database|schema|migration|migrate|linting|ariga/atlas)\b",re.I)
    atlas_identity_context=re.compile(r"Infrastructure Assurance|canonical.character.identity.{0,24}Atlas|Atlas.{0,24}Infrastructure",re.I)
    for path in files(root):
        rel=path.relative_to(root).as_posix()
        if rel in atlas_scan_exclusions or rel.startswith("reference/related-packets/") or path.suffix.lower() not in {".md",".yaml",".yml",".json",".py"}: continue
        database_tool_scope=rel.startswith("capabilities/database-migration-assurance/") or rel in {"research/source-register.md","research/research-agenda.md"}
        for line_number,line in enumerate(path.read_text(encoding="utf-8").splitlines(),1):
            if not re.search(r"\batlas\b",line,re.I): continue
            if (database_tool_scope or atlas_tool_context.search(line)) and not re.search(r"\bAriga Atlas\b",line,re.I) and not atlas_identity_context.search(line):
                fs.append(Finding("error","atlas-tool-ambiguity","Database migration tool reference must be qualified as 'Ariga Atlas'",f"{rel}:{line_number}"))
    try:
        workstreams=yload(root/"agent/family-workstreams.yaml").get("workstreams",[])
        wids=[x.get("id") for x in workstreams]
        if len(wids)!=len(set(wids)) or any(not x for x in wids):
            fs.append(Finding("error","workstream-ids","Workstream IDs must be non-empty and unique","agent/family-workstreams.yaml"))
    except Exception as e:
        fs.append(Finding("error","workstream-parse",str(e),"agent/family-workstreams.yaml"))
    # Family namespace is an explicit contract, not merely an incidental fixture field.
    try:
        manifest_schema=strict_json(root/"spec/schemas/standalone-capability-manifest.v0.schema.json")
        envelope_schema=strict_json(root/"spec/schemas/result-envelope.v0.schema.json")
        reference_schema=strict_json(root/"spec/schemas/result-reference.v0.schema.json")
        if "family_id" not in manifest_schema.get("required",[]) or manifest_schema.get("properties",{}).get("family_id",{}).get("const") != FAMILY_ID:
            fs.append(Finding("error","manifest-family-contract","Manifest schema must require the canonical family_id literal","spec/schemas/standalone-capability-manifest.v0.schema.json"))
        capability_schema=envelope_schema.get("properties",{}).get("capability",{})
        expected_envelope_identity={"family_id","capability_id","version"}
        if not expected_envelope_identity.issubset(set(capability_schema.get("required",[]))) or capability_schema.get("properties",{}).get("family_id",{}).get("const") != FAMILY_ID or "id" in capability_schema.get("properties",{}):
            fs.append(Finding("error","envelope-family-contract","Result envelope capability identity must require family_id/capability_id/version and reject legacy id","spec/schemas/result-envelope.v0.schema.json"))
        if "family_id" not in reference_schema.get("required",[]) or reference_schema.get("properties",{}).get("family_id",{}).get("const") != FAMILY_ID:
            fs.append(Finding("error","reference-family-contract","Result-reference schema must require the canonical family_id literal","spec/schemas/result-reference.v0.schema.json"))
    except Exception as e:
        fs.append(Finding("error","family-contract-schema",str(e),"spec/schemas"))
    try:
        ownership=(root/"spec/portfolio-source-ownership.md").read_text(encoding="utf-8")
        identity_map=(root/"spec/family-identity-and-repository-map.md").read_text(encoding="utf-8")
        migration=(root/"spec/migrations/provisional-family-namespace-1.2.0.md").read_text(encoding="utf-8")
        for marker in ["Plectarium suite repository","Family repository","Each capability repository","Workspace repository","Octon or another harness"]:
            if marker not in ownership:
                fs.append(Finding("error","source-ownership",f"Missing source-owner marker {marker!r}","spec/portfolio-source-ownership.md"))
        for cid,repository in CAPABILITY_REPOSITORIES.items():
            expected=f"| `{cid}` | {CANONICAL_CHARACTER_IDENTITIES[cid]} | `{repository}` | `cooperonlineenterprises/{repository}` |"
            if expected not in identity_map:
                fs.append(Finding("error","repository-registry",f"Missing exact repository mapping for {cid}","spec/family-identity-and-repository-map.md"))
        for marker in ["Pre-1.2.0 shape","Packet 1.2.0 shape","Reject missing, unknown, or mismatched `family_id`","must not rewrite immutable historical results"]:
            if marker not in migration:
                fs.append(Finding("error","namespace-migration",f"Missing migration requirement {marker!r}","spec/migrations/provisional-family-namespace-1.2.0.md"))
    except Exception as e:
        fs.append(Finding("error","portfolio-contract",str(e)))
    # YAML is canonical for these deterministic Markdown projections.
    projection_script=root/"scripts/render-projections.py"
    if projection_script.is_file():
        try:
            projection_check=subprocess.run(
                [sys.executable,"-B",str(projection_script),"--check"],
                cwd=root,text=True,capture_output=True,check=False,
            )
            if projection_check.returncode != 0:
                details=(projection_check.stderr or projection_check.stdout).strip()
                fs.append(Finding("error","projection-drift",details or "Deterministic Markdown projections are stale","scripts/render-projections.py"))
        except Exception as e:
            fs.append(Finding("error","projection-check",str(e),"scripts/render-projections.py"))
    try:
        related=root/"reference/related-packets"
        uzip=related/"uca-full-product-build-packet-v1.zip"
        usha=related/"uca-full-product-build-packet-v1.zip.sha256"
        if not uzip.is_file() or not usha.is_file():
            fs.append(Finding("error","uca-reference","Embedded UCA reference ZIP or checksum is missing","reference/related-packets"))
        else:
            expected=usha.read_text(encoding="utf-8").strip().split()[0]
            if sha256(uzip)!=expected:
                fs.append(Finding("error","uca-reference-hash","Embedded UCA reference ZIP hash mismatch",uzip.relative_to(root).as_posix()))
            with zipfile.ZipFile(uzip) as zf:
                bad_member=zf.testzip()
                if bad_member:
                    fs.append(Finding("error","uca-reference-zip",f"Embedded UCA ZIP corrupt member: {bad_member}",uzip.relative_to(root).as_posix()))
    except Exception as e:
        fs.append(Finding("error","uca-reference-verify",str(e),"reference/related-packets"))
    # Placeholder and emptiness checks.
    bad=re.compile(r"\bTODO\s*:|\bTBD\b|lorem ipsum",re.I)
    for p in files(root):
        if p.suffix.lower() not in {".md",".yaml",".yml",".json",".py"}: continue
        rel=p.relative_to(root).as_posix()
        text=p.read_text(encoding="utf-8")
        if not text.strip(): fs.append(Finding("error","empty","Empty file",rel))
        for m in bad.finditer(text):
            # Permit explicit governance discussion of unresolved-marker rules.
            if rel=="scripts/validate-packet.py" or "unclassified `todo`" in text.lower(): continue
            fs.append(Finding("warning","placeholder",f"Potential unresolved marker: {m.group(0)}",rel)); break
    # Embedded UCA reference packet integrity.
    embedded=root/"reference/related-packets/uca-full-product-build-packet-v1.zip"
    embedded_digest=root/"reference/related-packets/uca-full-product-build-packet-v1.zip.sha256"
    if embedded.exists() and embedded_digest.exists():
        try:
            expected=embedded_digest.read_text(encoding="utf-8").split()[0]
            if sha256(embedded)!=expected:
                fs.append(Finding("error","embedded-uca-hash","Embedded UCA ZIP digest mismatch",embedded.relative_to(root).as_posix()))
            with zipfile.ZipFile(embedded) as zf:
                bad_member=zf.testzip()
                if bad_member:
                    fs.append(Finding("error","embedded-uca-zip",f"Corrupt member: {bad_member}",embedded.relative_to(root).as_posix()))
        except Exception as e:
            fs.append(Finding("error","embedded-uca-zip",str(e),embedded.relative_to(root).as_posix()))
    # Manifest metadata, inventory closure, paths, sizes, classifications, and hashes.
    mp=root/MANIFEST
    if mp.exists():
        try:
            man=strict_json(mp)
            expected_manifest=build_manifest(root)
            metadata_keys=["schema_version","packet","family_id","authority_hierarchy","counts","capability_ids","capability_repositories","source_thread_coverage","key_relationships","integrity"]
            for key in metadata_keys:
                if man.get(key)!=expected_manifest.get(key):
                    fs.append(Finding("error","manifest-metadata",f"Manifest {key!r} does not match recomputed packet state",MANIFEST))
            items=man.get("files",[])
            if not isinstance(items,list):
                fs.append(Finding("error","manifest-inventory","Manifest files must be an array",MANIFEST)); items=[]
            paths=[item.get("path") for item in items if isinstance(item,dict)]
            string_paths=[path for path in paths if isinstance(path,str)]
            expected_items=expected_manifest["files"]
            expected_paths=[item["path"] for item in expected_items]
            if len(paths)!=len(items) or len(string_paths)!=len(paths) or len(string_paths)!=len(set(string_paths)):
                fs.append(Finding("error","manifest-inventory","Manifest file paths must be present and unique",MANIFEST))
            if paths!=expected_paths:
                missing=[path for path in expected_paths if path not in paths]
                extra=[repr(path) for path in paths if not isinstance(path,str) or path not in expected_paths]
                fs.append(Finding("error","manifest-inventory",f"Manifest inventory is not exact; missing={missing}, extra={extra}",MANIFEST))
            expected_by_path={item["path"]:item for item in expected_items}
            for item in items:
                if not isinstance(item,dict): continue
                rel=item.get("path")
                if not safe_relative_path(rel):
                    fs.append(Finding("error","manifest-path",f"Unsafe manifest path {rel!r}",MANIFEST)); continue
                expected_item=expected_by_path.get(rel)
                if expected_item is not None and item!=expected_item:
                    fs.append(Finding("error","manifest-entry",f"Manifest entry does not match recomputed path/hash/bytes/classification",rel))
            validation=man.get("validation",{})
            if allow_pending_manifest:
                valid_status=validation.get("status") in {"generated; final pass required","passed"}
            else:
                valid_status=validation.get("status")=="passed" and bool(validation.get("validated_at")) and validation.get("errors")==0 and validation.get("warnings")==0
            if validation.get("script")!="scripts/validate-packet.py" or not valid_status:
                fs.append(Finding("error","manifest-validation","Manifest validation receipt is not current and complete",MANIFEST))
        except Exception as e: fs.append(Finding("error","manifest",str(e),MANIFEST))
    # Checksum ledger inventory closure, path safety, uniqueness, syntax, and hashes.
    cp=root/CHECKSUMS
    if cp.exists():
        records=[]
        for line in cp.read_text(encoding="utf-8").splitlines():
            if not line.strip(): continue
            try: digest,rel=line.split("  ",1)
            except ValueError: fs.append(Finding("error","checksum-format","Invalid checksum line",CHECKSUMS)); continue
            records.append((digest,rel))
        checksum_paths=[rel for _,rel in records]
        expected_checksum_paths=[p.relative_to(root).as_posix() for p in files(root,include_integrity=True) if p.relative_to(root).as_posix()!=CHECKSUMS]
        if len(checksum_paths)!=len(set(checksum_paths)):
            fs.append(Finding("error","checksum-inventory","Checksum paths must be unique",CHECKSUMS))
        if checksum_paths!=expected_checksum_paths:
            missing=sorted(set(expected_checksum_paths)-set(checksum_paths)); extra=sorted(set(checksum_paths)-set(expected_checksum_paths))
            fs.append(Finding("error","checksum-inventory",f"Checksum inventory is not exact; missing={missing}, extra={extra}",CHECKSUMS))
        for digest,rel in records:
            if not re.fullmatch(r"[0-9a-f]{64}",digest):
                fs.append(Finding("error","checksum-format",f"Invalid SHA-256 digest {digest!r}",CHECKSUMS)); continue
            if not safe_relative_path(rel):
                fs.append(Finding("error","checksum-path",f"Unsafe checksum path {rel!r}",CHECKSUMS)); continue
            p=root/rel
            if not p.is_file(): fs.append(Finding("error","checksum-path","Checksum path missing",rel))
            elif sha256(p)!=digest: fs.append(Finding("error","checksum-hash","Checksum mismatch",rel))
    return fs

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--root",type=Path,default=Path(__file__).resolve().parents[1])
    ap.add_argument("--json",action="store_true")
    ap.add_argument("--refresh-projections",action="store_true")
    ap.add_argument("--write-manifest",action="store_true")
    ap.add_argument("--refresh-checksums",action="store_true")
    args=ap.parse_args(); root=args.root.resolve()
    if args.refresh_projections:
        projection_write=subprocess.run(
            [sys.executable,"-B",str(root/"scripts/render-projections.py"),"--write"],
            cwd=root,text=True,capture_output=True,check=False,
        )
        if projection_write.returncode != 0:
            message=(projection_write.stderr or projection_write.stdout).strip()
            raise SystemExit(f"Projection refresh failed: {message}")
    if args.write_manifest:
        manifest=build_manifest(root)
        manifest["validation"]={"script":"scripts/validate-packet.py","status":"generated; final pass required"}
        (root/MANIFEST).write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
    if args.refresh_checksums: write_checksums(root)
    findings=validate(root,allow_pending_manifest=args.write_manifest)
    errors=[x for x in findings if x.level=="error"]
    warnings=[x for x in findings if x.level=="warning"]
    if args.write_manifest and not errors:
        manifest=build_manifest(root)
        manifest["validation"]={"script":"scripts/validate-packet.py","status":"passed","validated_at":datetime.now(timezone.utc).isoformat(),"errors":0,"warnings":len(warnings)}
        (root/MANIFEST).write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
        if args.refresh_checksums: write_checksums(root)
        findings=validate(root); errors=[x for x in findings if x.level=="error"]; warnings=[x for x in findings if x.level=="warning"]
    result={"packet":PACKET_NAME,"version":PACKET_VERSION,"root":str(root),"validated_at":datetime.now(timezone.utc).isoformat(),"passed":not errors,"counts":{"errors":len(errors),"warnings":len(warnings),"info":0},"findings":[x.as_dict() for x in findings]}
    if args.json: print(json.dumps(result,indent=2))
    else:
        print(f"{PACKET_NAME}: {'PASS' if not errors else 'FAIL'} ({len(errors)} errors, {len(warnings)} warnings)")
        for x in findings: print(f"[{x.level.upper()}] {x.code}: {x.message}" + (f" ({x.path})" if x.path else ""))
    raise SystemExit(0 if not errors else 1)
if __name__=="__main__": main()
