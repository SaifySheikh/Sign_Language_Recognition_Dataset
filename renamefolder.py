import os

def rename_images(folder_path):
    # Get list of files in the folder
    files = os.listdir(folder_path)

    # Iterate over each file
    for i, file_name in enumerate(files):
        # Check if the file is an image file
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Construct the new file name
            new_file_name = f"{i}.{file_name.split('.')[-1]}"
            # Rename the file
            os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))
            print(f"Renamed {file_name} to {new_file_name}")

# Specify the folder path
folder_path = "J"

# Call the function to rename images
rename_images(folder_path)
