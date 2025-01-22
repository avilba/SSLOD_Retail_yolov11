import os
import shutil

def split_dataset(input_dir, output_dir, batch_size=500):
    os.makedirs(output_dir, exist_ok=True)
    images = sorted(os.listdir(input_dir))
    for i in range(0, len(images), batch_size):
        batch_dir = os.path.join(output_dir, f"batch_{i // batch_size}")
        os.makedirs(batch_dir, exist_ok=True)
        for img in images[i:i + batch_size]:
            shutil.copy(os.path.join(input_dir,img), os.path.join(batch_dir, img))

if __name__ == "__main__":
    split_dataset(
        input_dir="dataset/unlabeled/images",
        output_dir="dataset/unlabeled_batches",
        batch_size=500
    )