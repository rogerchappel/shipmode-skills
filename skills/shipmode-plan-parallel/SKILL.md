---
name: shipmode-plan-parallel
description: Plan parallel agent work for an already bounded software task using interfaces, exclusive file ownership and dependency gates; use before delegation, not as permission to spawn agents.
---

# Plan parallel work

Build an integration plan from an agreed scope and available repository layout.

1. Identify work that can proceed independently. Prefer sequential work when tasks share a small implementation surface or an interface is still unsettled.
2. Freeze the smallest shared contract: function/API signature, data shape, error behavior, and compatibility expectations. Label undecided parts.
3. Give each workstream exclusive write ownership of concrete paths. Assign one integration owner for shared files. Read access can overlap. Resolve overlapping ownership before proposing simultaneous edits.
4. Mark dependencies and gates: what can start now, what waits for a contract or artifact, and what the integration owner verifies after combining work.
5. Provide each worker a brief with input, owned files, expected artifact, relevant checks, and a stop/report condition for scope or interface changes.

Return workstream/owner/path/contract/dependency/check rows plus integration order. This skill produces a plan; it does not authorize spawning agents. If delegation is unavailable or unauthorized, retain the plan and suggest a sequential order.

Read [example.md](example.md) when adapting the plan to a small repository.
