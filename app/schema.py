from pydantic import BaseModel
from typing import List

class BoundingBox(BaseModel):
    x_min: float
    y_min: float
    x_max: float
    y_max: float

class DetectionResult(BaseModel):
    class_name: str
    confidence: float
    box: BoundingBox

class DetectionResponse(BaseModel):
    status: str
    detections: List[DetectionResult]