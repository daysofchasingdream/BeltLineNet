# BeltLineNet: Real-time Circular Conveyor Belt Deviation Detection

## 🌟 Introduction

Detecting deviation in circular pipe conveyors is essential for preventing material spillage, environmental contamination, and ensuring operational efficiency.

This repository introduces our work "*BeltLineNet: A Lightweight Real-time Network for Circular Conveyor Belt Deviation Detection*". The current version provides **experimental results** and **dataset access**. Code, implementation details, and training weights will be released **upon paper acceptance**.

Two demonstration videos have been uploaded for intuitive comparison:

 🔹 **Baseline method**
  


https://github.com/user-attachments/assets/7572f9b2-e9a6-452f-becf-71df2261bbeb


  
 🔹 **Our BeltLineNet method (with proposed enhancements)**
  
  https://github.com/user-attachments/assets/f41a324d-80db-48b0-b711-c772476b678b


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

