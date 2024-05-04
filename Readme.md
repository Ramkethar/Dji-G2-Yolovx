Real-time Object Detection with YOLOv8 and YOLOv9 on NDI Live Stream

Prerequisites:
DJI Goggles 2
Cosmostreamer box for DJI G2 (Raspberry Pi 4B)


Introduction:
This project enables real-time object detection using YOLOv8 and YOLOv9 models on an NDI live stream from DJI Goggles 2. The NDI live stream is captured using the ndi-python library, allowing seamless integration with Python for further processing.

Setup Instructions:
Install Cosmoviewer: Download Cosmoviewer and set it up by adjusting the display settings to 1080p 30fps and enabling NDI/HX video stream. Ensure UDP is turned off for optimal performance. Refer to the setup tutorial provided by Cosmostreamer for detailed instructions.
Ethernet Configuration: Configure the Ethernet IP and subnet mask settings in Cosmoviewer to establish a stable connection.
Alternative Method (Optional): Another method involves displaying the DJI G2 feed using the DJI Fly app and mirroring it to PC using scrcpy. Note that this method may introduce occasional bandwidth loss and frame skipping.

Introduction:
This project enables real-time object detection using YOLOv8 and YOLOv9 models on an NDI live stream from DJI Goggles 2. The NDI live stream is captured using the ndi-python library, allowing seamless integration with Python for further processing.


Setup Instructions:
Install Cosmoviewer: Download Cosmoviewer and set it up by adjusting the display settings to 1080p 30fps and enabling NDI/HX video stream. Ensure UDP is turned off for optimal performance. Refer to the setup tutorial provided by Cosmostreamer for detailed instructions.
Ethernet Configuration: Configure the Ethernet IP and subnet mask settings in Cosmoviewer to establish a stable connection.
Alternative Method (Optional): Another method involves displaying the DJI G2 feed using the DJI Fly app and mirroring it to PC using scrcpy. Note that this method may introduce occasional bandwidth loss and frame skipping.


Installation:
Install required Python packages:
Copy code
pip install ndi-python torch cv2 ultralytics numpy
Usage
Clone the repository:
bash
Copy code
git clone <repository_url>
Navigate to the project directory:
bash
Copy code
cd <project_directory>
Run either yolov8.py or yolov9.py script:
Copy code
python yolov8.py
Copy code
python yolov9.py

Models Download:
Download the YOLOv8 and YOLOv9 models from the following links:
YOLOv8 Model
YOLOv9 Model

Notes:
Ensure that the DJI G2 feed is being streamed and available before running the scripts. Try Running the ndirec example code to check if g2 is streaming correctly.
Adjust the paths to the YOLOv8 and YOLOv9 models in the scripts according to your directory structure.
Feel free to contribute to this project by raising issues or submitting pull requests. For any further assistance, please contact the project maintainers.
