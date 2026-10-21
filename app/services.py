import io
from PIL import Image
from ultralytics import YOLO

# Carrega o modelo YOLO (ajuste o caminho se necessário)
model = YOLO("models/best.pt")

def run_inference(image_bytes: bytes) -> list:
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    results = model(image)
    
    detections = []
    for result in results:
        for box in result.boxes:
            x_min, y_min, x_max, y_max = box.xyxy[0].tolist()
            confidence = float(box.conf[0])
            cls_id = int(box.cls[0])
            class_name = model.names[cls_id]
            
            detections.append({
                "class_name": class_name,
                "confidence": round(confidence, 2),
                "box": {
                    "x_min": round(x_min, 2),
                    "y_min": round(y_min, 2),
                    "x_max": round(x_max, 2),
                    "y_max": round(y_max, 2)
                }
            })
    return detections