---
title: Skin Engine (Skin/Theme)
created: 2026-04-10
updated: '2026-06-08'
type: concept
tags:
- agent-system
- cli
- ai-ml
sources:
- title: Hermes-Wiki Repository
  type: web
  url: https://github.com/cclank/Hermes-Wiki
confidence: high
contested: false
---
# Skin Engine

## Overview

The visual appearance of the Hermes CLI is entirely driven by YAML [1]. Users can customize colors, spinner animations, and branding copy without modifying code [1].

## Skin File Structure

Skin files are located in `~/.hermes/skins/*.yaml` [1]. All fields are optional; missing values inherit from the `default` skin [1].

```yaml
name: mytheme
description: Custom theme

colors:
  banner_border: "#CD7F32"     # Banner border
  banner_title: "#FFD700"      # Banner title
  banner_accent: "#FFBF00"     # Section title
  ui_accent: "#FFBF00"         # UI accent color
  ui_ok: "#4caf50"             # Success
  ui_error: "#ef5350"          # Error
  ui_warn: "#ffa726"           # Warning
  prompt: "#FFF8DC"            # Input prompt
  response_border: "#FFD700"   # Response box border

spinner:
  waiting_faces: ["(⚔)", "(⛨)"]
  thinking_faces: ["(⌁)", "(<>)"]
  thinking_verbs: ["forging", "plotting"]
  wings: [["⟪⚔", "⚔⟫"], ["⟪▲", "▲⟫"]]

branding:
  agent_name: "My Agent"
  welcome: "Welcome!"
  goodbye: "Bye! ⚕"
  response_label: " ⚕ Response "
  prompt_symbol: "❯ "
```

## Switching Skins

```bash
/skin mytheme          # Switch within session [1]
hermes config set display.skin mytheme  # Persist configuration [1]
```

## Different Skins per Profile

Skin files are located in the `skins/` directory of each Profile [1]. Different Profiles can use different visual themes [1].

## Related Pages
- [[I18N And Locales|i18n-and-locales]]

- [Configuration And Profiles](configuration-and-profiles.md) — Profile system (independent skins directory per Profile)
- [Cli Architecture](cli-architecture.md) — CLI architecture

## Key Source Code

- `hermes_cli/skin_engine.py` — Skin loading, inheritance, rendering [1]