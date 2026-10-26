# PR description authoring

When preparing, creating, or editing a pull request description, invoke the `pr-qa-description` skill before writing the description. This standing order applies only to PR-authoring work; it does not apply to ordinary coding, planning, or review.

# Releases

Every PR must bump the same stable version in all four provider manifests (`.claude-plugin`, `.codex-plugin`, `.cursor-plugin`, and `.devin-plugin`). Choose the next version from current `main`. The required `Plugin version` check enforces this, including documentation changes.

Merging into `main` automatically publishes the matching GitHub release. After merging, verify the `Plugin release` workflow succeeds and the release tag points to the merged commit before declaring completion. A failed publication remains unfinished release work; fix it and rerun the failed job. Never move an existing release tag.
