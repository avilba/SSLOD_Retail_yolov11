import os
import shutil

def merge_pseudo_to_labeled(unlabeled_images, unlabeled_labels, labeled_images, labeled_labels):
    # Gabungkan gambar
    for img_file in os.listdir(unlabeled_images):
        shutil.copy(os.path.join(unlabeled_images, img_file), os.path.join(labeled_images, img_file))

    # Gabungkan label
    for label_file in os.listdir(unlabeled_labels):
        shutil.copy(os.path.join(unlabeled_labels, label_file), os.path.join(labeled_labels, label_file))

merge_pseudo_to_labeled(
    unlabeled_images="dataset/unlabeled/images",
    unlabeled_labels="dataset/unlabeled/labels",
    labeled_images="dataset/labeled/images",
    labeled_labels="dataset/labeled/labels"
)