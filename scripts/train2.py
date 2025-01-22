from ultralytics import YOLO

def train_model():
    model = YOLO("runs/detect/train4/weights/best.pt")

    model.train(
        data='dataset/data2.yaml', 
        epochs=20, 
        imgsz=640, 
        batch=16, 
        device='0',
        augment=True,  # Aktifkan augmentasi
        mosaic=1.0,
        mixup=0.2,
        degrees=10.0,
        translate=0.1,
        scale=0.5,
        shear=2.0,
        hsv_h=0.015,
        hsv_s=0.7,
        hsv_v=0.4,
        flipud=0.1,
        fliplr=0.5
    )

if __name__ == "__main__":
    train_model()