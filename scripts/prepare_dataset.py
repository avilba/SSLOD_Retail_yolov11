import os
import random
import shutil

def split_dataset(input_dir, dataset_dir, labeled_ratio=0.3):
    labeled_dir = os.path.join(dataset_dir, 'labeled')
    unlabeled_dir = os.path.join(dataset_dir, 'unlabeled')
    
    # Buat folder jika belum ada
    os.makedirs(os.path.join(labeled_dir, 'images'), exist_ok=True)
    os.makedirs(os.path.join(labeled_dir, 'labels'), exist_ok=True)
    os.makedirs(os.path.join(unlabeled_dir, 'images'), exist_ok=True)

    images_dir = os.path.join(input_dir, 'images')
    labels_dir = os.path.join(input_dir, 'labels')

    images = sorted(os.listdir(images_dir))
    labeled_count = int(len(images) * labeled_ratio)
    random.shuffle(images)

    for i, image in enumerate(images):
        src_image = os.path.join(images_dir, image)
        src_label = os.path.join(labels_dir, image.replace('.jpg', '.txt'))
        
        if i < labeled_count:
            shutil.copy(src_image, os.path.join(labeled_dir, 'images', image))
            shutil.copy(src_label, os.path.join(labeled_dir, 'labels', image.replace('.jpg', '.txt')))
        else:
            shutil.copy(src_image, os.path.join(unlabeled_dir, 'images', image))

if __name__ == "__main__":
    split_dataset('./dataset/train', './dataset', labeled_ratio=0.3)