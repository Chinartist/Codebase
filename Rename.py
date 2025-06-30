import os 

import re

# Function to rename files in a directory
def rename_files_in_directory(directory):
    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Loop through each file in the directory
    for filename in files:
        # Check if the file is a .txt file
        if filename.endswith('.jpg'):
            # Extract the part of the filename before the first underscore
            new_filename = "00"+filename
            # Construct the full path to the old and new filenames
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            # Rename the file
            os.rename(old_file, new_file)
            print(f'Renamed: {old_file} to {new_file}')
rename_files_in_directory('/nvme0/public_data/Occupancy/proj/img2img-turbo/outputs/120f/cycle_1_cmp/images')