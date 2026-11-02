# PR description authoring

When preparing, creating, or editing a pull request description, pushing changes to an existing PR, or preparing an authorized merge, invoke the `pr-qa-description` skill. Keep the PR description and QA context up to date as the change evolves, and confirm they describe the final version before merging. This standing order does not apply to ordinary coding, planning, or review outside these PR lifecycle steps.

# Releases

Every PR must bump the same stable version in all four provider manifests (`.claude-plugin`, `.codex-plugin`, `.cursor-plugin`, and `.devin-plugin`). Choose the next version from current `main`. The required `Plugin version` check enforces this, including documentation changes.

Merging into `main` automatically publishes the matching GitHub release. After merging, verify the `Plugin release` workflow succeeds and the release tag points to the merged commit before declaring completion. A failed publication remains unfinished release work; fix it and rerun the failed job. Never move an existing release tag.
