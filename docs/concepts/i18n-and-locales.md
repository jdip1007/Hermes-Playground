---
title: i18n Internationalization and Multi-Language Architecture
created: 2026-05-20
updated: '2026-06-08'
type: concept
tags:
- agent-system
- i18n
- locales
- ai-ml
sources:
- title: Hermes-Wiki Repository
  type: web
  url: https://github.com/cclank/Hermes-Wiki
confidence: high
contested: false
---
# i18n Internationalization (v0.13.0)

`agent/i18n.py` + `locales/*.yaml` introduced a **thin-slice** internationalization approach — only translating "static strings displayed by Hermes itself to the user," while leaving agent output, logs, and stack traces untouched [1].

## 1. Design Principle: Thin Slice

Source code comment (`agent/i18n.py:1-20`) quoted directly [1]:

> Scope (thin slice, by design): only the highest-impact static strings shown to the user by Hermes itself —— approval prompts, a handful of gateway slash command replies, restart-drain notices. **Agent-generated output, log lines, error tracebacks, tool outputs, and slash-command descriptions all stay in English.**

**Why thin?**

| Not Translated | Reason |
|--------|------|
| Agent Output | LLM adapts to user language automatically; not controlled by Hermes |
| Log Lines | For developers; English is easier for grep/searching |
| Tool Output | Same as above, plus mostly structured data |
| Error Tracebacks | Native Python traces; Hermes shouldn't interfere |
| Slash Command Descriptions | Read by the agent too; mixed languages confuse the model |

Translated:
- Approval prompts (dangerous command confirmations users see multiple times daily)
- A few gateway slash command replies
- Restart-drain notifications ("Gateway restarting in 30s, X sessions entering drain")

## 2. Resolution Order [1]

```python
# agent/i18n.py
def t(key: str, *, lang: Optional[str] = None, **fmt_args) -> str:
    """Translate static string identified by `key`.

    Language resolution order:
        1. Explicit ``lang=`` argument (tests / temporary override)
        2. ``HERMES_LANGUAGE`` env var
        3. ``display.language`` in config.yaml
        4. ``"en"`` (baseline)
    """
```

The catalog is a **flat dict key path** (e.g., `approval.choose_long`, `gateway.draining`), not a nested tree — simple and O(1) lookup.

## 3. File Layout [1]

```
locales/
├── en.yaml      # baseline, keys not found in hermes will always fall back here
├── zh.yaml      # Simplified Chinese
├── zh-hant.yaml # Traditional Chinese (v0.13.0+)
├── ja.yaml
├── de.yaml
├── es.yaml
├── fr.yaml
├── tr.yaml
├── uk.yaml      # Ukrainian
├── af.yaml      # Afrikaans
├── ga.yaml      # Irish
├── hu.yaml      # Hungarian
├── it.yaml
├── ko.yaml
├── pt.yaml      # Portuguese
└── ru.yaml      # Russian
```

**16 YAML files** at HEAD. The "7 first-class production languages" highlighted in release notes are a subset with full coverage + tests + doc site translation: **zh / ja / de / es / fr / uk / tr**. The remaining 9 are community-contributed best-effort translations.

The documentation site (`website/`) also added **zh-Hans translation** (v0.13.0 PR #20329).

## 4. Fallback Chain [1]

```python
def t(key, lang=None, **fmt_args):
# 1. Look in the user's language catalog
# 2. If not found, look in the en catalog
# 3. If still not found, return the key itself (e.g., "approval.choose")
# 4. Return the key itself if any step throws an exception — never crash the agent
```

> This is the critical invariant of "**broken catalog never crashes the agent**" — i18n is a presentation layer and must never become an availability failure point.

## 5. Practical Usage [1]

```python
from agent.i18n import t

# Simple string
print(t("approval.choose_long"))

# With parameters
print(t("gateway.draining", count=3))
# zh.yaml:  gateway:
#             draining: "Gateway restarting in 30 seconds — {count} sessions entering drain"

# Explicitly override language
print(t("approval.choose_long", lang="zh"))
```

## 6. Relationship with Existing Systems [1]

| System | Uses i18n? |
|------|-------------|
| Approval / dangerous command prompts | **Yes** |
| Gateway slash command replies (partial) | **Yes** |
| Restart drain notifications | **Yes** |
| TUI fixed labels (e.g., "Status", "Press 'q' to quit") | TUI's own locale subset |
| Web Dashboard | Independent dashboard i18n (since v0.11.0, EN + ZH) |
| LLM system prompts | **No** (English, maintains optimal model behavior) |
| Skill descriptions | **No** (read by agent too) |
| Tool outputs | **No** |
| Errors / Logs | **No** |

---

## 7. Invariants [1]

- Catalog is always a **flat dict** + dot-separated path keys.
- Missing keys always fallback to English; missing English keys always fallback to the key string itself.
- Resolution order is fixed: `lang=` → `HERMES_LANGUAGE` → config → `"en"`.
- **Do not translate** agent-generated content; only translate what the Hermes framework says directly.
- Translation failures never crash the system.

## 8. Verification [1]

```
agent/i18n.py:1-30          docstring explicitly states "thin slice" principle + resolution order
locales/*.yaml              16 language files
website/docs/i18n/          Doc site zh-Hans translation path
```

## Related Pages

- [[Configuration And Profiles|configuration-and-profiles]]
- [[Skin Engine|skin-engine]]
---