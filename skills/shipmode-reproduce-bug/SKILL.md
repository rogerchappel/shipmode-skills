---
name: shipmode-reproduce-bug
description: Reproduce a reported software bug from raw inputs and define a regression check that fails before a fix; use for bug reports, not general feature planning.
---

# Reproduce a bug

Establish what happens before proposing a fix.

1. Read the report, smallest relevant source, and existing checks. Record runtime and exact setup needed; use synthetic inputs when possible.
2. Run a minimal reproduction with explicit input, expected behavior grounded in the requirement, actual output, command, and exit status. Narrow the trigger while retaining the failure. If you cannot run it, label it unverified and give the command another person can run.
3. Separate observed facts from a suspected cause. A plausible explanation alone is not a reproduction.
4. Define or add a regression check around observable behavior. Run it against the original implementation and record the failure. Include a neighboring case to detect an overbroad fix.
5. If fixing is authorized, make the narrow change and rerun the regression and relevant existing checks. Preserve the failing baseline evidence; report any unrun cases.

Return a reproduction note, regression check, suspected cause (if useful), and before/after evidence. Do not claim resolution from a passing baseline suite that never exercised the trigger.

See [example.md](example.md) for an empty-query failure.
