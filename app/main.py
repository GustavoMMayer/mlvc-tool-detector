from fastapi import FastAPI, UploadFile, File, HTTPException
from app.schema import DetectionResponse
from app.services import run_inference

app = FastAPI(
    title="ToolDetector API",
    description="API RESTful para detecção de ferramentas utilizando YOLO",
    version="1.0.0"
)

@app.post("/detect", response_model=DetectionResponse)
async def detect_objects(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="O arquivo enviado não é uma imagem.")
    
    try:
        contents = await file.read()
        detections = run_inference(contents)
        return {
            "status": "success",
            "detections": detections
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro no processamento: {str(e)}")