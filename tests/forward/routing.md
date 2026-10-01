# Shipmode routing trial

Single-run observed routing decisions based only on the five SKILL.md name and description frontmatter fields. No bodies, examples, or other trials were consulted, and no prompt tasks were executed. These decisions are not accuracy guarantees.

| # | Prompt | Decision | Reason |
|---|---|---|---|
| 1 | Make this vague feature brief small enough for tomorrow and define done. | shipmode-scope-build | A vague feature brief needs a bounded build slice and observable acceptance checks. |
| 2 | Divide this agreed change across agents without both editing the same files. | shipmode-plan-parallel | An agreed change calls for parallel planning with exclusive file ownership. |
| 3 | The empty search fails; get a minimal repro and a check that catches it. | shipmode-reproduce-bug | A reported bug needs reproduction and a regression check. |
| 4 | Review this diff; the author says tests passed but there are no logs. | shipmode-review-evidence | Patch assessment requires actual test evidence alongside the diff. |
| 5 | Write the next engineer a release-readiness note with what is still unverified. | shipmode-handoff-release | A work-boundary handoff should state readiness, verification limits, and next actions. |
| 6 | What is Python list syntax? | none | General language syntax does not match any of the five described workflows. |
| 7 | Deploy this website now. | none | Deployment is outside these descriptions; the release handoff skill explicitly excludes deploying. |
| 8 | Write me a LinkedIn announcement. | none | Announcement writing is outside the described software workflows. |
| 9 | Fix this typo in README. | none | A direct, already clear typo fix needs neither scoping nor the other described workflows. |
| 10 | Estimate cloud hosting prices. | none | Hosting price estimation is outside the five described workflows. |
