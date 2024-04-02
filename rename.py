import os
import glob

def rename_images(folder_path, folder_name):
    count = 0
    for file in sorted(glob.glob(os.path.join(folder_path, '*.jpg'))):  # assuming images are in jpg format
        count += 1
        new_name = f"{count+300}.jpg"
        new_path = os.path.join(folder_path, new_name)
        try:
            os.rename(file, new_path)
            print(f"Renamed {file} to {new_path}")
        except Exception as e:
            print(f"Error renaming {file}: {e}")
    return count

def main():
    base_path = 'sohamdataset'
    for folder_name in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        folder_path = os.path.join(base_path, folder_name)
        if os.path.exists(folder_path):
            print(f"Renaming images in folder {folder_name}:")
            image_count = rename_images(folder_path, folder_name)
            print(f"{image_count} images renamed.")
            print()

if __name__ == "__main__":
    main()
