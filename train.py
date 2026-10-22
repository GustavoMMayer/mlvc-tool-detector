from ultralytics import YOLO

def main():
    # Carrega o modelo base pré-treinado
    model = YOLO("yolov8n.pt")  # Pode usar yolov8s.pt para um modelo ligeiramente maior

    # Inicia o Fine-Tuning
    results = model.train(
        data="Dataset/data.yaml",
        epochs=50,             # Número de épocas (ajuste conforme necessário)
        imgsz=640,             # Tamanho da imagem
        batch=16,              # Tamanho do batch
        device=0,              # Usa a GPU NVIDIA GTX detetada no Dev Container
        workers=0,
        project="runs/detect",
        name="tools_model"
    )

    print("Treino concluído com sucesso!")

if __name__ == "__main__":
    main()