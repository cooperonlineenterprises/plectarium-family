# Family Security Policy and Threat Model

**Authority:** Family security governance  
**Status:** `ESTABLISHED` principles; capability-specific controls remain mandatory

## 1. Security objective

A capability must be useful without turning untrusted repositories, build scripts, analyzers, browsers, networks, infrastructure providers, databases, telemetry, or AI context into ambient authority.

## 2. Trust boundaries

```text
trusted capability engine
    ├── untrusted subject/repository/input
    ├── untrusted project configuration
    ├── trusted-but-constrained adapter
    ├── untrusted specialist-tool output
    ├── optional network services
    ├── optional credentials and controlled environments
    ├── cache and artifact stores
    ├── optional AI provider
    └── result consumers
```

## 3. Safe defaults

- target state read-only where possible;
- repository, Git, infrastructure, database, production, and artifact mutation denied;
- network denied;
- credentials and secrets unavailable;
- project/build/test execution denied unless intrinsic to the accepted plan;
- no shell interpolation by default;
- no automatic installation or update;
- direct argv and sanitized environments;
- explicit output/cache/temp locations;
- process, CPU, memory, time, output, archive, and graph limits;
- no inherited home-directory credentials;
- no Docker socket or privileged container;
- repository and external content treated as untrusted data, including instructions embedded in source and documentation.

## 4. Common threat catalogue

{bullets([
'malicious source repositories, comments, documentation, filenames, Git metadata, and configuration;',
'hostile build scripts, test runners, generators, plugins, package-manager hooks, and provider code;',
'compromised or substituted analyzers and malformed analyzer output;',
'network exfiltration and dependency/registry compromise;',
'credential, token, browser-session, database, cloud, and production secret exposure;',
'cache poisoning, forged result artifacts, stale evidence, and result substitution;',
'path traversal, symlink escape, special files, archive traversal, decompression bombs, and parser exploits;',
'container escape, browser escape, profiler/collector compromise, and denial of service;',
'prompt injection and poisoned context supplied to AI providers;',
'authority confusion in which analysis is mistaken for permission to act.'
])}

## 5. Domain escalation

Every capability seed extends this threat model. Execution-heavy capabilities must define exact isolation. UI Assurance must constrain browser origins/storage/downloads. Infrastructure and Migration Assurance must prove that analysis cannot apply changes. Runtime Investigation must bound production observation and instrumentation overhead. Release Assurance must prevent a `ready` result from becoming publication authority.

## 6. Result integrity

Durable results require checksums and producer/provenance records. Capabilities SHOULD support signatures where their threat model requires non-local trust. A consumer MUST validate the result identity and completion state before use. Corrupt or unverifiable results are not silently accepted.

## 7. Incident and vulnerability handling

Each implementation repository must publish a security policy, supported-version policy, private disclosure route, advisory process, and release-response procedure. This family packet does not grant permission to test third-party production systems.
