# API / Contract Assurance Research Agenda

## Primary systems and categories

- Schemathesis
- Pact
- OpenAPI diff systems
- GraphQL compatibility
- protobuf compatibility
- AsyncAPI/event compatibility
- SDK/API evolution tools

## Research standard

For every consequential source:

- verify current repository, maintenance state, release/version, license, and security policy;
- inspect actual schemas, CLI/API contracts, code architecture, tests, fixtures, benchmark methodology, failure behavior, and offline/network behavior;
- distinguish measured results from marketing claims;
- identify build-versus-integrate decisions;
- record data sent to external services and credential implications;
- inspect extensibility and output stability before defining an adapter;
- preserve historical reasoning when current source status changes.

## Required comparative questions

1. What domain semantics already have mature standards or tools?
2. What differentiated value belongs in the capability engine?
3. Which evidence can be imported versus generated?
4. What cannot be made language/platform/provider agnostic?
5. What false-positive/false-proof/false-safety patterns dominate?
6. What exact security boundary is needed for execution?
7. What evaluation corpus can establish mature-v1 claims?
