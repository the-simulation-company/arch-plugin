# PR description behavior cases

Use these cases to verify the installed plugin. Compare whether the resulting PR description contains the expected information; do not require exact headings or wording.

## 1. Route, role, component, and changed behavior

**Evidence available:** The diff changes the `Bulk approve` button on `/admin/orders`. Tests show it is visible only to managers and changes from disabled to enabled when at least one pending order is selected.

**Expected outcome:** The description identifies the route and component, states the before → after behavior, and names the manager role and pending-order setup. It does not invent behavior for other roles or write a full QA suite.

## 2. Navigation and setup inferred from nearby code

**Evidence available:** The edited component is a Slack confirmation panel. The diff does not explain navigation, but its parent route and nearby tests show that users reach it through **Settings → Integrations → Slack** after connecting a workspace.

**Expected outcome:** The description includes that evidenced navigation and connected-workspace setup. It does not guess additional permissions, flags, or variants.

## 3. Internal-only change

**Evidence available:** The PR refactors a server-side cache adapter without changing responses, rendered UI, or externally observable behavior.

**Expected outcome:** The description contains `@arch skip qa` on its own line, gives one concise reason that browser goal QA does not apply, and does not fabricate pages, navigation, setup, or QA scenarios.

## 4. Backend change with a browser-visible consumer

**Evidence available:** The PR changes the authorization response used by the browser's team-settings page. The intended UI is unchanged, but a regression could hide settings from organization administrators.

**Expected outcome:** The description does not skip goal QA merely because the diff is backend-only. It identifies the administrator settings flow and the existing behavior worth rerunning without inventing a visible redesign.

## 5. Existing template and human-authored content

**Evidence available:** The repository template contains `## Summary`, `## Rollout`, and a checklist. The author has already written a rollout note and checked two items.

**Expected outcome:** The description preserves every template section, the rollout note, and the checklist state while adding useful product context in compatible locations. It does not replace the template with the plugin's suggested headings.


## 6. Two-repository implementation

**Evidence available:** One task changes a frontend repository and an API repository. Both PRs have been created as drafts and GitHub reports their canonical URLs as `https://github.com/acme/frontend/pull/123` and `https://github.com/acme/backend/pull/456`.

**Expected outcome:** Each description contains the exact deployment coordination heading and label. The frontend PR lists only the backend URL; the backend PR lists only the frontend URL. Existing QA and template content remains intact.

## 7. Three-repository implementation

**Evidence available:** One task creates draft PRs in frontend, backend, and worker repositories.

**Expected outcome:** Every PR lists the other two canonical URLs exactly once. Combining a PR's own URL with its two links yields the same three-member set for every PR.

## 8. Standalone implementation

**Evidence available:** The task changes and creates a PR in only one repository.

**Expected outcome:** The PR has no deployment coordination block.

## 9. Asymmetric or incomplete set

**Evidence available:** PR A lists PR B and PR C, but PR B lists only PR A.

**Expected outcome:** The agent does not mark the PRs ready. It edits the incomplete descriptions, fetches all descriptions again, and verifies the same complete three-member set.

## 10. Invalid, duplicate, or self link

**Evidence available:** A coordination block contains a guessed URL, a non-canonical URL, the current PR's own URL, or the same related URL twice.

**Expected outcome:** The agent replaces invalid links with canonical URLs from GitHub, removes self and duplicate links, and re-verifies every member before marking any PR ready.

## 11. Product development tools versus customer administration

**Evidence available:** An audit-software PR removes an extra rollout flag from a browser-based QA console used by the engineers building that software. Customer organization administrators cannot access it. No customer workflow changes and no QA scope for the console has been requested.

**Expected outcome:** The description uses `@arch skip qa`, explains that this console supports building the product rather than using it as a customer, and keeps any console checks in ordinary verification. An admin role and a route alone do not justify customer coverage. If the author explicitly requests testing the console, the description instead includes its actual platform-admin setup and changed behavior.

## 12. Mixed development-tool and customer-workflow changes

**Evidence available:** The same PR also fixes saving a customer organization's notification preferences in Settings. Customer organization administrators can edit those preferences and reopen Settings to see the saved values.

**Expected outcome:** The description does not use `@arch skip qa`. Its browser QA context covers saving and reopening the customer's preferences, while engineering-console checks remain in ordinary verification. Customer administration is not excluded merely because its users are administrators. Likewise, a product sold to developers or operators still receives coverage for those customers' workflows.
