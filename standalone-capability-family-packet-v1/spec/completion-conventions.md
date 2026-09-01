# Shared Completion Conventions

**Status:** Top-level semantics `ESTABLISHED`; exact v0 schema `PROVISIONAL`

## 1. Common top-level states

| State | Meaning |
|---|---|
| `complete` | All required work for the accepted plan completed and no material limitation prevents the requested conclusion. |
| `complete_with_limitations` | Required work completed, but declared limitations materially qualify interpretation. |
| `partial` | Some required work, scope, evidence, or upstream result is missing, denied, unsupported, stale, failed, or timed out. |
| `failed` | Foundational validation or execution failure prevents a usable result for the request. |
| `cancelled` | External cancellation or accepted stop condition ended the operation. |

## 2. Common node outcomes

```text
succeeded
failed
unavailable
skipped
timed_out
cancelled
denied
incompatible
stale
```

Capabilities may add domain details without changing the top-level meaning.

## 3. Mandatory distinctions

Completion MUST distinguish, where applicable:

- no conclusion/problem found in analyzed scope;
- provider intentionally disabled;
- provider unavailable;
- permission denied;
- unsupported subject/environment/language/platform;
- provider failed or timed out;
- stale/reused evidence;
- missing upstream result;
- corrupt or unverifiable result;
- partial subject scope;
- missing runtime/production/consumer evidence;
- planned sampling or approximation.

## 4. Truthful claim rule

A consumer must inspect completion, subject, scope, provider coverage, freshness, and limitations before describing the outcome. “No findings,” “tests passed,” “compatible,” “safe,” “ready,” or “conformant” must be qualified by the actual scope and completion semantics.
