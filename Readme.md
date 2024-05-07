# **Real-time Object Detection in Fpv Drone with YOLOv8 and YOLOv9 on NDI Live Stream**

## Prerequisites
- DJI Goggles 2
- Cosmostreamer box for DJI G2 (Raspberry Pi 4B)

## Introduction
This project enables real-time object detection using YOLOv8 and YOLOv9 models on an NDI live stream from DJI Goggles 2. The NDI live stream is captured using the `ndi-python` library, allowing seamless integration with Python for further processing.

## Setup Instructions
### Install Cosmoviewer
Download Cosmoviewer and set it up by adjusting the display settings to 1080p 30fps and enabling NDI/HX video stream. Ensure UDP is turned off for optimal performance. Refer to the setup tutorial provided by Cosmostreamer for detailed instructions.

### Ethernet Configuration
Configure the Ethernet IP and subnet mask settings in Cosmoviewer to establish a stable connection.

### Alternative Method (Optional)
Another method involves displaying the DJI G2 feed using the DJI Fly app and mirroring it to PC using scrcpy. Note that this method may introduce occasional bandwidth loss and frame skipping.

## Installation
### Install required Python packages
```bash
pip install ndi-python torch cv2 ultralytics numpy

##Usage
##Clone the repository:
##Copy code
git clone <repository_url>

##Navigate to the project directory:
##Copy code
cd <project_directory>

##Run either yolov8.py or yolov9.py script:
##Copy code
python yolov8.py
python yolov9.py
