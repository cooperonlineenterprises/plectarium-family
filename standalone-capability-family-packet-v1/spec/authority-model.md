# Shared Authority and Permission Model

**Authority:** Normative security/authority semantics  
**Status:** `ESTABLISHED` separation; vocabulary is `PROVISIONAL v0`

## 1. Authority separation

```text
Capability plan requests bounded permission.
External user/harness/policy accepts or denies permission.
Capability executes only within accepted permission.
Capability result provides evidence.
External project process decides and authorizes downstream action.
```

Permission to inspect or execute does not imply permission to mutate, publish, deploy, communicate, or create governance records.

A canonical character identity is presentation and interaction metadata. Anthropomorphic language does not imply that Verity, Titra, Ortha, Genea, Echo, Harmia, Iris, Atlas, Janus, or Sibyl can grant permission or authorize downstream action.

## 2. Provisional permission vocabulary

| Permission | Meaning |
| --- | --- |
| repository_read | Read declared repository paths. |
| repository_write | Modify declared repository paths. |
| git_read | Read Git objects/history/refs. |
| git_write | Modify Git index, refs, commits, or configuration. |
| project_execution | Run project-defined build/test/generation/runtime code. |
| external_process_execution | Invoke declared non-project tools. |
| network | Open declared network connections. |
| browser_execution | Run controlled browser sessions. |
| infrastructure_read | Read plans/state/provider metadata/cloud state. |
| infrastructure_apply | Create/update/delete infrastructure. |
| database_read | Read schema/data/metadata from a database. |
| database_write | Modify database schema or data. |
| production_access | Access a production environment or data plane. |
| output_write | Write durable result/output artifacts. |
| cache_write | Write capability-owned cache. |
| temporary_write | Write bounded temporary data. |
| credential_access | Use declared credential references. |
| secret_access | Read secret values beyond opaque credential use. |
| artifact_publish | Publish packages/images/releases/artifacts. |
| deployment | Deploy or promote software. |
| issue_creation | Create or mutate issue/task records. |
| external_communication | Send messages, webhooks, notifications, or external reports. |

## 3. Default-deny rules

A capability MAY declare permissions in discovery, but the declaration is not acceptance. The accepted plan must bind exact scope, operation, provider/tool identities, writable paths, network policy, credential references, environment, resource limits, and output expectations.

The following are denied unless explicit:

- all writes except approved output/cache/temp;
- project execution;
- network;
- browser execution;
- infrastructure/database/production access;
- credentials/secrets;
- publication/deployment/communication/issue creation.

Production mutation permissions SHOULD remain unsupported in evidence capabilities. If a future product performs authorized actions, it requires a distinct family review and capability class rather than silently extending these evidence-producer products.

## 4. No transitive permission inheritance

An adapter, subprocess, browser page, imported capability, or external result cannot inherit rights beyond the accepted plan. A capability consuming an upstream result does not acquire the upstream capability’s execution permissions.

## 5. Permission evidence

Every result SHOULD record:

- requested and accepted permissions;
- denied permissions that affected completeness;
- actual provider/tool executions;
- network and credential categories used;
- writable locations;
- resource limits and termination outcomes;
- unexpected-effect detection where supported.
