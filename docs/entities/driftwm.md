---
title: "DriftWM — Infinite Canvas Wayland Compositor"
created: 2026-06-07
updated: 2026-06-07
type: entity
tags: [ai-ml, agent-system]
sources:
  - type: web
    url: "https://github.com/malbiruk/driftwm"
    title: "driftwm — GitHub Repository"
    date: 2026-06-07
  - type: web
    url: "https://codeberg.org/malbiruk/driftwm"
    title: "driftwm — Codeberg Mirror"
    date: 2026-06-07
confidence: high
contested: false
---

# DriftWM

**DriftWM** is a trackpad-first infinite canvas Wayland compositor written in Rust. Instead of arranging windows to fit the screen (like stacking or tiling WMs), it places windows at their native size on an unbounded 2D plane, and the display acts as a camera viewing that canvas. Navigation happens via pan, zoom, and pinch gestures — no workspaces, no tiling.

## Core Concept

Traditional window managers constrain windows to screen boundaries. DriftWM inverts this: the screen is a viewport onto an infinite canvas. Each window has absolute `(x, y)` coordinates on the canvas. The viewport maintains a camera position `(cx, cy)` and zoom level `z`. Screen position for any window = `(wx - cx) * z`. Multiple monitors become independent viewports sharing the same canvas [1].

## Architecture

Built on [[smithay]] (Rust Wayland compositor framework). Uses Rust edition 2024, requires Rust 1.88+ [1].

### Camera/Viewport Model

The screen is a viewport onto an infinite 2D plane. Multiple monitors = multiple independent viewports on the same canvas. Cursor crosses between monitors freely; dragged windows teleport to the target viewport's canvas position [1].

### Source Structure (92 Rust files, 19 GLSL shaders)

- `backend/` — Winit (nested) and Udev/DRM (bare metal) backends
- `state/` — DriftWm struct, camera animations, navigation, fullscreen, focus management
- `config/` — TOML config parsing with context-aware bindings (key/mouse/gesture per context: on-window/on-canvas/anywhere)
- `canvas.rs` — Coordinate transforms, camera math, cone search for directional window navigation
- `render/` — Frame composition, blur pipeline, gigapixel wallpaper support via pyramidal-TIFF LOD chunks
- `shaders/` — GLSL fragment shaders (dot_grid, shadow, blur_down/up/mask, corner_clip, border)
- `layout/` — Magnetic snap during drag, BFS cluster detection over snap-adjacency graph, auto-placement adjacent to focused window's cluster
- `input/` — Keyboard, pointer, gesture state machine (swipe/pinch/hold), libinput device config
- `grabs/` — MoveSurfaceGrab, ResizeSurfaceGrab, PanGrab, NavigateGrab
- `handlers/` — XDG shell, layer shell, compositor commit, background effects

### Key Dependencies [1]

- smithay (git rev 5312d5c) — Wayland protocol implementation, backend, renderer
- libdisplay-info — VESA CVT modeline synthesis
- cosmic-text — CPU-side text shaping for SSD title bars
- image/tiff — PNG/JPEG/pyramidal TIFF wallpaper support

## Features

### Pan & Zoom [1]

Infinite 2D canvas with scroll momentum. Quick flick carries viewport smoothly until friction stops it.

| Input | Action | Context |
|---|---|---|
| 3-finger swipe | Pan viewport | anywhere |
| Trackpad scroll | Pan viewport | on-canvas |
| Mod + LMB drag | Pan viewport | anywhere |
| 2/3-finger pinch | Zoom | on-canvas / anywhere |
| Mod + scroll | Zoom at cursor | anywhere |

### Window Navigation [1]

Cone search finds nearest window in any direction. MRU cycling (Alt-Tab) with hold-to-commit. Configurable anchors act as navigation targets even with no window present — useful for pinned widget areas.

| Input | Action |
|---|---|
| 4-finger swipe | Jump to nearest window (natural direction) |
| Mod + arrow | Jump in direction |
| Alt-Tab / Alt-Shift-Tab | MRU cycle |
| 4-finger pinch in / Mod+W | Zoom-to-fit (overview) |
| 4-finger pinch out / Mod+A | Home toggle (origin and back) |
| Mod+1-4 | Jump to bookmarked canvas position |

### Snapping & Clusters [1]

Windows snap together during drag. Snapped windows form a cluster — neighbors stay visible at view edges for spatial context. Shift + any move/resize/fit action acts on the whole cluster. No explicit grouping needed.

Fit-window (Mod+M) is the maximize analogue: centers viewport, resets zoom to 1.0, resizes window to fill screen. Fullscreen (Mod+F) is a viewport mode, not a window state — any canvas action naturally exits it.

### Infinite Background [1]

Background scrolls and zooms with the viewport, providing spatial awareness during pan. Three modes:

- **shader** — Procedural GLSL, animated or static, optionally sampling an image texture. Default is dot grid. GPU cost depends on uniforms read (none = render once; u_camera/u_zoom = redraw on pan/zoom; u_time = every frame)
- **tile** — PNG/JPG tiled infinitely, or pyramidal TIFF for gigapixel wallpapers with LOD chunk decode/upload
- **wallpaper** — Single image stretched to fill viewport (does not scroll/zoom)

### Window Rules [1]

Match by `app_id` and/or `title` (glob patterns). Control position, size, decorations, blur, opacity, pass-through keys. Widget mode pins windows immovable at canvas positions, below normal windows, excluded from Alt-Tab — useful for clocks, system stats, trays.

### IPC [1]

Unix domain socket with line-delimited JSON protocol. `driftwm msg` subcommand provides: camera position/zoom read/write, focus by app_id, window move, action dispatch (any config keybind), canvas/DPI screenshots at arbitrary resolution, full state dump. Scriptable from any language.

### Multi-Monitor [1]

Independent viewports on same canvas. Outline shows where other monitors' viewports are. Mod+Alt+arrow sends window to adjacent output.

## Configuration

TOML config at `~/.config/driftwm/config.toml` (respects XDG_CONFIG_HOME). Partial configs merge with built-in defaults — only specify what you want to change. Use `"none"` to unbind defaults. Validate without starting: `driftwm --check-config`. Config hot-reload keeps old config on bad edits and never crashes [1].

## Build & Install

- **Arch Linux (AUR):** `yay -S driftwm` or `yay -S driftwm-git`
- **NixOS:** Included flake.nix, build with `nix build`
- **Source:** Requires Rust 1.88+, libseat-devel, libdisplay-info-devel, libinput-devel, mesa-libgbm-devel [1]

## Ecosystem

### Example Setup (extras/) [1]

Complete setup including driftwm config, GLSL shader wallpapers, Python widgets (clock, calendar, system stats, power menu), waybar with taskbar/tray, fuzzel window-search script.

### Community Tools [1]

- driftwm-settings — GTK4 GUI config editor
- driftwm-noctalia — noctalia shell fork adapted for driftwm

## References

[1] malbiruk/driftwm GitHub repository (https://github.com/malbiruk/driftwm), v0.9.0, accessed 2026-06-07. Author: Klim Kostiuk. License: GPL-3.0-or-later. Primary reference for all technical details above.
