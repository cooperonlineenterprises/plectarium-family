# Capability Packages

This plural `.agents/` tree contains discoverable agents, skills, and
workflows. The singular `.agent/` tree remains the live governance and state
plane.

Capabilities inherit and may narrow the current task's authority. They cannot
expand permission, approve their own work, or bypass kernel policy and
validation. Under `DEC-0001`, the read-only reviewer and safe-change workflow
are adopted for `TASK-0001` and later authorized family-repository work. Their
owner role is `family_repository_maintainer`; they remain non-authorizing and
must not review or modify capability or suite semantics outside the active
task.
