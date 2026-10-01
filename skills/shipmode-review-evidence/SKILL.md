---
name: shipmode-review-evidence
description: Review a software change against requirements, diff and actual test evidence; use when assessing a patch or PR, not when writing a release announcement.
---

# Review against evidence

Assess the change and the strength of its verification separately.

1. Read the requested behavior and diff (or explicit before/after files). Identify changed paths and the exact version covered by each test record.
2. Inspect test commands, exit statuses, assertions, and results. Distinguish tests you ran from supplied logs and proposed checks. If logs predate a change or omit the trigger, they do not establish the changed behavior.
3. Map each acceptance requirement to a code path and an observed check. Run focused checks when available and within scope; otherwise say what remains unverified.
4. Report concrete defects with location, trigger, impact, and a verification step. Keep missing evidence distinct from confirmed defects. Do not invent a finding to fill a template.
5. Give a recommendation proportional to what was checked: ready for the stated scope, changes needed, or insufficient evidence. Avoid treating passing tests as proof of all behavior or security.

Return findings first, then a requirement/evidence/gap table and recommendation. Reviewing does not authorize publishing, merging, or deploying.

Read [example.md](example.md) for a patch whose supplied test misses the bug.
