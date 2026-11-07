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

## 11. Bedrock infrastructure with no product monitoring surface

**Evidence available:** A single-repository PR changes Bedrock pool routing and quota telemetry. Related AWS SDK calls and Datadog metrics live in the product repository, but route, component, and test evidence shows no supported product UI for viewing pool selection or quota usage. Those facts require AWS or Datadog access, which has not been verified for the QA account. No browser-visible consumer's behavior is affected.

**Expected outcome:** The description names the AWS/Bedrock and Datadog impacts, distinguishes code changed here from externally observed infrastructure state, and states that the product browser cannot verify pool selection or quota usage. It identifies the external verification and unverified access without claiming checks passed. It includes `@arch skip qa` with a concise reason and invents neither a monitoring journey nor a deployment coordination block. The skip directive does not replace the external-impact context.

## 12. Mixed product flow and external infrastructure impact

**Evidence available:** A Bedrock fallback change affects a chat flow reached through **Projects → Open project → Chat**, with tests covering a successful answer and the product's visible failure state. The selected AWS pool and quota consumption are observable only through provider tooling or telemetry, not through that chat UI.

**Expected outcome:** The description retains browser goal QA for the evidenced chat outcomes and supplies their navigation and setup. In the same QA block it separates those outcomes from pool selection and quota usage, naming the external verification needed for the latter under ordinary verification. It does not treat receiving an answer as proof of a particular pool, invent product monitoring controls, or skip the entire PR.

## 13. Evidenced product monitoring surface

**Evidence available:** A PR changes quota data returned by an external provider. The supported `/admin/usage` page displays the reported usage and an unavailable-data state; route and permission tests show how organization administrators reach it. The UI does not show which AWS pool served a request. API contract tests passed, but a live provider comparison has not been run.

**Expected outcome:** The description includes browser coverage for administrators viewing reported usage and the unavailable-data state, grounded in that real product surface. It keeps AWS pool selection outside browser coverage, records the passed contract tests separately from the pending live comparison, and does not claim displaying usage proves its accuracy against the provider. It does not skip goal QA merely because an external service is involved.

## 14. Impact outside the repository with incomplete evidence

**Evidence available:** A PR changes an API payload consumed by a separate worker repository. Local tests establish the new payload, but the worker repository and its deployment configuration are inaccessible. No companion PR was created, and the evidence does not establish whether the worker's result is exposed in the product UI.

**Expected outcome:** The description names the worker dependency and payload boundary, distinguishes the local change from its unverified downstream impact, and identifies the missing consumer contract, deployment, and UI-exposure evidence. It asks a focused author question rather than inventing a worker page, assuming downstream compatibility, or asserting that browser QA is definitively applicable or inapplicable. It does not invent a related PR URL or a deployment coordination block.
