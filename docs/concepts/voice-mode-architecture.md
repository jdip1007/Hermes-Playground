---
title: Voice Mode Architecture
created: 2026-04-10
updated: '2026-06-08'
type: concept
tags:
- agent-system
- voice
- ai-ml
sources:
- title: Hermes-Wiki Repository
  type: web
  url: https://github.com/cclank/Hermes-Wiki
confidence: high
contested: false
---
> **v2026.5.7 additions**:
>
> - **xAI Custom Voices — Voice cloning** (@alt-glitch, #18776). Source: `tools/tts_tool.py:861` `_generate_xai_tts` + line 875 `voice_id = str(xai_config.get("voice_id", DEFAULT_XAI_VOICE_ID))`, alongside ElevenLabs / MiniMax / Mistral TTS.
> - **`video_analyze` tool** (@alt-glitch, #19301). Native video understanding on multimodal models like Gemini. Source: `tools/vision_tools.py:915` `async def video_analyze_tool`, name at line 1123, peer to line 759 `vision_analyze`.
> - **TUI voice push-to-talk parity restored** (salvage #16189, #20897).

# Voice Mode Architecture

## Overview

Hermes supports push-to-talk voice interaction: user presses key to record → STT converts to text → LLM processes → TTS speaks the reply [1]. The entire pipeline runs in the CLI, depending on optional audio libraries [1]. **v2026.5.7+ also supports video understanding** (`video_analyze`) and **voice cloning** (xAI Custom Voices) [1].

## Dependencies

```bash
pip install sounddevice numpy   # or
pip install hermes-agent[voice]
```

Audio libraries are **lazily loaded on demand** — not installing them doesn't affect text mode [1]. Automatically detected and disabled in environments without audio devices (SSH, Docker, WSL) [1].

> WSL improvement (v0.12.0, 081f936): When `sd.query_devices()` returns empty list but `PULSE_SERVER` env is set, still considers audio available (previously disabled outright, preventing WSL + PulseAudio users from using voice) [1].

## Flow

```text
User presses Ctrl+B to start recording
    ↓
sounddevice captures audio → WAV temp file
    ↓
Press Ctrl+B again to stop recording
    ↓
STT converts to text (5 providers available):
  - local: faster-whisper (local, no API key needed, default)
  - groq: Whisper via Groq (free tier)
  - openai: Whisper via OpenAI
  - mistral: Voxtral Transcribe via Mistral
  - xai: Grok STT via xAI
    ↓
Transcribed text sent as user message to LLM
    ↓
LLM responds (auto-injects concise instruction: "respond concisely, 2-3 sentences max")
    ↓
TTS voice playback (10 built-in providers + custom command provider):
  - edge（Edge TTS）
  - elevenlabs (streaming, plays as it generates)
  - openai（OpenAI TTS）
  - gemini（Google Gemini TTS）
  - xai（xAI TTS）
  - minimax（MiniMax TTS）
  - mistral（Mistral TTS）
  - neutts (self-hosted)
  - kittentts (local CPU)
  - piper (local neural TTS)
```

## STT Configuration

```yaml
# config.yaml
stt:
  provider: local   # local | groq | openai | mistral | xai
  model: base       # faster-whisper model size (base ~150MB, auto-downloads on first use)
```

When no provider is explicitly specified, auto-detects in order: `local > groq > openai > xai` (`mistral` temporarily skipped due to `mistralai` PyPI package isolation on 2026-05-12)skipped when）[1]。

```bash
# .env
GROQ_API_KEY=...              # Groq Whisper (free)
VOICE_TOOLS_OPENAI_KEY=...    # OpenAI Whisper
MISTRAL_API_KEY=...           # Mistral Voxtral Transcribe
XAI_API_KEY=...               # xAI Grok STT
```

## TTS Configuration

TTS provider selection and voice settings managed through `tools/tts_tool.py`, supporting ElevenLabs streaming playback — LLM generates a sentence, it plays immediately without waiting for the full response [1].

### TTS Provider Matrix (registry since v0.12.0)

v0.12.0 introduced `tts.providers.<name>` plugin registry (PR #17843, closes #8508) [1]. All TTS providers now register through the same ABC [1].

| Provider | Origin |
|----------|------|
| ElevenLabs | Original — streaming |
| OpenAI | Original |
| **Google Gemini TTS** | v0.10.0，Gemini API |
| **xAI TTS** | v0.10.0，xAI Responses API |
| **KittenTTS (local)** | v0.10.0+, CPU, no GPU or API key needed |
| **Piper (local)** (v0.12.0) | First native local TTS implemented via new registry (PR #17885) |
| **xAI Custom Voices** (v0.13.0) | TTS provider + **voice cloning** support (@alt-glitch, PR #18776) |
| **xAI TTS speech-tag pauses** (post-v0.14.0) | Opt-in, enables SSML-like pause tags |

These providers can also be accessed through Nous Tool Gateway (no need for your own API keys) [1].

### TTS Provider Registry + Piper (v0.12.0+)

`tools/tts_tool.py:203,349,1475-1607` introduces **pluggable TTS provider registry** (`tts.providers.<name>` config namespace), and adds **Piper** as native local TTS provider [1]:

- Fully local, no network, no API key [1]
- 5000 character output cap (`tools/tts_tool.py:203`) [1]
- Registered as builtin (`tools/tts_tool.py:349`) [1]

### xAI Custom Voices — Voice Cloning (v0.13.0+)

`tools/tts_tool.py:73,196,969-991` (`DEFAULT_XAI_VOICE_ID` at line 986): xAI Custom Voices added to TTS provider, supports **cloning any voice sample** for generation [1]. Subscribers can upload voice samples and reuse them [1].

### STT Provider Extensions (v2026.4.18+)

| Provider | Description |
|----------|------|
| `edge` | Edge TTS |
| `elevenlabs` | ElevenLabs, supports streaming playback |
| `openai` | OpenAI TTS |
| `gemini` | Google Gemini TTS (via Gemini API) |
| `xai` | xAI TTS |
| `minimax` | MiniMax TTS (default model `speech-02`, supports GroupId) |
| `mistral` | Mistral TTS |
| `neutts` | NeuTTS (self-hosted) |
| `kittentts` | KittenTTS, runs on local CPU, no GPU or API key needed, default model `KittenML/kitten-tts-nano-0.8-int8` (25MB),default voice `Jasper` |
| `piper` | **Piper (added v2026-05-15+)**, fast local neural TTS from Home Assistant project (OHF-Voice/piper1-gpl), supports 44 languages, zero API key |

Some cloud providers can also be accessed through Nous Tool Gateway (no need for your own API keys) [1].

### Piper Local TTS (v2026-05-15+)

`piper` added as native built-in provider (closes #8508 / #17885), alongside `edge`/`neutts`/`kittentts`, installable via `hermes tools` in one click [1]:

- Lazy-load import `_import_piper()` [1]
- Module-level voice cache keyed by `(model_path, use_cuda)` — switching voices doesn't invalidate old cache [1]
- `_resolve_piper_voice_path()` accepts absolute `.onnx` path or voice name (auto-downloads on first use via `python -m piper.download_voices`) [1]
- Voice cache at `~/.hermes/cache/piper-voices/` (profile-aware) [1]
- Optional `SynthesisConfig` parameters: `length_scale`, `noise_scale`, `noise_w_scale`, `volume`, `normalize_audio`, `use_cuda` [1]
- Output WAV converted via ffmpeg (same as neutts/kittentts), supports Telegram voice bubbles when ffmpeg is present [1]

### Command-Type Provider Registry (v2026-05-15+)

`tts.providers.<name>` registry (#17843) lets users connect any local/external TTS CLI without adding engine-specific Python code [1]:

```yaml
tts:
  provider: piper-en
  providers:
    piper-en:
      type: command
      command: 'piper -m ~/model.onnx -f {output_path} < {input_path}'
      output_format: wav
```

- Placeholders: `{input_path}`, `{text_path}`, `{output_path}`, `{format}`, `{voice}`, `{model}`, `{speed}`; `{{` / `}}` for literal braces [1]
- When `command:` is set, `type: command` is default [1]
- **Built-in provider names always take precedence** — entries like `tts.providers.openai` cannot shadow native built-in providers [1]

### STT Providers (5)

`tools/transcription_tools.py` provides 5 STT providers [1]:

| Provider | Description |
|----------|------|
| `local` | faster-whisper runs locally, default, no API key needed, auto-downloads model |
| `groq` | Groq Whisper API (free tier), requires `GROQ_API_KEY` |
| `openai` | OpenAI Whisper API, requires `VOICE_TOOLS_OPENAI_KEY` |
| `mistral` | Mistral Voxtral Transcribe API, requires `MISTRAL_API_KEY` (temporarily disabled due to `mistralai` package isolation on 2026-05-12)） |
| `xai` | xAI Grok STT API, requires `XAI_API_KEY`, supports ITN (Inverse Text Normalization) + optional diarization, 21 languages |

## Voice Mode Special Behaviors

- When LLM receives voice input, system automatically injects prefix instruction requesting brief reply [1]
- This prefix is only used for the API call, **not persisted to session history** (original transcription saved via `persist_user_message` parameter) [1]
- In continuous voice mode, persistent errors (like 429) automatically stop to prevent error → record → error loop [1]

## TUI Voice Mode (v2026.4.30+)

VAD loop + TTS + crash forensics all implemented in Ink-based TUI for parity (previously only classic CLI supported push-to-talk) [1]. Ctrl+B behavior under `hermes --tui` matches classic CLI [1]. Vision cache now uses `HERMES_HOME` instead of cwd (PR #17719), avoiding duplicate model downloads across different project directories [1].

## Related Pages
- [[Terminal Backends|terminal-backends]]
- [[Messaging Gateway Architecture|messaging-gateway-architecture]]

- [Cli Architecture](cli-architecture.md) — Voice mode integration in CLI
- [Auxiliary Client Architecture](auxiliary-client-architecture.md) — STT/TTS uses auxiliary model configuration

## Key Source Files

| File | Responsibility |
|------|------|
| `tools/voice_mode.py` (1018 lines) | Recording, STT scheduling, audio playback |
| `tools/tts_tool.py` (2225 lines) | TTS provider routing (10 built-in + command-type custom), streaming playback |
| `tools/transcription_tools.py` (921 lines) | Unified STT provider interface |
| `cli.py` | Push-to-talk key binding (Ctrl+B) |

## 2026-05-31 addition — Allow voice over SSH (detects PulseAudio / PipeWire socket)

`fix(voice): allow /voice over SSH when a sound server is reachable`（`d4e7b2fc1`，#35719）[1]：

**Problem**: Previously SSH sessions **hard-failed** voice mode, rejecting based solely on presence of `SSH_*` env vars [1]. But many users' workflows are:

- Host runs PulseAudio / PipeWire;
- SSH into hermes, but use X11/audio forwarding or local socket to let ffplay/aplay/pw-play go directly through host audio [1].

Voice mode should work in this setup [1].

**Fix**: After SSH detection, **continue probing** default sound-server sockets [1]:

- `PULSE_SERVER` (unix path mode)
- `PULSE_RUNTIME_PATH/native` (default PulseAudio runtime dir)
- PipeWire socket（`XDG_RUNTIME_DIR/pipewire-*`）

Any one reachable → allow voice mode; all unreachable → keep original failure (with friendly error message listing which sockets were probed) [1].
