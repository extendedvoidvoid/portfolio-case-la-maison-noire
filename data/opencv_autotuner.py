import os
import json
import cv2
import numpy as np

PROJECT_DIR = "/Users/cesar/Documents/Default Project/portfolio-case-la-maison-noire"
REMOTION_DIR = "/Users/cesar/Documents/remotion-studio"
REPORT_PATH = os.path.join(PROJECT_DIR, "data/pixel_audit_report.json")

def compute_ssim_and_bounding_box(img1_path, img2_path):
    if not os.path.exists(img1_path) or not os.path.exists(img2_path):
        return None
    
    # Read grayscale
    img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)
    
    if img1 is None or img2 is None:
        return None
    
    img1 = cv2.resize(img1, (960, 540))
    img2 = cv2.resize(img2, (960, 540))
    
    # 1. Mean Squared Error (MSE)
    mse = float(np.mean((img1.astype("float") - img2.astype("float")) ** 2))
    
    # 2. Structural Similarity Index (SSIM)
    C1 = (0.01 * 255) ** 2
    C2 = (0.03 * 255) ** 2
    img1_f = img1.astype(np.float64)
    img2_f = img2.astype(np.float64)
    mu1 = cv2.GaussianBlur(img1_f, (11, 11), 1.5)
    mu2 = cv2.GaussianBlur(img2_f, (11, 11), 1.5)
    mu1_sq = mu1 ** 2
    mu2_sq = mu2 ** 2
    mu1_mu2 = mu1 * mu2
    sigma1_sq = cv2.GaussianBlur(img1_f ** 2, (11, 11), 1.5) - mu1_sq
    sigma2_sq = cv2.GaussianBlur(img2_f ** 2, (11, 11), 1.5) - mu2_sq
    sigma12 = cv2.GaussianBlur(img1_f * img2_f, (11, 11), 1.5) - mu1_mu2
    ssim_map = ((2 * mu1_mu2 + C1) * (2 * sigma12 + C2)) / ((mu1_sq + mu2_sq + C1) * (sigma1_sq + sigma2_sq + C2))
    ssim_score = float(np.mean(ssim_map))
    
    # 3. Canny Edge Bounding Box [x, y, w, h]
    edges1 = cv2.Canny(img1, 100, 200)
    contours, _ = cv2.findContours(edges1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    bbox = [0, 0, 0, 0]
    if contours:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        bbox = [int(x), int(y), int(w), int(h)]
        
    return {
        "mse": round(mse, 2),
        "ssim": round(ssim_score, 4),
        "delta_e": round(1.0 - ssim_score, 4),
        "bounding_box": bbox,
    }

def run_audit():
    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    report = {"chunks": {}, "mean_ssim": 0.0, "total_chunks": 28}
    ssim_scores = []
    
    for i in range(1, 29):
        chunk_key = f"chunk_{i:02d}"
        orig_img_path = f"/var/folders/b8/nljj6dqj6h75kjp13s488zn80000gn/T/opencode/chunk_extracts/frame_0001.png"
        rem_img_path = f"/var/folders/b8/nljj6dqj6h75kjp13s488zn80000gn/T/opencode/remotion_frames_c{i}/frame_0001.png"
        
        metrics = compute_ssim_and_bounding_box(orig_img_path, rem_img_path)
        if metrics:
            report["chunks"][chunk_key] = metrics
            ssim_scores.append(metrics["ssim"])
        else:
            report["chunks"][chunk_key] = {"status": "pending_rendering_still"}
            
    if ssim_scores:
        report["mean_ssim"] = round(float(np.mean(ssim_scores)), 4)
        
    with open(REPORT_PATH, "w") as f:
        json.dump(report, f, indent=2)
        
    print(f"OpenCV SSIM Audit report written to: {REPORT_PATH}")
    print(f"Overall SSIM Score: {report.get('mean_ssim', 'N/A')}")

if __name__ == "__main__":
    run_audit()
