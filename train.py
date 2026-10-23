from ultralytics import YOLO

def main():
    
    model = YOLO("tools_model/weights/last.pt")  

   
    results = model.train(
        data="Dataset/data.yaml",
        epochs=100,
        patience=50,
        resume=True,             
        imgsz=512,             
        batch=16,              
        device=0,              
        workers=8,
        amp=False,
        cache=True,
        project="./runs/detect",
        name="tools_model"
    )
 

    print("Treino concluído com sucesso!")

if __name__ == "__main__":
    main()