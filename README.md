# Arch PR Authoring Plugin

A cross-agent plugin that helps authors write PR descriptions with enough grounded product context for Arch to turn the description into useful goals later.

Built by [Foothill Labs](https://foothill.sh).

The repository contains one canonical `pr-qa-description` skill and native packaging for Claude Code, Codex, Cursor, and Devin.

## Migrate from the legacy plugins

Run the matching migration once in each developer environment. Remove only the named legacy package and marketplace; do not remove unrelated plugins.

### Claude Code

```bash
claude plugin uninstall pr-qa-authoring@arch-pr-authoring --scope user --yes
claude plugin marketplace remove arch-pr-authoring --scope user
claude plugin marketplace add https://github.com/the-simulation-company/arch-plugin.git --scope user
claude plugin install arch-plugin@arch-pr-authoring --scope user
```

### Codex

```bash
codex plugin remove arch-codex-plugin@arch-pr-authoring
codex plugin marketplace remove arch-pr-authoring
codex plugin marketplace add the-simulation-company/arch-plugin --ref main
codex plugin add arch-plugin@arch-pr-authoring
```

### Cursor

Confirm that the legacy clone has no local changes, then replace it:

```bash
git -C ~/.cursor/plugins/local/arch-cursor-plugin status --short
rm -rf ~/.cursor/plugins/local/arch-cursor-plugin
git clone https://github.com/the-simulation-company/arch-plugin.git \
  ~/.cursor/plugins/local/arch-plugin
```

Reload Cursor with **Developer: Reload Window**.

### Devin

Organization admins should:

1. Remove any Devin plugin installed from a legacy provider repository.
2. Install `the-simulation-company/arch-plugin` from **Customize → Plugins → Add plugin → From repository** at organization scope.
3. Remove duplicate personal `pr-qa-description` skills after the organization installation is active.
4. Start a new Devin session.

For Devin Local installations, use:

```bash
devin plugins remove pr-qa-authoring
devin plugins install the-simulation-company/arch-plugin
```

If the legacy package is not installed, skip its removal command and continue with the new installation.

### Instruction for an agent

```text
Migrate this environment from the legacy Arch PR-authoring plugin to
the-simulation-company/arch-plugin. Follow the matching provider steps in the
repository README, remove only the legacy package and marketplace, verify that
arch-plugin v0.2.0 is installed, and restart or reload the agent environment.
```

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
