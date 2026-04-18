# TruFor-Based Image Forgery Detection and Visualization

## Video Demonstration

A detailed video explanation of the implementation and results is available at:

https://drive.google.com/drive/u/0/folders/14tU6L69XOfVKw0aa3rL_DYiL41YWg1AY

## Overview

This project is based on the TruFor framework for image forgery detection and localization. The method combines low level forensic traces and high level visual features to identify manipulated regions in images and provide reliable predictions.

In this project, the official TruFor implementation was used with pretrained weights. The system was then extended by adding a visualization pipeline to improve interpretability and reduce false positives using confidence aware filtering.

Reference for original method and workflow:
https://grip-unina.github.io/TruFor/

---

## Objectives

- Execute TruFor using pretrained weights  
- Perform image level forgery detection using integrity score  
- Generate anomaly maps and confidence maps  
- Improve output interpretability through visualization  
- Reduce false positives using confidence based filtering  

---

## Mid Term Implementation

During the mid term phase, the following steps were completed:

- Cloned the official TruFor GitHub repository  
- Set up the environment and dependencies  
- Ran the model using pretrained weights  
- Performed inference on sample images  
- Generated:
  - Anomaly map  
  - Confidence map  
  - Integrity score  
- Classified images as REAL or FAKE using a threshold of 0.5  

The system was successfully executed end to end from input image to final prediction.

---

## End Term Improvements

The following enhancements were added to the original pipeline:

### Visualization Pipeline

- Converted anomaly maps into heatmaps using OpenCV  
- Overlayed heatmaps on original images  
- Generated visual outputs for easier interpretation  

### Confidence Aware Filtering

- Applied element wise multiplication of anomaly and confidence maps  
- Suppressed unreliable detections  
- Produced cleaner and more reliable localization results  

### Side by Side Comparison

Generated combined output images showing:

- Original image  
- Raw anomaly overlay  
- Confidence filtered overlay  

This allows direct comparison between raw and refined predictions.

---

## Key Contribution

We extended the TruFor inference pipeline by adding visual explainability and confidence aware filtering, making the system more interpretable and reliable without modifying the core model.

---

## How to Run

### Step 1: Run inference

```bash
python trufor_test.py --gpu -1 --input ../data --output ../output
```

### Step 2: Generate visual outputs

```bash
python check_scores.py
```

---

## Output

For each input image, the system produces:

- Integrity score for classification  
- Anomaly map highlighting suspicious regions  
- Confidence map indicating reliability  
- Overlay visualization  
- Confidence filtered overlay  
- Side by side comparison image  

---

## Observations

- Raw anomaly maps may contain false positives in uniform or textured regions  
- Confidence filtering helps suppress unreliable detections  
- Visualization significantly improves interpretability  
- The system performs robustly even on compressed images  

---

## Future Work

- Evaluation on benchmark datasets such as CASIA and Columbia  
- Fine tuning on domain specific datasets such as social media images  
- End to end training of all modules jointly  
- Extension to detect fully AI generated images  

---

## Conclusion

This project successfully demonstrates the TruFor framework and extends it with a practical visualization pipeline. The added confidence aware filtering improves the reliability of localization results and makes the system more suitable for real world applications.
