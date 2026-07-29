import os
import json
import cv2
import numpy as np

PROJECT_DIR = "/Users/cesar/Documents/Default Project/portfolio-case-la-maison-noire"
EXTRACT_DIR = "/tmp/etv_orig_0_20s_frames"
OUTPUT_JSON = os.path.join(PROJECT_DIR, "data/orig_0_20s_frame_by_frame_manifest.json")

def analyze_extracted_frames():
    fps = 24.0
    max_frames = 480
    
    frame_data = []
    cuts = []
    prev_gray = None
    
    for i in range(1, max_frames + 1):
        frame_path = os.path.join(EXTRACT_DIR, f"frame_{i:04d}.png")
        if not os.path.exists(frame_path):
            break
            
        frame = cv2.imread(frame_path)
        frame_idx = i - 1
        time_sec = frame_idx / fps
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        small = cv2.resize(frame, (100, 100))
        
        # Dominant RGB
        avg_bgr = [int(x) for x in np.mean(small, axis=(0, 1))]
        avg_rgb = [avg_bgr[2], avg_bgr[1], avg_bgr[0]]
        
        is_cut = False
        if prev_gray is not None:
            diff = np.mean(cv2.absdiff(gray, prev_gray))
            if diff > 20.0:
                is_cut = True
        else:
            is_cut = True
            
        if is_cut:
            cuts.append(frame_idx)
            
        prev_gray = gray.copy()
        
        # Bounding Box using Canny
        edges = cv2.Canny(gray, 100, 200)
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        bbox = [0, 0, 0, 0]
        area = 0
        if contours:
            c = max(contours, key=cv2.contourArea)
            area = int(cv2.contourArea(c))
            bbox = [int(v) for v in cv2.boundingRect(c)]
            
        frame_info = {
            "frame": frame_idx,
            "time_sec": round(time_sec, 3),
            "is_cut": is_cut,
            "avg_rgb": avg_rgb,
            "text_area": area,
            "bounding_box": bbox,
        }
        frame_data.append(frame_info)
        
    # Group into shots
    shots = []
    for idx, c in enumerate(cuts):
        start_f = c
        end_f = cuts[idx + 1] - 1 if idx + 1 < len(cuts) else len(frame_data) - 1
        duration_frames = end_f - start_f + 1
        duration_ms = round((duration_frames / fps) * 1000, 1)
        
        shots.append({
            "shot_id": idx + 1,
            "start_frame": start_f,
            "end_frame": end_f,
            "duration_frames": duration_frames,
            "duration_ms": duration_ms,
            "start_time_sec": round(start_f / fps, 3),
            "end_time_sec": round(end_f / fps, 3),
            "avg_rgb": frame_data[start_f]["avg_rgb"]
        })
        
    manifest = {
        "total_frames_analyzed": len(frame_data),
        "fps": fps,
        "total_cuts_detected": len(cuts),
        "mean_shot_duration_frames": round(float(np.mean([s["duration_frames"] for s in shots])), 2),
        "shots": shots,
        "frame_by_frame": frame_data
    }
    
    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
    with open(OUTPUT_JSON, "w") as f:
        json.dump(manifest, f, indent=2)
        
    print(f"Analyzed {len(frame_data)} frames.")
    print(f"Detected {len(cuts)} shot cuts in 20 seconds!")
    print(f"Mean shot duration: {manifest['mean_shot_duration_frames']} frames ({round((manifest['mean_shot_duration_frames']/fps)*1000, 1)}ms)")
    print(f"Manifest written to: {OUTPUT_JSON}")

if __name__ == "__main__":
    analyze_extracted_frames()
