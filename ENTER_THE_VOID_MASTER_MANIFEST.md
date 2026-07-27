# ENTER THE VOID (TOM KAN 2009) MASTER RECONSTRUCTION MANIFEST

**Author:** César Cabrera (Extended Void)  
**Execution Standard:** Frame-by-Frame Sub-Millimeter Reconstruction Engine  
**System Target:** Remotion 4.0 + Local Vision Model + FFmpeg + WebGL Shaders  
**Total Frames:** 3,408 frames (142 seconds @ 23.976 fps)

---

## SECTION 1: EVERY SINGLE FRAME EXTRACTION (3,408 FRAMES)
- **Rule 1.1:** Do NOT extract scene cuts only. Extract **EVERY SINGLE FRAME INDIVIDUALLY** (`frame_0001.png` to `frame_3408.png`).
- **Rule 1.2:** Native resolution: 1920×1080 PNG 24-bit RGB.
- **Rule 1.3:** Directory: `/Users/cesar/Documents/remotion-studio/frames_master/`.

---

## SECTION 2: CHUNK & MODULE LAYER SEGREGATION
Every title card sequence broken into 4 distinct functional modules/layers:

```
┌─────────────────────────────────────────────────────────────┐
│ LAYER 4: Post-FX (Glow, Chromatic Aberration, Scanlines)   │
├─────────────────────────────────────────────────────────────┤
│ LAYER 3: Opt Art Distortion & Wave Warp Field               │
├─────────────────────────────────────────────────────────────┤
│ LAYER 2: Typography Fill & Outline Stroke (CSS / SVG)       │
├─────────────────────────────────────────────────────────────┤
│ LAYER 1: Stroboscopic Background Canvas (RGB Color Lock)    │
└─────────────────────────────────────────────────────────────┘
```

- **Module A: Background Canvas:** Hex color lock per frame (`#FF0000`, `#000000`, `#FFFF00`, `#FFFFFF`, `#0000FF`).
- **Module B: Core Typography:** Vector font, kerning, tracking, scale, rotation, positioning.
- **Module C: Outline Stroke:** Outer/inner border pixel width (`-webkit-text-stroke`).
- **Module D: Distortion Engine:** SVG `feDisplacementMap`, `feTurbulence`, AE *Shine* radial blur, AE *Wave Warp*.

---

## SECTION 3: FONT SANDBOX & WEB TYPOGRAPHY INJECTION
- **Rule 3.1:** ZERO installation of 300 system fonts.
- **Rule 3.2:** Font Sandbox via dynamic CSS `@font-face` injection & Google Fonts / Adobe Web Fonts API.
- **Core 2008 Typography Mappings:**
  1. *Impact* / *Arial Black* (Heavy Grotesque Block)
  2. *Futura Extra Bold* / *Helvetica Ultra Compressed*
  3. *Cooper Black* / *ITC Kabel* (Vintage Display)
  4. *Eurostile Bold* / *Bank Gothic* (Geometric Tech)
  5. *Shin Serif* / *DynaComware Katakana* (Japanese Stencil Overlay)

---

## SECTION 4: 25-STEP MILIMETRIC EXECUTION MANIFEST

### Phase I — Frame-by-Frame Extraction (Steps 1–5)
1. Execute total frame extraction pass: `ffmpeg -i input.mkv -vsync 0 frames_master/frame_%04d.png`.
2. Extract 48kHz WAV audio master (`lfo_freak_audio.wav`).
3. Compute audio RMS amplitude array per frame for 132 BPM beat-sync alignment.
4. Generate frame index manifest `data/frame_master_index.json` (3,408 array items).
5. Verify zero missing or dropped frames in disk cache.

### Phase II — Frame-by-Frame Vision & OCR Audit (Steps 6–10)
6. Run local Vision OCR (`qwen2.5-vl` via Ollama) on every frame.
7. Record text bounding boxes `[x, y, w, h]` and text orientation angle.
8. Classify font family category per frame (Impact / Futura / Helvetica / Cooper / Japanese).
9. Measure letter-spacing (`tracking_em`) and line height (`leading_px`).
10. Identify fill mode: Solid White, Solid Yellow, Outline Only, Inverted Mask.

### Phase III — Color Matrix & Strobe Mapping (Steps 11–15)
11. Sample dominant background RGB per frame using PIL ImageStat.
12. Detect strobe frequency (e.g., 1-frame flash vs. 2-frame hold).
13. Calculate chromatic aberration offset in pixels (`red_shift_x`, `blue_shift_x`).
14. Detect Opt Art background pattern (Stripes, Checkerboard, Radial Lines).
15. Measure AE *Shine* / *Starglow* vector direction and decay opacity.

### Phase IV — Automated Matching & Difference Loop (Steps 16–20)
16. Substitute credit strings with César Cabrera's 30 portfolio keywords.
17. Render candidate frame via Remotion headless Chrome renderer.
18. Compute pixel-level Structural Similarity (SSIM) between original and rendered frame.
19. Auto-tune typography font size, scale, and stroke width via gradient descent loop.
20. Lock frame parameters into `data/enter_the_void_locked_blueprint.json`.

### Phase V — Remotion Engine & Final Master Render (Steps 21–25)
21. Build Remotion composition `<EnterTheVoidMasterSequence />` using locked JSON blueprint.
22. Attach SVG WebGL shader filters for wave distortion and scanline grain.
23. Synchronize `useCurrentFrame()` with `lfo_freak_audio.wav` waveform peak triggers.
24. Multi-threaded hardware render (16 threads) to 1080p60 MP4 master.
25. Generate web-optimized WebP / GIF hero banner for portfolio website.
