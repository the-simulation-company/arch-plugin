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

## What it adds

The `pr-qa-description` skill asks the coding agent to ground the PR description in the diff, relevant tests, and repository template, then decide whether browser goal QA applies.

For qualifying changes, it captures the user-visible change, affected pages and components, navigation, required setup or state, and evidenced behavioral variants and E2E risks.

For changes without a supported browser-product consumer, it adds the exact `@arch skip qa` directive and a concise reason instead of inventing browser coverage.

Human-authored and template sections are preserved. The skill traces relevant repository evidence before asking the author for context that is genuinely unavailable.

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
