# ENTER THE VOID (Tom Kan) KINETIC TYPOGRAPHY RECONSTRUCTION PLAN

**Target Output:** Interactive 60fps Remotion / Canvas / WebGL / GIF Hero Header featuring César Cabrera's portfolio keywords.

---

## 1. System Hardware Audit (Verified)
- **CPU:** Intel Core i9-9900K (8 Cores / 16 Threads @ 3.6 GHz)
- **RAM:** 64 GB DDR4 (Massive memory for parallel frame caching & vision analysis)
- **GPU:** AMD Radeon Pro 575X (4 GB VRAM) with Videotoolbox Hardware Acceleration
- **Tools Available:** FFmpeg 7.1.1, Remotion 4.0, Deno 2.9, Node 24, Python 3.12 + Pillow / OpenCV

---

## 2. 4-Stage Reconstruction Pipeline

### Stage 1: Temporal Cut Detection & Keyframe Mining (Zero-Cost Local FFmpeg)
- Run FFmpeg scene change detection (`select='gt(scene,0.2)'`) on `/Users/cesar/Downloads/Enter the Void (2009) title sequence.mkv`.
- Export precise timestamp manifest (`cuts_manifest.json`) recording exact millisecond intervals for all 150+ rapid typography flashes.
- Extract individual title cards at native resolution (1080p).

### Stage 2: Typographic & Color Extraction (Gemini 2.5 Flash / Local Vision)
- Process extracted frames to identify:
  1. Font family classification (Impact, Helvetica Black, Futura Bold, Japanese Katakana, Custom Neon Outlines).
  2. Text placement, rotation angle (0°, 90°, 45° tilt), tracking (letter spacing), and scale factor.
  3. Color Palette: Foreground fill color, stroke outline color, background flash color.
  4. Stroboscopic frequency (number of flash frames per second).

### Stage 3: Remotion React Architecture (`<EnterTheVoidHeader />`)
- Build modular Remotion composition:
  - `<StrobeCanvas />`: High-speed background color flasher (Red, Black, Yellow, White, Neon Blue).
  - `<KineticTitle />`: Layered SVG/CSS text component with:
    - Layer A: Solid font fill (`color`, `font-weight`, `letter-spacing`).
    - Layer B: High-contrast outline stroke (`-webkit-text-stroke`, `filter: drop-shadow`).
    - Layer C: Opt Art distortion & chromatic aberration (`feDisplacementMap`, `feTurbulence`).
- Substitute original movie credits with César Cabrera's portfolio keywords:
  - *Start:* **CÉSAR CABRERA** (Giant Red/Black Strobe)
  - *Acceleration (Rapid Flash):* CANAL+ · DÉJÀ VU · ABSENCE · PARFUMS BEAUTÉ · 360° CAMPAIGN · SCRIPT · SCÉNARIO · STORYBOARD · GOBELINS · SORBONNE · FLAUBERT · CANNES · BERLINALE · MOSTRA · PARIS · MILANO · MADRID
  - *Finish:* **CÉSAR CABRERA** (Sustained Opt Art Strobe)

### Stage 4: Local Render & Web Embedding
- Render locally via Remotion CLI (`npx remotion render`) on 16 threads.
- Export formats:
  - High-res 60fps MP4 with LFO audio beat sync for full-screen view.
  - Lightweight WebP / GIF loop for instant portfolio hero header loading.

---

## 3. Recommended Master Prompt for Gemini 2.5 Vision Analysis

```markdown
Role: Elite Motion Graphics Analyst & Typographic Engineer specializing in Tom Kan's "Enter the Void" (2009) title sequence.

Task: Analyze the attached sequence of keyframes extracted from the title card cut at timestamp [TIMESTAMP].

Output JSON format strictly:
{
  "frame_id": "[FRAME_ID]",
  "timestamp_ms": [MILLISECONDS],
  "typography": {
    "font_style_closest": "Impact | Futura Bold | Helvetica Black | Custom Katakana",
    "case": "UPPERCASE",
    "color_fill": "#RGB",
    "color_stroke": "#RGB",
    "stroke_width_px": [PIXELS],
    "letter_spacing_em": [FLOAT],
    "scale_percent": [PERCENTAGE],
    "rotation_deg": [DEGREES]
  },
  "background": {
    "color_hex": "#RGB",
    "strobe_intensity": "high | medium | low",
    "flash_frequency_hz": [HERTZ]
  },
  "effects": {
    "chromatic_aberration": boolean,
    "glow_blur_px": [PIXELS],
    "opt_art_pattern": "none | stripes | checkerboard | diagonal_lines"
  }
}
```
