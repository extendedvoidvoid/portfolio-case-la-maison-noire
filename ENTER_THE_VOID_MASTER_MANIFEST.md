# ENTER THE VOID (TOM KAN 2009) MASTER RECONSTRUCTION MANIFEST

**Author:** César Cabrera (Extended Void)  
**Execution Standard:** Frame-by-Frame 50-Step Milimetric Reconstruction Engine  
**System Target:** Remotion 4.0 + Local Vision Model + FFmpeg + WebGL Shaders  
**Total Frames:** 3,408 frames (142 seconds @ 23.976 fps / 60 fps Remotion timeline)

---

## LAYER ARCHITECTURE (5-LAYER SYSTEM)

```
┌─────────────────────────────────────────────────────────────┐
│ LAYER 5: Post-FX (Glow, Chromatic Aberration, Scanlines)   │
├─────────────────────────────────────────────────────────────┤
│ LAYER 4: Opt Art Wave Warp & Displacement Filter            │
├─────────────────────────────────────────────────────────────┤
│ LAYER 3: Primary Typography (Fill + Stroke/Outline)         │
├─────────────────────────────────────────────────────────────┤
│ LAYER 2: Japanese Katakana / Secondary Text Overlay          │
├─────────────────────────────────────────────────────────────┤
│ LAYER 1: Stroboscopic Background Canvas (RGB Color Lock)    │
└─────────────────────────────────────────────────────────────┘
```

---

## 50-STEP MILIMETRIC EXECUTION MANIFEST

### Phase I: Media Ingestion & Pixel-Exact Frame Extraction (Steps 1–10)
1. **Source Verification:** Confirm 1080p MKV source video metadata (`Enter the Void (2009) title sequence.mkv`).
2. **Total Frame Unpack:** Extract all 3,408 frames as uncompressed 24-bit PNGs (`frame_0001.png` to `frame_3408.png`).
3. **Audio Master Extraction:** Extract 48kHz stereo WAV audio master (`lfo_freak.wav`).
4. **BPM & Beat Transients:** Compute 132 BPM onset detection, transient peaks, and 60–120Hz FFT bass drum triggers.
5. **Disk Cache Allocation:** Allocate high-speed SSD cache folder `/Users/cesar/Documents/remotion-studio/frames_master/`.
6. **Master Database Init:** Create `data/frame_manifest_3408.json` with 3,408 frame records.
7. **Frame Integrity Audit:** Calculate per-frame SHA256 checksums to verify zero frame loss.
8. **Telecine & Interlacing Check:** Analyze 3:2 pull-down artifacts vs native progressive scan fields.
9. **Proxy Thumbnail Generation:** Build 1/4 scale thumbnails for fast vision model parsing.
10. **Phase I Integrity Lock:** Lock extraction manifest with timestamp indices.

### Phase II: Multi-Layer Isolation & Mask Generation (Steps 11–20)
11. **Layer 1 Isolation:** Extract background canvas RGB color matrix per frame.
12. **Layer 2 Isolation:** Extract primary typography fill mask via color thresholding.
13. **Layer 3 Isolation:** Extract text stroke/outline geometry via Canny edge detection.
14. **Layer 4 Isolation:** Extract AE *Shine* / *Starglow* radial vector maps.
15. **Layer 5 Isolation:** Isolate secondary Japanese Katakana background text layers.
16. **Opt Art Pattern Detection:** Classify background textures (Checkerboard, Scanlines, Concentric Circles, Stripes).
17. **Alpha Matte Extraction:** Generate RGBA transparency mattes for all text elements.
18. **Sub-Pixel Motion Tracking:** Track motion vectors (X/Y position, scale, rotation angle) between adjacent frames.
19. **1-Frame Strobe Mapping:** Identify single-frame solid color toggles (Black/Red/Yellow/White/Blue).
20. **Chromatic Aberration Vectoring:** Measure RGB channel pixel displacement distance per flash.

### Phase III: Vision OCR & Adobe Typekit Font Sandbox (Steps 21–30)
21. **Local Vision Engine Setup:** Connect local Ollama instance (`qwen2.5-vl` / `llava`) on port 11434.
22. **OCR Parsing Pass:** Execute Vision OCR across all 3,408 frames to log original text strings.
23. **Spatial Bounding Box Mapping:** Calculate exact `[x, y, width, height]` coordinates and center anchor points.
24. **Font Family Classification:** Categorize fonts into 2008 Adobe Typekit families (*Impact*, *Futura Extra Bold*, *Helvetica Black*, *Cooper Black*, *ITC Kabel*, *Eurostile*, *Katakana*).
25. **Tracking Measurement:** Calculate letter-spacing (`tracking_em`) per character pair.
26. **Leading Measurement:** Calculate line-height (`leading_px`) for stacked multi-line cards.
27. **Font Weight & Thickness:** Measure stroke weight and optical width.
28. **Web Font Sandbox Setup:** Configure dynamic CSS `@font-face` sandbox with Google Fonts & Adobe Web Fonts.
29. **Vector Glyph Fallback:** Integrate `opentype.js` / SVG path converter for custom non-standard glyphs.
30. **Font Metadata Locking:** Write typographic schema per frame to master JSON.

### Phase IV: Portfolio Keyword Mapping & Text Substitution (Steps 31–40)
31. **Portfolio Corpus Compilation:** Compile César Cabrera's 30+ portfolio credentials (*CÉSAR CABRERA*, *CANAL+*, *DÉJÀ VU*, *ABSENCE*, *PARFUMS BEAUTÉ*, *360° CAMPAIGN*, *SORBONNE*, *CANNES*, *BERLINALE*, *MOSTRA*, *MILANO*, *MADRID*, etc.).
32. **Temporal Distribution:** Distribute keywords across 3,408 frames matching Tom Kan's cut acceleration curve.
33. **Character Aspect Matching:** Scale replacement text strings to maintain original bounding box aspect ratios.
34. **Hero Placement:** Assign "CÉSAR CABRERA" to heavy Impact/Futura stroboscopic sequences (Intro and Outro).
35. **Editorial Placement:** Assign Canal+, Déjà Vu, and Absence to high-contrast mid-sequence cards.
36. **Geographic Burst Placement:** Assign Paris, Milano, Madrid, Rouen to rapid-fire 1-frame strobe cuts.
37. **Japanese Subtitle Translation:** Translate portfolio keywords into accurate Japanese Katakana for secondary layer.
38. **Automated Layout Fitting:** Execute auto-scaling algorithm to prevent text overflow.
39. **Keyword Schema Locking:** Write `data/substituted_keywords_map.json`.
40. **Safe-Zone Validation:** Verify all text bounds stay within 16:9 action-safe margins.

### Phase V: Remotion React Architecture & Shader Engine (Steps 41–45)
41. **Root Composition Setup:** Construct `<EnterTheVoidMasterSequence />` in Remotion (1920×1080 @ 60fps, 3,408 frames).
42. **Strobe Canvas Component:** Build `<StrobeBackground />` for frame-exact RGB color flashing.
43. **Kinetic Type Component:** Build `<KineticTypographyLayer />` rendering vector text, outlines, and SVG stroke filters.
44. **Opt Art Shader Component:** Build `<OptArtShaderLayer />` using WebGL/SVG filters (`feDisplacementMap`, `feTurbulence`) for wave warping.
45. **Chromatic Aberration Filter:** Build `<ChromaticFilter />` splitting RGB channels with dynamic offset vectors.

### Phase VI: Difference Optimization, Hardware Compile & Export (Steps 46–50)
46. **Candidate Still Rendering:** Render candidate test stills using `npx remotion still`.
47. **SSIM & MSE Difference Analysis:** Calculate Structural Similarity Index (SSIM) between original and rendered frames.
48. **Iterative Parameter Tuning Loop:** Execute automated gradient-descent loop adjusting font scale, stroke, and wave frequency until SSIM > 0.92.
49. **Multi-Threaded Master Render:** Render 1080p60 MP4 master video via Remotion CLI (`npx remotion render`) using Apple Videotoolbox GPU acceleration on Intel i9 / Radeon Pro 575X.
50. **Web Asset Export & Git Lock:** Export lightweight WebP/GIF hero loop for website integration, update documentation, and commit changes to Git repository.
