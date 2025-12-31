# A Hybrid Deep Learning Framework for Malware Classification & Zero-Shot Anomaly Detection

## Project Overview
This research explores the intersection of **Computer Vision** and **Cybersecurity** to address the challenge of evolving malware landscapes. By transforming raw binary executables into high-dimensional representations, this framework leverages spatial feature extraction to identify known malware families while utilizing an **Anomaly-based Clustering** layer to facilitate **Zero-Shot Learning** for previously unseen "zero-day" threats.

> **Note on Accessibility:** This repository serves as technical documentation. The full source code and model weights are currently **private** pending peer-reviewed publication (Target: *IEEE Transactions*). Detailed architecture drafts and code snippets are available for review during the residency interview process.

---

## Key Research Contributions
* **Multi-Dataset Fusion (Malimg + MALEVIS):** Engineered a robust training pipeline utilizing both the **Malimg** and **MALEVIS** datasets. This fusion ensures superior generalization across diverse malware architectures and varied binary-to-image mapping techniques.
* **Binary-to-Image Engine:** Developed a custom preprocessing engine to convert raw binary data into grayscale and RGB-mapped representations ($N \times M$ matrices), preserving structural signatures of malicious code.
* **Hybrid Architecture:** Designed a dual-pathway model (CNN-LSTM) to capture both spatial visual features and sequential execution dependencies.
* **Zero-Shot Generalization:** Integrated an unsupervised anomaly clustering layer to detect statistical deviations, allowing the model to flag novel "out-of-distribution" (OOD) malware samples.

---

## Dataset Description
To ensure the robustness of the framework, two primary benchmarks were combined:
1. **Malimg Dataset:** 9,339 images across 25 malware families.
2. **MALEVIS Dataset:** A high-quality dataset consisting of 14,226 images from 26 malware classes (and one legitimate class), providing high-fidelity visual representations of binary structures.

---

## Technical Stack
* **Language:** Python 3.x
* **Deep Learning:** PyTorch / TensorFlow 
* **Mathematics:** NumPy, Scikit-Learn (Anomaly Clustering), Matplotlib
* **Data Engineering:** OpenCV, PIL (Image Normalization & Data Augmentation)

---

## Research Status: [In Preparation]
**Title:** "Zero-Shot Generalization in Image-Based Malware Detection via Hybrid Deep Architectures and Multi-Dataset Fusion"  
**Researcher:** Muhammad Usman [Google Scholar](https://scholar.google.com/citations?user=Egg_oLsAAAAJ&hl=en)
