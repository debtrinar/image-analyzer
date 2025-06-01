import torch
import cv2
import numpy as np
from PIL import Image

# Load YOLOv5 model (download if not already cached)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def detect_objects(image: Image.Image):
    # Convert PIL to OpenCV format (BGR)
    img_cv2 = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Perform detection
    results = model(img_cv2)
    detections = results.pandas().xyxy[0].to_dict(orient="records")

    # Draw bounding boxes
    for det in detections:
        x1, y1, x2, y2 = int(det['xmin']), int(det['ymin']), int(det['xmax']), int(det['ymax'])
        label = f"{det['name']} {det['confidence']:.2f}"

        cv2.rectangle(img_cv2, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img_cv2, label, (x1, max(y1 - 10, 0)), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2)

    # Convert back to PIL for saving/display
    drawn_image = Image.fromarray(cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB))
    return detections, drawn_image
