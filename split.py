import os
import shutil
import random

def split_images(source_folder, train_folder, val_folder, split_ratio=0.8):
    # Create train and val folders if they don't exist
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(val_folder, exist_ok=True)

    # Get list of image files in source folder
    image_files = [f for f in os.listdir(source_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # Shuffle the list of image files randomly
    random.shuffle(image_files)

    # Calculate number of images for training and validation
    num_train = int(len(image_files) * split_ratio)
    num_val = len(image_files) - num_train

    # Copy images to train folder
    for image_file in image_files[:num_train]:
        source_path = os.path.join(source_folder, image_file)
        destination_path = os.path.join(train_folder, image_file)
        shutil.copy(source_path, destination_path)
        print(f"Copied {image_file} to train folder")

    # Copy images to val folder
    for image_file in image_files[num_train:]:
        source_path = os.path.join(source_folder, image_file)
        destination_path = os.path.join(val_folder, image_file)
        shutil.copy(source_path, destination_path)
        print(f"Copied {image_file} to val folder")

# Specify the source folder containing images
source_folder = "J"

# Specify the train and val folders
train_folder = "train"
val_folder = "val"

# Specify the split ratio
split_ratio = 0.8  # 80% for training, 20% for validation

# Call the function to split images
split_images(source_folder, train_folder, val_folder, split_ratio)
