import os
import glob

def count_and_delete_images(folder_path):
    count = 0
    for file in glob.glob(os.path.join(folder_path, '*.jpg')):  # assuming images are in jpg format
        count += 1
        if count > 140:
            try:
                os.remove(file)
            except Exception as e:
                print(f"Error deleting file: {file}. Error: {e}")
    return count

def main():
    base_path = 'sohamdataset'
    for folder_name in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        folder_path = os.path.join(base_path, folder_name)
        if os.path.exists(folder_path):
            print(f"Counting and deleting images in folder {folder_name}:")
            image_count = count_and_delete_images(folder_path)
            print(f"{image_count} images found.")
            if image_count > 100:
                print("Images beyond 101 deleted.")
            else:
                print("No images deleted.")
            print()

if __name__ == "__main__":
    main()
