# ENTER THE VOID (TOM KAN 2009) MASTER RECONSTRUCTION & AMPLIFICATION MANIFEST

**Author:** César Cabrera (Extended Void)  
**Execution Standard:** 50-Step Milimetric Frame-by-Frame Reconstruction  
**Primary Engine:** Remotion 4.0 (React/TypeScript + WebGL Shaders) + OpenCV + Ollama Qwen2.5-VL  
**Target Sequence:** 3,408 Frames (142s @ 23.976 fps / 60 fps Remotion Timeline)  
**Name Corpus:** 32 Custom Portfolio Keywords (César Cabrera Master Corpus)

---

## CORE LAWS OF RIGOR & TRICHER METHODOLOGY

### 1. Remotion-Native Skeleton-First Paradigm
- **Law:** We build a pure **Remotion Skeleton Component** (`<EnterTheVoidSkeleton />`) first. 
- Every layer—Background Strobe, Primary Typography, Secondary Japanese Katakana, Stroke Outline, and Post-FX Shaders—is controlled by pure React props driven by frame indices from `master_frame_db.json`.

### 2. The 5-Frame Random Morph Trick
- **Law:** Randomly sample 5 keyframes every 100 frames. Keep the original video's Opt Art background, chromatic aberration, and particle effects intact while **morphing new text ("César Cabrera" keywords) directly over the original text region** using OpenCV/Remotion alpha masks.

### 3. Quantitative Name Corpus Lock (32 Portfolio Keywords)
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

## STORYBOARD & SEQUENTIAL GOALS MAP

```
[ ACT I: INTRO STROBE ] ──────► [ ACT II: ACCELERATION ] ──────► [ ACT III: HYPER-AMPLIFICATION ]
Frames 0001 – 0400             Frames 0401 – 2400               Frames 2401 – 3408
- Hero: "CÉSAR CABRERA"        - 30 Portfolio Keywords           - Outro: "CÉSAR CABRERA"
- High-contrast Red/Black      - Rapid 1-frame cuts              - 1.8x Saturation + WebGL
- Impact / Futura Bold         - Dual-language Katakana          - Opt Art Wave Overdrive
```

---

## 50-STEP MILIMETRIC EXECUTION MANIFEST

### Phase I: Ingestion & Frame-Level Unpacking (Steps 1–8)
1. **Source Lock:** Verify source `/Users/cesar/Downloads/Enter the Void (2009) title sequence.mkv`.
2. **3,408 Frame Unpack:** Extract all 3,408 frames as uncompressed 24-bit PNGs (`frame_0001.png` to `frame_3408.png`).
3. **Audio Master Dump:** Extract 48kHz stereo WAV (`lfo_freak.wav`).
4. **Transient Peak Array:** Calculate audio RMS amplitude array per frame for 132 BPM beat sync.
5. **Database Init:** Initialize `master_frame_db.json` with 3,408 entry stubs.
6. **Frame Integrity Check:** Compute per-frame SHA-256 hashes to guarantee zero dropped frames.
7. **Telecine Normalization:** Detect 3:2 pulldown fields and normalize to progressive 60 FPS.
8. **Proxy Downsampling:** Generate 1/4 scale PNG thumbnails (`frames_proxy/`) for high-speed Vision model throughput.

### Phase II: Multi-Layer Vision Deconstruction (Steps 9–17)
9. **Layer 1 Background Sampling:** Measure dominant background RGB color matrix per frame.
10. **Canny Edge Detection:** Isolate typography outer stroke geometry vs fill regions.
11. **Bounding Box Isolation:** Detect exact text bounding coordinates `[x, y, w, h]` via OpenCV contour detection.
12. **Rotation Angle Vectoring:** Measure text rotation angle $\theta$ (-30° to +30°).
13. **Japanese Layer Detection:** Identify secondary Katakana/Kanji overlay presence.
14. **Tracking Measurement:** Measure horizontal character spacing (`tracking_em`) via pixel projection profiles.
15. **Leading Measurement:** Measure vertical line-height (`leading_px`) on stacked cards.
16. **Opt Art Texture Classification:** Detect background pattern type (stripes, checkerboard, concentric, solid).
17. **Chromatic Displacement Vectors:** Measure red/blue RGB channel split offset in pixels.

### Phase III: OCR & Adobe Typekit Font Sandbox (Steps 18–24)
18. **Vision OCR Pass:** Execute local Vision OCR (`qwen2.5-vl` via Ollama) on proxy frames.
19. **String & Boundary Logging:** Write original text strings to `ocr_raw_manifest.json`.
20. **2008 Adobe Taxonomy Matching:** Classify letterforms into Adobe Typekit families (*Impact*, *Futura ExtraBold*, *Helvetica Black*, *Cooper Black*, *ITC Kabel*, *Eurostile*, *Katakana*).
21. **Font Sandbox Assembly:** Build CSS `@font-face` sandbox with dynamic Google Fonts & Adobe Web Font embeds inside Remotion.
22. **Stroke Ratio Mapping:** Calculate `-webkit-text-stroke` pixel width relative to font size.
23. **Blend Mode Mapping:** Log layer CSS composite modes (`difference`, `overlay`, `screen`, `color-dodge`).
24. **Deconstruction Lock:** Save full parameters to `tom_kan_deconstructed.json`.

### Phase IV: Portfolio Keyword Mapping & Text Morphing (Steps 25–30)
25. **Corpus Compilation:** Lock César Cabrera's 32 portfolio keywords into master map.
26. **Acceleration Mapping:** Distribute 32 keywords across 3,408 frames matching Tom Kan's cut-rate curve.
27. **5-Frame Random Morph Trick:** Execute 5-frame random sampling morphing substitute text over original background FX.
28. **Katakana Layer Translation:** Translate portfolio keywords to Japanese Katakana for Layer 2 background text.
29. **Font Scale Calculation:** Compute scale multiplier $S = \frac{\text{target\_width}}{\text{text\_width}}$.
30. **Safe-Zone Enforcement:** Pad text coordinates to respect 16:9 action-safe margins.

### Phase V: Remotion Skeleton & Difference Optimization (Steps 31–40)
31. **Remotion Composition Setup:** Construct `<EnterTheVoidSkeleton />` in Remotion studio.
32. **Prop Parameter Injection:** Pass initial $X, Y, S, \theta$ props directly to Remotion component.
33. **Remotion Still Render:** Call `npx remotion still --frame=N` for keyframe evaluation.
34. **SSIM & MSE Computation:** Compute Structural Similarity Index ($\text{SSIM}$) and Mean Squared Error ($\text{MSE}$).
35. **Error Delta Evaluation:** Compute error metric $\Delta E = 1.0 - \text{SSIM}$.
36. **Branch Check:** If $\Delta E \le 0.08$, lock frame parameters and proceed to next keyframe.
37. **Remotion Parameter Tuning:** If $\Delta E > 0.08$, adjust stroke width or tracking via Remotion prop gradient step.
38. **Re-evaluate Candidate:** Re-compute SSIM on adjusted Remotion render.
39. **Loop Convergence Cap:** Repeat steps 33–38 (max 5 iterations) until $\Delta E \le 0.08$.
40. **Master Blueprint Lock:** Save converged JSON array to `converged_state.json`.

### Phase VI: Amplification Engine ("More Violent, More Saturated, More Animated") (Steps 41–46)
41. **Hyper-Saturation Boost:** Multiply RGB saturation matrix by $1.8\times$ in WebGL shader (`saturate(1.8)`).
42. **Violent Strobe Injection:** Inject 60Hz 1-frame sub-strobe color toggles (`#FF0000` / `#000000` / `#FFFF00` / `#0000FF`) synced to audio drum transients.
43. **Chromatic Blowout:** Expand RGB channel displacement from 2px to 8px on sub-bass drops (`filter: drop-shadow(-8px 0 red) drop-shadow(8px 0 blue)`).
44. **Opt Art Wave Overdrive:** Apply dynamic SVG `feDisplacementMap` oscillating scale from 0 to 45 via sine wave LFO.
45. **CRT Phosphor & Particle Glitch:** Layer VHS scanline grid and noise particle overlays on high-transient frames.
46. **Kinetic Scale Pop:** Apply $1.25\times$ typographic spring bounce on kick drum beats.

### Phase VII: Hardware Compile & Deployment (Steps 47–50)
47. **Multi-Threaded Hardware Render Pass:** Execute Remotion CLI render (`npx remotion render`) reading `converged_state.json` across 16 CPU/GPU threads with Apple Videotoolbox acceleration.
48. **Audio Muxing:** Combine 48kHz audio `lfo_freak.wav` with rendered video into 1080p60 MP4 master.
49. **Hero WebP/GIF Loop Conversion:** Generate lightweight loop for portfolio header banner.
50. **Git Deployment:** Commit all blueprints, scripts, and rendered assets to `feat/timeline` branch.
