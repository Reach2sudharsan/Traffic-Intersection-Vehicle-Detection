# **Traffic Intersection Vehicle Detection**


## Overview
This project focuses on detecting vehicles at a simulated traffic intersection built by Mihir Gandhi [(link to repo)](https://github.com/mihir-m-gandhi/Traffic-Intersection-Simulation-with-Stats/tree/main) using a YOLOv5 object detection model. 

## Features
- **Custom Dataset**: The [dataset](https://universe.roboflow.com/sg-icrum/simtrafficview5k), called **SimTrafficView5K**, has 5000 images generated from the  traffic intersection simulation, annotated in YOLOv5 format using OpenCV.
- **Efficient Model Training**: YOLOv5s model trained on images for optimized detection performance.
- **Multi-Class Detection**: The model detects different vehicle classes.
- **Easy Integration**: The trained model can be used directly for inference with images, videos, or live camera feeds.

## Dataset
- **Source**: Screenshots of a traffic intersection simulation.
- **Annotations**: YOLOv5-compatible `.txt` format labels for bounding boxes.
- **Classes**: Includes classes such as `Bike`, `Bus`, `Car`, `Truck`, etc.
- **Format**: 
  - Images in `.png` format.
  - Labels stored in `.txt` files with YOLOv5 format.


