---
name: pr-qa-description
description: Use whenever the coding agent prepares, creates, or edits a GitHub pull request description. Ground the description in the actual change and include the product, navigation, and E2E risk context needed to understand and test its behavior. Do not use for ordinary coding, planning, or review when no PR description is being authored.
---

# PR QA Description

Write or improve the pull request description using evidence from the actual diff, relevant tests, author-provided context, and the repository's PR template.

First decide whether Arch browser goal QA applies from the change's real production consumers. Do not decide from change size or from a frontend-versus-backend label alone.

Goal QA applies when the change alters, or could regress, behavior that an end user or supported product operator can trigger and observe through a supported browser product surface. This includes backend behavior consumed by that surface, user actions and outcomes, permissions, state transitions, and user-visible errors or recovery. Existing goals may still be worth rerunning when intended behavior is unchanged but their production path changed.

Goal QA does not apply when the change is limited to internal QA infrastructure, judge or worker orchestration, CI and deployment mechanics, developer tooling, documentation, tests, logging or observability, or backend behavior with no current supported product-surface consumer. Performance-only changes are also excluded from goal testing for now; describe their diagnostics or benchmarks under ordinary verification.

When goal QA does not apply:

- put `@arch skip qa` on its own line in the PR description;
- give one concise reason in an existing testing section or a compact `QA decision` section; and
- do not invent pages, navigation, user setup, goals, or E2E scenarios.

Do not use the directive when a backend or infrastructure change has a current browser-visible consumer whose behavior could change.

For qualifying behavior changes, capture the useful product context:

- the user-visible change, preferably as before → after behavior;
- the affected pages or UI components and where they appear;
- how a user reaches the changed behavior;
- required setup or state, such as data, role, permissions, account state, or a feature flag;
- behavioral variants only when the implementation or tests show that behavior differs by state, role, or another condition;
- potential failure modes or behavioral boundaries exposed by the change, grounded in the changed code or tests; and
- a concise set of high-value E2E coverage areas for the changed behavior and those risks.

Treat these as information requirements and a preferred extraction block, not a required format for the whole PR description. Follow the repository's PR template, local authoring instructions, and any other applicable PR-writing skill. Preserve human-authored content and every existing section.

Keep the qualifying QA information together whenever the format permits, in this order:

1. If the template already has a dedicated `QA`, `Testing`, `Test plan`, or equivalent section that can hold the information clearly, put it there.
2. Otherwise add a compact `## QA context` section.
3. Only distribute the information across unrelated existing sections when the required format prohibits adding a suitable section or subsection.

Use the following labels when they fit the available evidence and format. When reusing an existing QA section, omit the `## QA context` heading. Keep the selected QA section or block self-contained so downstream extraction does not depend on unrelated sections. Concise repetition of details stated elsewhere is acceptable; do not create multiple QA blocks.

```markdown
## QA context
- User-visible change:
- Affected pages/components:
- How to reach it:
- Required setup/state:
- Behavioral variants:
- E2E considerations:
```

Omit irrelevant or empty labels. Exact UI copy, product rationale, or test evidence may be included when it materially clarifies a qualifying behavior change. Keep E2E considerations at the user-observable behavior level: identify the flow, state transition, permission boundary, integration boundary, or failure path worth validating. Do not turn them into detailed test scripts or a complete set of test goals; downstream goal creation decides the exact new or revised goals against the existing goal inventory.

## Context for downstream goal creation

Give the downstream goal planner enough concrete evidence to design valuable behavior checks without asking it to invent product behavior:

- Describe the real user job and why its result matters, not just the changed page or control.
- State the business rules and code-backed behavior that govern the result. Name the actual starting state, supported actions, and downstream outcome; include roles, permissions, records, or configuration only when they materially affect this flow.
- Trace the supported journey across the connected parts of the product a real user would use, including the meaningful decisions, changes, and follow-through. Be specific enough to expose non-trivial combinations that arise naturally in that work.
- Explain concrete failure risks supported by the implementation. Do not substitute a shallow presence check unless visibility is itself the behavior at risk.

This is context for goal creation, not the final goal design. Keep it proportional to the changed behavior rather than supplying an exhaustive scenario inventory.

Do not invent product behavior, navigation, setup, variants, failure modes, or E2E coverage. Infer a risk only when it follows from the changed control or data flow, an evidenced behavioral boundary, or a nearby test, and present it as something worth validating rather than as confirmed product behavior. Before treating navigation or setup as unknown, keep tracing the relevant routes, component callers, authentication and role checks, feature flags, fixtures, tests, seed data, and nearby documentation. Leave a short, clearly marked question for the author only when the answer depends on inaccessible code or data, unavailable environment configuration, or product intent that is not represented in the repository; state exactly what information is missing. Do not add exhaustive file lists, generic implementation summaries, a complete QA scenario inventory, or an executable goal set.


## Cross-repository deployment coordination

When one logical implementation produces pull requests in more than one repository, coordinate those PRs as one deployment set:

1. Determine the complete repository set from the work performed in the current task. Do not group unrelated PRs.
2. Create every member as a draft before finalizing any member's description.
3. Read each canonical URL from GitHub (for example, `gh pr view --json url`); do not construct or guess URLs.
4. Edit every member so it contains exactly one block in this form:

```markdown
## Deployment coordination
- Related PRs:
    - https://github.com/acme/frontend/pull/123
    - https://github.com/acme/backend/pull/456
```

On each PR, omit that PR's own URL and list every other member exactly once. Use only canonical `https://github.com/<owner>/<repository>/pull/<positive-number>` URLs. The block must use the heading and label exactly as shown. It may appear alongside `QA context`, the repository template, and human-authored content; preserve all of them.

After editing, fetch every description again and verify that each member resolves to the same complete set: its own canonical URL plus its listed URLs must equal the full set. Stop and repair the descriptions before marking any PR ready for review if a link is missing, duplicated, malformed, self-referential, or names a PR outside the set.

For a change contained in one repository, omit the deployment coordination block entirely.
