import sys
import numpy as np
import cv2 as cv
import NDIlib as ndi
from ultralytics import YOLO

def main():
    # Initialize NDI
    if not ndi.initialize():
        return 0

    # Find NDI sources
    ndi_find = ndi.find_create_v2()
    if ndi_find is None:
        return 0

    sources = []
    while not len(sources) > 0:
        print('Looking for sources ...')
        ndi.find_wait_for_sources(ndi_find, 1000)
        sources = ndi.find_get_current_sources(ndi_find)

    # Create NDI receiver
    ndi_recv_create = ndi.RecvCreateV3()
    ndi_recv_create.color_format = ndi.RECV_COLOR_FORMAT_BGRX_BGRA
    ndi_recv = ndi.recv_create_v3(ndi_recv_create)
    if ndi_recv is None:
        return 0

    ndi.recv_connect(ndi_recv, sources[0])
    ndi.find_destroy(ndi_find)

    # Load YOLOv8 model
    yolo_model = YOLO('C:/Users/91902/Documents/dji g2/yolov9c.pt')

    cv.startWindowThread()

    while True:
        # Receive NDI video frame
        t, v, _, _ = ndi.recv_capture_v2(ndi_recv, 5000)

        if t == ndi.FRAME_TYPE_VIDEO:
            print('Video data received (%dx%d).' % (v.xres, v.yres))
            frame = np.copy(v.data)

            # Ensure the frame has exactly 3 channels (RGB)
            if frame.shape[2] == 4:
                frame = cv.cvtColor(frame, cv.COLOR_BGRA2BGR)

            # Perform YOLOv8 inference on the frame
            results = yolo_model(frame)

            # Ensure results is a single result object
            if isinstance(results, list) and len(results) > 0:
                result = results[0]  # Assuming the first result is the one you want
                annotated_frame = result.plot()  # Use plot() method for visualization

                # Convert frame to suitable format for OpenCV
                annotated_frame = cv.cvtColor(annotated_frame, cv.COLOR_RGB2BGR)

                # Display the annotated frame
                cv.imshow('YOLOv9 Tracking with NDI Stream', annotated_frame)

            ndi.recv_free_video_v2(ndi_recv, v)

        if cv.waitKey(1) & 0xff == 27:  # Exit on 'Esc' pressq
            break

    # Cleanup
    ndi.recv_destroy(ndi_recv)
    ndi.destroy()
    cv.destroyAllWindows()

    return 0


if __name__ == "__main__":
    sys.exit(main())
