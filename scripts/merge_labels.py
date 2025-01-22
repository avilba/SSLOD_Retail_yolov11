import os
import shutil

def merge_labels(input_dir, output_dir):
    """
    Menggabungkan file label dari beberapa batch ke dalam satu folder.

    Parameters:
    - input_dir: Direktori yang berisi batch pseudo-label (labels_batches).
    - output_dir: Direktori tujuan untuk menyimpan semua label yang digabungkan.
    """
    os.makedirs(output_dir, exist_ok=True)  # Membuat folder output jika belum ada

    for batch in os.listdir(input_dir):
        batch_labels_dir = os.path.join(input_dir, batch, "predict", "labels")
        if os.path.exists(batch_labels_dir):
            for label_file in os.listdir(batch_labels_dir):
                # Salin setiap file label ke folder output
                shutil.copy(
                    os.path.join(batch_labels_dir, label_file),
                    os.path.join(output_dir, label_file)
                )
            print(f"Labels from {batch} merged.")
        else:
            print(f"No labels found in {batch}")

if __name__ == "__main__":
    merge_labels(
        input_dir="dataset/unlabeled/labels_batches",  # Lokasi batch pseudo-label
        output_dir="dataset/unlabeled/labels"         # Lokasi output
    )