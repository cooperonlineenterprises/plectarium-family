# Capability Planning Conventions

**Status:** `ACCEPTED` for material-effect capabilities

A capability SHOULD produce an inspectable plan before materially consuming resources, executing project code, invoking external tools, using network or credentials, opening browsers, reading controlled infrastructure/databases/production, or generating significant outputs.

A plan should expose:

- exact capability and operation;
- subject identity and scope;
- providers/adapters/tools and versions;
- dependency tasks and execution order;
- requested permissions and denied-right consequences;
- network destinations/data categories where practical;
- credentials by opaque reference, never embedded secret;
- sandbox/environment and writable paths;
- resource/time/output budgets;
- cache and evidence-reuse basis;
- expected result schemas and artifacts;
- known limitations and stop conditions.

Material substitutions require a new plan or an explicitly bounded substitution rule. A plan digest helps a user or harness ensure the reviewed plan is the executed plan.
