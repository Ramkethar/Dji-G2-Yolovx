---

# **Real-time Object Detection in FPV Drone with YOLOv10 on NDI Live Stream**

This project demonstrates how to enable real-time object detection on an FPV drone using the YOLOv10 model, leveraging the NDI live stream from DJI Goggles 2 for seamless processing.

---

## **Prerequisites**
- **Hardware**:
  - DJI Goggles 2
  - Cosmostreamer Box (Raspberry Pi 4B)
- **Software**:
  - Python 3.9
  - Miniconda3
  - VSCode with Jupyter extension (recommended for ease of use)

---

## **Introduction**
This repository provides a step-by-step guide to setting up real-time object detection using YOLOv10. The system processes NDI live streams captured via the `ndi-python` library, enabling advanced object detection with Python.

---

## **Setup Instructions**

### **Step 1: Install Prerequisites**
1. **Install Miniconda3**:  
   [Download Miniconda3](https://docs.conda.io/en/latest/miniconda.html) and follow the installation instructions.

2. **Clone the Repository**:  
   Open a terminal (Miniconda3 Command Prompt) and run:
   ```bash
   git clone https://github.com/Ramkethar/Dji-G2-Yolov10.git
   ```
   Alternatively, download the repository as a ZIP file and extract it.

3. **Create a Virtual Environment**:
   ```bash
   conda create -n djig2_env python=3.9 -y
   conda activate djig2_env
   ```

4. **Install Required Python Packages**:
   ```bash
   pip install notebook jupyter
   pip install ultralytics
   pip install torch torchvision torchaudio
   pip install opencv-python opencv-contrib-python
   pip install ndi-python
   ```

---

### **Step 2: Set Up VSCode for Jupyter Notebooks**
1. **Install VSCode**:  
   [Download Visual Studio Code](https://code.visualstudio.com/).

2. **Install Extensions**:
   - Open VSCode and go to the Extensions tab (on the left sidebar).
   - Install the following extensions:
     - **Python**
     - **Jupyter**

3. **Open the Notebook**:
   - Open the `djig2_yolov10.ipynb` notebook from the repository.
   - Ensure the Python interpreter points to the `djig2_env` Conda environment.

---

### **Step 3: Run the Notebook**
Navigate to the `DJI-G2-YOLOVX/djig2_yolov10.ipynb` file and execute the cells in sequence.

---

### **Install Cosmoviewer**
- Download and configure **Cosmoviewer**:
  - Set the display to **1080p 30fps**.
  - Enable **NDI/HX video stream**.
  - Disable UDP for optimal performance.
- Refer to the Cosmostreamer tutorial for detailed instructions.

---

### **Ethernet Configuration**
Set up the **Ethernet IP** and **subnet mask** settings in Cosmoviewer to ensure a stable connection.

---

### **Alternative Method (Optional)**
If you don’t have a Cosmostreamer box:
1. Use the **DJI Fly app** to display the DJI G2 feed.
2. Mirror the feed to your PC using **scrcpy**.
   - Note: This method may result in occasional bandwidth loss and frame skipping.

---

## **Usage**

### **Run Object Detection**
1. Clone the repository:
   ```bash
   git clone https://github.com/Ramkethar/Dji-G2-Yolov10.git
   cd Dji-G2-Yolov10
   ```

2. Run the object detection script:
   ```bash
   python yolov10.py
   ```

---

## **Features**
- **Real-Time Detection**: Optimized for low-latency performance.
- **Advanced Model**: Supports YOLOv10 for accurate object detection.
- **Easy Integration**: Use with DJI Goggles 2 and NDI streaming.

---

## **Credits**
This project is created and maintained by **Ramkethar**.

Feel free to share feedback or raise issues to improve the repository. 🎯

---

### **Changelog**
- Updated all references to YOLOv10.
- Ensured clarity and consistency for instructions.
