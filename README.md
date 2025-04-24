# BeltLineNet: Real-time Circular Conveyor Belt Deviation Detection

## 🎯 Introduction

Detecting deviation in circular pipe conveyors is essential for preventing material spillage, environmental contamination, and ensuring operational efficiency.

This repository introduces our work "*BeltLineNet: A Lightweight Real-time Network for Circular Conveyor Belt Deviation Detection*". 

Two demonstration videos have been uploaded for intuitive comparison:

🔹 **Baseline method**

https://github.com/user-attachments/assets/618d51d0-2148-48b1-af8f-f3e51ed233c0



🔹 **Our BeltLineNet method (with proposed enhancements)**

https://github.com/user-attachments/assets/8af2cb04-d1d1-4d21-8049-5485eed51e29







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

📋 [Zenodo Repository - CCDD Dataset](https://doi.org/10.5281/zenodo.15094230)

Original source videos used to create the dataset are also included in this repository.

### 📖 Citation
🙏 If you find this dataset or project useful in your research or applications, please consider citing the following paper:

```
@ARTICLE{10974487,
  author={Zhao, Long and Su, Jinhui and Zhong, Yusheng and Xie, Weiwei and Su, Jinya and Chen, Xisong and Chen, Congyan and Li, Shihua},
  journal={IEEE Sensors Journal}, 
  title={BeltLineNet: A Shape-Prior-Guided Lightweight Network for Real-Time Deviation Detection in Circular Pipe Conveyors}, 
  year={2025},
  volume={},
  number={},
  pages={1-1},
  keywords={Belt Deviation;Circular Pipe Conveyor;Machine Vision;Model Compression;Object Detection},
  doi={10.1109/JSEN.2025.3561351}
}
```

