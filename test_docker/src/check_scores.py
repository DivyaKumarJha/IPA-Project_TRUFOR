import numpy as np
import cv2
import os

# Paths (CHANGE ONLY IF NEEDED)
npz_dir = r'D:\Sem 6\ipa-project\TruFor\test_docker\output'
img_dir = r'D:\Sem 6\ipa-project\TruFor\test_docker\data'
save_dir = r'D:\Sem 6\ipa-project\TruFor\test_docker\visual_outputs'

# create output folder
os.makedirs(save_dir, exist_ok=True)

for f in os.listdir(npz_dir):
    if f.endswith('.npz'):

        data = np.load(os.path.join(npz_dir, f))
        print("Keys inside npz:", data.files)
        

        anomaly = data['map']
        confidence = data['conf']
        score = float(data['score'])

        anomaly = anomaly.squeeze()
        confidence = confidence.squeeze()

        # normalize anomaly
        anomaly_norm = (anomaly - anomaly.min()) / (anomaly.max() - anomaly.min() + 1e-8)

        # confidence filtered anomaly
        filtered = anomaly_norm * confidence

        # convert to heatmaps
        heatmap = cv2.applyColorMap((anomaly_norm * 255).astype(np.uint8), cv2.COLORMAP_JET)
        filtered_heatmap = cv2.applyColorMap((filtered * 255).astype(np.uint8), cv2.COLORMAP_JET)

        # load original image
        img_name = f.replace(".npz", "")
        img_path = os.path.join(img_dir, img_name)

        img = cv2.imread(img_path)

        if img is None:
            print(f"Image not found: {img_path}")
            continue

        # resize heatmaps
        heatmap = cv2.resize(heatmap, (img.shape[1], img.shape[0]))
        filtered_heatmap = cv2.resize(filtered_heatmap, (img.shape[1], img.shape[0]))

        # overlays
        overlay = cv2.addWeighted(img, 0.6, heatmap, 0.4, 0)
        filtered_overlay = cv2.addWeighted(img, 0.6, filtered_heatmap, 0.4, 0)

        # SIDE-BY-SIDE COMPARISON (THIS IS YOUR BONUS)
        combined = np.hstack((img, overlay, filtered_overlay))

        # save outputs
        cv2.imwrite(os.path.join(save_dir, img_name + "_overlay.jpg"), overlay)
        cv2.imwrite(os.path.join(save_dir, img_name + "_filtered_overlay.jpg"), filtered_overlay)
        cv2.imwrite(os.path.join(save_dir, img_name + "_compare.jpg"), combined)

        # print results
        verdict = "FAKE" if score > 0.5 else "REAL"
        print(f'File: {f}')
        print(f'Score: {score:.4f}')
        print(f'Verdict: {verdict}')
        print("Saved visualizations\n")