# BeltLineNet: Real-time Circular Conveyor Belt Deviation Detection

## 🎯 Introduction

Detecting deviation in circular pipe conveyors is essential for preventing material spillage, environmental contamination, and ensuring operational efficiency. 

This repository provides the implementation for our paper, "*BeltLineNet: A Lightweight Real-time Network for Circular Conveyor Belt Deviation Detection*". It includes complete code and weights to replicate the experimental results reported in our paper.

The entire experimental framework is developed based on [Ultralytics](https://github.com/ultralytics/ultralytics), a comprehensive and efficient object detection toolbox. We sincerely acknowledge their excellent contributions.

## ⚙️ Code Structure and Usage

### 📁Repository Structure

The main directory structure is as follows:

```plaintext
│── ultralytics/           # Ultralytics framework (base environment)
│   │── nn/
│   │   │── extra_modules/ # Custom feature enhancement modules (Line Feature Interaction Enhancement)
│   │── utils/             # Custom loss strategies (Shape-Prior-Based Penalty Strategy)
│
│── weights/               # Trained weights for inference (weight.pt)
│── inference.py           # Inference script
│
│── Based_results.avi      # Results without the proposed strategies
│── BeltLineNet_results.avi# Results with BeltLineNet strategies (ours)
│── test_video/            # Video data samples for testing
```

### Getting Started

#### 1. Installation

To replicate our results, please first configure the Ultralytics environment:

```bash
git clone https://github.com/ultralytics/ultralytics.git
cd ultralytics
pip install -r requirements.txt
```

#### 2. Inference

The trained model weights (`weight.pt`) for our proposed BeltLineNet are stored in the `weights/` folder.

To perform inference, run the following command from the repository root directory:

```bash
python inference.py
```

The inference script will automatically load the model weights and process the provided video or images.

#### 3. Custom Modules

- **Shape-Prior-Based Penalty Strategy**: Implemented under `ultralytics/utils/`.
- **Line Feature Interaction Enhancement Module**: Implemented under `ultralytics/nn/extra_modules/`.

#### 4. Experimental Results

Two demonstration videos are provided for comparison:

- **`Based_results.avi`**: Results using the original oriented bounding box (OBB) detection method without our proposed enhancements.
- **`BeltLineNet_results.avi`**: Results obtained by applying our proposed shape-prior penalty strategy and line feature enhancement module, demonstrating improved detection performance, especially on thin, elongated belt-line features.

## 📂 Dataset: Circular pipe Conveyor belt line Deviation Dataset (CCDD)

Due to the absence of publicly available datasets specifically targeting circular pipe conveyor deviation detection, we introduce the **Circular pipe Conveyor belt line Deviation Dataset (CCDD)**, explicitly tailored for detecting critical conveyor components—rollers and belt lines—under realistic industrial scenarios.

### 📌 Dataset Overview

- **Data Source:** Authentic, unaugmented images captured directly from operational industrial environments.
- **Acquisition Method:** Images manually captured by personnel mimicking the inspection robot's trajectory and perspectives.
- **Dataset Characteristics:**
  - Realistic inspection scenarios: slight camera shaking, minor motion blur, varied yet typical viewpoints, and visual occlusions.
  - Diverse industrial sites: coal mines, docks, chemical plants, ensuring dataset robustness and practical relevance.

### 📌 Dataset Composition

- **Total Instances:**
  - Rollers: **4,201**
  - Belt Lines: **1,025**
- **Annotations Format:** Oriented Bounding Box (OBB) annotations provided.

### 📌 Availability and Access

The CCDD dataset, including images and OBB annotations, is publicly available at:

📎 [Zenodo Repository - CCDD Dataset](https://doi.org/10.5281/zenodo.15094230)

Additionally, the original source videos used to create the dataset are provided in the repository.
