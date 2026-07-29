# ENTER THE VOID (TOM KAN 2009) MASTER RECONSTRUCTION & AMPLIFICATION MANIFEST
**Current Version:** 0.1 Forensic Reconstruction Engine  
**Author:** César Cabrera (Extended Void)  
**Execution Standard:** 50-Step Milimetric Frame-by-Frame Reconstruction + 30,000V Kirlian Analysis + Modular 5s Incremental Engine  
**Primary Engine:** Remotion 4.0 (Modular React Compositions + WebGL SVG Shaders) + OpenCV + Pillow  
**Target Sequence:** 3,408 Frames (142s @ 23.976 fps / 60 fps Remotion Timeline)  
**Chunk Size:** 5-Second Incremental Modules (28 Total 5s Chunks)  
**Forensic Manual Reference:** `data/ENTER_THE_VOID_FORENSIC_DECONSTRUCTION_35MM.md`  
**Name Corpus:** 32 Custom Portfolio Keywords (César Cabrera Master Corpus)

---

## CANONICAL WORKFLOW LAW: STORYBOARD FIRST, PRODUCTION SECOND

```
┌────────────────────────────────────────────────────────────────────────┐
│                   STRICT 5-SECOND MODULAR WORKFLOW                     │
│                                                                        │
│ 1. Select 5s Chunk (e.g., 0–5s) ──► 2. Generate Storyboard Contact Sheet│
│                                                   │                    │
│                                                   ▼                    │
│ 4. Render 5s Remotion Module ◄── 3. HUMAN APPROVAL GATE?               │
│               │                         │ (Approved)                   │
│               ▼                         └──► (If rejected: Adjust)     │
│ 5. Validate & Lock Module ──► Proceed to Next 5s Chunk (5–10s)         │
└────────────────────────────────────────────────────────────────────────┘
```

**Rule 0.1 (Human Approval Gate):** No video module rendering proceeds without explicit human approval of the 5-second storyboard contact sheet.

---

## REMOTION MODULAR ARCHITECTURE (28 CHUNKS OF 5 SECONDS)

Each 5-second interval is built as an independent, isolated React module in Remotion:

```tsx
// src/chunks/Chunk_01_00_05.tsx  -> Frames 0000 - 0120
// src/chunks/Chunk_02_05_10.tsx  -> Frames 0121 - 0240
// src/chunks/Chunk_03_10_15.tsx  -> Frames 0241 - 0360
// ... up to Chunk_28 (135–142s)
```

Each module encapsulates:
1. `<BackgroundStrobe />`: Hex color lock per frame.
2. `<PrimaryType />`: Vector font fill, tracking, rotation angle.
3. `<StrokeLayer />`: Outer stroke width & color.
4. `<SecondaryTypeKatakana />`: Translated Japanese text layer.
5. `<ShaderEffects />`: Opt Art displacement map + chromatic aberration.

---

## 32-NAME PORTFOLIO CORPUS

```json
[
  "CÉSAR CABRERA", "CANAL+", "DÉJÀ VU", "ABSENCE", "PARFUMS BEAUTÉ",
  "360° CAMPAIGN", "NARRATION VISUELLE", "STORYTELLING", "DIRECTION ARTISTIQUE",
  "CONCEPTEUR-RÉDACTEUR", "SÉRIES ENTRE POTES", "LA SCÈNE", "FESTIVAL DE CANNES",
  "BERLINALE", "MOSTRA DE VENISE", "DEAUVILLE", "CÉRÉMONIE DES CÉSAR",
  "ROBERT REDFORD", "ÉCOLE DES GOBELINS", "LA SORBONNE", "FLAUBERT", "KAFKA",
  "STEFAN ZWEIG", "EXTENDED VOID", "PARIS", "MILANO", "MADRID", "ROUEN",
  "NEUILLY-SUR-SEINE", "MODUL9", "CRAFTCUT", "CÉSAR CABRERA"
]
```

---

## 50-STEP MILIMETRIC EXECUTION MANIFEST

### Phase I: Source Unpacking & Chunk Partitioning (Steps 1–8)
1. **Source Lock:** Verify source `/Users/cesar/Downloads/Enter the Void (2009) title sequence.mkv`.
2. **3,408 Frame Unpack:** Extract all 3,408 frames as 24-bit PNGs (`frame_0001.png` to `frame_3408.png`).
3. **Audio Master Dump:** Extract 48kHz stereo WAV (`lfo_freak.wav`).
4. **Transient Peak Array:** Calculate audio RMS amplitude array per frame for 132 BPM beat sync.
5. **5s Chunk Splitter:** Partition 3,408 frames into 28 sub-directories of 120 frames each (`chunk_01/` to `chunk_28/`).
6. **Master Database Init:** Initialize `data/master_frame_db.json` structured by 28 chunks.
7. **Frame Integrity Audit:** Calculate SHA-256 hashes per frame for zero frame loss.
8. **Proxy Downsampling:** Generate 1/4 scale thumbnails (`frames_proxy/`) for fast Vision model pass.

### Phase II: Vision Deconstruction & Layer Separation (Steps 9–17)
9. **Layer 1 Background Sampling:** Sample dominant background RGB color per frame.
10. **Layer 2 Canny Edge Isolation:** Extract outer text stroke geometry vs fill regions.
11. **Bounding Box Calculation:** Extract exact `[x, y, w, h]` text bounding boxes via OpenCV.
12. **Rotation Angle Vectoring:** Measure text tilt angle $\theta$ (-30° to +30°).
13. **Katakana Layer Identification:** Detect secondary Japanese text overlay presence.
14. **Tracking Measurement:** Calculate letter-spacing (`tracking_em`) per character pair.
15. **Leading Measurement:** Calculate line-height (`leading_px`) for stacked multi-line cards.
16. **Opt Art Pattern Tagging:** Classify background textures (stripes, checkerboard, concentric).
17. **Chromatic Displacement Vectors:** Measure RGB split offset in pixels.

### Phase III: OCR & Adobe Typekit Font Sandbox (Steps 18–24)
18. **Vision OCR Pass:** Execute local Vision OCR (`qwen2.5-vl` via Ollama) on proxy frames.
19. **String & Boundary Logging:** Save raw OCR strings to `ocr_raw_manifest.json`.
20. **2008 Adobe Taxonomy Matching:** Map fonts to Adobe Typekit families (*Impact*, *Futura ExtraBold*, *Helvetica Black*, *Cooper Black*, *ITC Kabel*, *Eurostile*, *Katakana*).
21. **Font Sandbox Assembly:** Build CSS `@font-face` sandbox in Remotion with Google Fonts & Adobe Web Fonts.
22. **Stroke Ratio Mapping:** Calculate `-webkit-text-stroke` width relative to font size.
23. **Blend Mode Mapping:** Log composite blend modes (`difference`, `overlay`, `screen`, `color-dodge`).
24. **Deconstruction Lock:** Write complete parameters to `tom_kan_deconstructed.json`.

### Phase IV: Storyboard Generation & Human Approval Gate (Steps 25–30)
25. **Portfolio Keyword Mapping:** Assign 32 portfolio keywords across 28 chunks.
26. **5-Frame Random Morph Trick:** Execute 5-frame random sampling morphing text over original background FX.
27. **Katakana Subtitle Translation:** Translate keywords to Japanese Katakana for Layer 2.
28. **Storyboard Contact Sheet Generator:** Render 12-frame grid contact sheet PNG for current 5s chunk (`storyboard_chunk_01.png`).
29. **HUMAN APPROVAL GATE:** Present contact sheet to human. Pause execution until human issues `approved` or `adjust`.
30. **Storyboard Locking:** Lock approved storyboard layout into `storyboard_approved_manifest.json`.

### Phase V: Remotion Module Development & Iterative Optimization (Steps 31–40)
31. **Module Scaffolding:** Create Remotion component `src/chunks/Chunk_XX.tsx` for approved chunk.
32. **Prop Parameter Injection:** Inject $X, Y, S, \theta$, colors, and font styles into React props.
33. **Remotion Still Render:** Call `npx remotion still --frame=N` for chunk keyframes.
34. **SSIM & MSE Computation:** Compute SSIM and MSE between original and Remotion render.
35. **Error Delta Evaluation:** Compute error metric $\Delta E = 1.0 - \text{SSIM}$.
36. **Branch Check:** If $\Delta E \le 0.08$, lock chunk parameters and proceed.
37. **Remotion Parameter Tuning:** If $\Delta E > 0.08$, adjust stroke width, tracking, or scale via Remotion prop gradient step.
38. **Re-evaluate Candidate:** Re-compute SSIM on adjusted Remotion render.
39. **Loop Convergence Cap:** Repeat steps 33–38 (max 5 iterations per keyframe) until $\Delta E \le 0.08$.
40. **Module Lock:** Save converged state to `converged_chunk_XX.json`.

### Phase VI: Amplification Engine ("More Violent, More Saturated, More Animated") (Steps 41–46)
41. **Hyper-Saturation Boost:** Multiply RGB saturation matrix by $1.8\times$ in WebGL shader (`saturate(1.8)`).
42. **Violent Strobe Injection:** Inject 60Hz 1-frame sub-strobe color toggles (`#FF0000` / `#000000` / `#FFFF00` / `#0000FF`) synced to audio drum transients.
43. **Chromatic Blowout:** Expand RGB channel displacement from 2px to 8px on sub-bass drops (`filter: drop-shadow(-8px 0 red) drop-shadow(8px 0 blue)`).
44. **Opt Art Wave Overdrive:** Apply dynamic SVG `feDisplacementMap` oscillating scale from 0 to 45 via sine wave LFO.
45. **CRT Phosphor & Particle Glitch:** Layer VHS scanline grid and noise particle overlays on high-transient frames.
46. **Kinetic Scale Pop:** Apply $1.25\times$ typographic spring bounce on kick drum beats.

### Phase VII: Master Assembly, Hardware Compile & Deployment (Steps 47–50)
47. **Root Master Assembly:** Combine all 28 validated 5s React modules into `<EnterTheVoidMasterSequence />`.
48. **Multi-Threaded Master Render:** Execute Remotion CLI render (`npx remotion render`) across 16 CPU/GPU threads with Apple Videotoolbox acceleration.
49. **Audio Muxing:** Combine 48kHz audio `lfo_freak.wav` with rendered video into 1080p60 MP4 master.
50. **Web Asset Export & Git Lock:** Export lightweight WebP/GIF hero loop for portfolio header banner, update documentation, and commit changes to Git repository.
