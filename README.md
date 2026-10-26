# Arch PR Authoring Plugin

A cross-agent plugin that helps authors write PR descriptions with enough grounded product context for Arch to turn the description into useful goals later.

Built by [Foothill Labs](https://foothill.sh).

The repository contains one canonical `pr-qa-description` skill and native packaging for Claude Code, Codex, Cursor, and Devin.

## Install

### Claude Code

```bash
claude plugin marketplace add https://github.com/the-simulation-company/arch-plugin.git --scope user
claude plugin install arch-plugin@arch-pr-authoring --scope user
```

Start a new Claude Code session after installation.

### Codex

```bash
codex plugin marketplace add the-simulation-company/arch-plugin --ref main
codex plugin add arch-plugin@arch-pr-authoring
```

Start a new Codex task after installation.

### Cursor

```bash
mkdir -p ~/.cursor/plugins/local
git clone https://github.com/the-simulation-company/arch-plugin.git \
  ~/.cursor/plugins/local/arch-plugin
```

Reload Cursor with **Developer: Reload Window**.

### Devin

Organization admins can install the plugin for every repository and session origin:

1. Open **Customize → Plugins → Add plugin → From repository**.
2. Use `https://github.com/the-simulation-company/arch-plugin`.
3. Select the organization scope and install the plugin.

Start a new Devin session after installation.

## Update

These steps apply to the installation methods above. Updates become available after changes merge to the branch you track (normally `main`); an open PR does not update installed copies. Start a new session/task after updating.

### Claude Code

Update the installed plugin:

```bash
claude plugin update arch-plugin@arch-pr-authoring
```

For automatic updates, open `/plugin` → **Marketplaces** → **arch-pr-authoring** → **Enable auto-update**. Third-party marketplaces have auto-update off by default. Running sessions keep their loaded version until `/reload-plugins` or a new session. See [Claude Code's update docs](https://code.claude.com/docs/en/discover-plugins#keep-plugins-updated).

### Codex

Refresh the Git marketplace:

```bash
codex plugin marketplace upgrade arch-pr-authoring
```

Restart the desktop app and start a new task to load refreshed plugin files. This is the explicit refresh path; do not assume Git-installed plugins update automatically in every client. See [Codex's marketplace instructions](https://developers.openai.com/plugins/build/plugins#add-a-marketplace-from-the-cli).

### Cursor

For the local clone installed above:

```bash
git -C ~/.cursor/plugins/local/arch-plugin pull --ff-only
```

Then run **Developer: Reload Window** and start a new chat. This local clone does not pull changes automatically. If the pull reports local changes or diverged history, reconcile those changes before updating; do not reset away local edits.

### Devin

**Cloud sessions automatically fetch plugin content at session start from the tracked branch.** With the repository installation above and no commit pin, that is the repository's default branch. After an Arch plugin change merges, start a new Devin session; existing sessions keep the version they loaded.

In **Customize → Plugins**, open the plugin's details to check its tracked ref or pinned SHA. A SHA-pinned install stays at that commit until an administrator updates the pin. ZIP uploads are fixed copies and must be replaced to receive changes.

To refresh the Customize listing after a source change, choose **Plugin settings → Reindex plugins** and check that indexing succeeds. Reindexing refreshes the web listing; cloud sessions fetch plugins directly and do not wait for that index.

For a stale Devin CLI/Desktop local installation:

```bash
devin plugins update arch-plugin
```

Then start a new session. See [Devin's update rollout docs](https://docs.devin.ai/product-guides/plugins#how-updates-roll-out) and [CLI plugin management](https://docs.devin.ai/cli/extensibility/plugins/overview#managing-plugins).

## What it adds

The `pr-qa-description` skill asks the coding agent to ground the PR description in the diff, relevant tests, and repository template, then decide whether browser goal QA applies.

For qualifying changes, it captures the user-visible change, affected pages and components, navigation, required setup or state, and evidenced behavioral variants and E2E risks.

For changes without a supported browser-product consumer, it adds the exact `@arch skip qa` directive and a concise reason instead of inventing browser coverage.

Human-authored and template sections are preserved. The skill traces relevant repository evidence before asking the author for context that is genuinely unavailable.

## Releasing changes

Every PR increments the same stable `major.minor.patch` version in all four provider manifests. The required `Plugin version` check compares against the current base; update your branch and version if another release merges first. This applies to documentation changes too, so every merged snapshot has its own version.

On a merge to `main`, the `Plugin release` workflow publishes that version as a GitHub release with generated notes. Verify the workflow and release before considering the change shipped. To recover a failed publication, fix the cause and rerun the failed job; an already-published tag is accepted only when it points to that workflow's commit.

## Repository layout

The canonical skill lives in `skills/pr-qa-description/`. Provider manifests and standing-order adapters live at the repository root:

- `.claude-plugin/`
- `.codex-plugin/`
- `.cursor-plugin/`
- `.devin-plugin/`
- `.agents/plugins/marketplace.json`
- `AGENTS.md`
- `rules/`

Provider adapters must reference the canonical root skill rather than carrying provider-specific copies.
