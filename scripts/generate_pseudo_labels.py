from ultralytics import YOLO
import os


def generate_pseudo_labels_batch(model_path, batch_dir, output_dir, conf_threshold=0.5):
    model = YOLO(model_path)
    os.makedirs(output_dir, exist_ok=True)
    for batch in os.listdir(batch_dir):
        batch_path = os.path.join(batch_dir,batch)
        if os.path.isdir(batch_path):
            output_labels_dir = os.path.join(output_dir, batch)
            os.makedirs(output_labels_dir, exist_ok=True)
            model.predict(
                source=batch_path,
                conf=conf_threshold,
                save=False,
                save_txt=True,
                save_conf=False,
                project=output_labels_dir,
                name=""
            )
            print(f"Processed batch: {batch}")

#
generate_pseudo_labels_batch(
    model_path="runs/detect/train4/weights/best.pt",
    batch_dir="dataset/unlabeled_batches",
    output_dir="dataset/unlabeled/labels_batches"
)