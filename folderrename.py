import os

def rename_folders(base_dir):
    folders = os.listdir(base_dir)
    for folder in folders:
        folder_path = os.path.join(base_dir, folder)
        if os.path.isdir(folder_path):
            new_folder_name = folder.split('_')[0]  # Extract the first part of the folder name
            new_folder_path = os.path.join(base_dir, new_folder_name)
            os.rename(folder_path, new_folder_path)
            print(f"Renamed '{folder}' to '{new_folder_name}'")

# Change 'base_dir' to the path of your "sohamdataset" folder
base_dir = 'C:\\Users\\LENOVO\\Downloads\\Sign Dataset Modified\\sohamdataset'
rename_folders(base_dir)
