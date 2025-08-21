import os
import argparse
import shutil

# Argument parser to handle command line arguments
parser = argparse.ArgumentParser(description="Rename files containing 'quest' in their names.")
parser.add_argument('-s', '--source-dir', type=str, required=True)
args = parser.parse_args()

current_directory = os.getcwd()
directory = args.source_dir
files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.startswith("quest")]
for file in files:
    # copy the file from a given directory to current_directory
    source_file = os.path.join(directory, file)
    destination_file = os.path.join(current_directory, file)
    shutil.copy(source_file, destination_file)
    # os.rename(source_file, destination_file)




