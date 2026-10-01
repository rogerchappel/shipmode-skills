# ShipMode Skills · 0.1.0

Five small developer workflows for turning a brief into reviewable work: scope a build, plan parallel work, reproduce a bug, review evidence, and hand off with known limits.

Prepared for the [ShipMode community](https://www.skool.com/shipmode-9184/about). Version 0.1.0 dated 2 October 2026 (Brisbane). Published under the MIT licence with Roger's approval. [Source repository](https://github.com/rogerchappel/shipmode-skills) · [Tagged source download](https://github.com/rogerchappel/shipmode-skills/archive/refs/tags/v0.1.0.zip). No live skill installation is performed by this repository.

| Skill | Output |
| --- | --- |
| `shipmode-scope-build` | Bounded build brief and observable acceptance checks |
| `shipmode-plan-parallel` | Contracts, exclusive file ownership, dependencies and integration plan |
| `shipmode-reproduce-bug` | Minimal reproduction and before/after regression evidence |
| `shipmode-review-evidence` | Findings, evidence gaps and scoped recommendation |
| `shipmode-handoff-release` | Usage, verification, limits, readiness and next actions |

## Start with three essentials

1. **Scope** a small outcome and define observable acceptance checks.
2. **Reproduce** a bug with a failing regression before fixing it.
3. **Review** the change against actual evidence and remaining gaps.

Use the parallel plan when multiple workers help; use the handoff at the work boundary.

## Try it in Codex

For a repository-scoped trial, copy the chosen skill folder(s) from `skills/` into `<your-project>/.agents/skills/`. Keep each folder's `SKILL.md` and `example.md` together. Check for an existing folder or matching skill name first; do not overwrite. Codex loads repo skills from `.agents/skills`; personal skills can live in `~/.agents/skills`. Invoke one explicitly, for example:

```text
$shipmode-scope-build Scope a completed filter for an in-memory task list.
Give acceptance checks; do not implement.
```

Codex detects skill changes automatically; restart if a new skill does not appear. To uninstall this pack, remove only the five `shipmode-*` folders you copied, preserving unrelated skills and any local edits you want to keep. No uninstall script is needed. These instructions are for manual local trials; plugin distribution is a later packaging option.

Setup checked against [official OpenAI build-skills documentation](https://learn.chatgpt.com/docs/build-skills) on 2 October 2026 Brisbane. Claude compatibility has not been tested: expect manual adaptation of discovery paths, invocation syntax and tools; no drop-in compatibility claim is made.

## Examples and checks

Start with the [example index](examples/README.md). A tiny synthetic Python fixture exercises search boundaries without dependencies. Run `python3 scripts/validate_pack.py` from this repository for structural and fixture checks. Read [test evidence](tests/REPORT.md) for independent model-task trials and their limits.

## Limits

These are instruction skills, not permission controls, security guarantees, or autonomous deployment tools. They preserve the user's task scope. Planning does not authorize delegation; handoff does not authorize publication. Model results vary and need review. Fixture checks do not validate real applications. No claim is made about Roger's daily use or measured productivity improvements.

## Attribution and licence

Original instructions, examples, fixtures and validation code were authored with Codex assistance for this pack. No third-party skill/library implementation was copied or vendored. Official OpenAI documentation informed setup paths and format and is linked rather than reproduced. The conventional MIT licence text is the sole standard legal text; see the [licence inventory](LICENCE-REVIEW.md) and [MIT licence](LICENSE). ShipMode and OpenAI names/links identify context, not an endorsement or a grant of trademark rights.

[Changelog](CHANGELOG.md) · [Release notes](RELEASE-REVIEW.md)
