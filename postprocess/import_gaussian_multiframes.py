import os
import sys
import re
import dpdata

# Check the number of arguments.
if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <input_file>")
    sys.exit(1)

# Get the input file from the command-line arguments
input_file = sys.argv[1]

# Check if the input file exists
if not os.path.isfile(input_file):
    print(f"Input file '{input_file}' does not exist.")
    sys.exit(1)

# Extract the file name from the input file path and create the output file name
base_name = os.path.basename(input_file)
name_without_ext = os.path.splitext(base_name)[0]

# Extract dimension and sequence number from the file name using regex
match = re.match(r"(\w+)_set_(\d+)", name_without_ext)
if not match:
    print(f"Invalid file name format: {name_without_ext}")
    sys.exit(1)

dimension, sequence_number = match.groups()

# Define output directories for raw and npy formats
output_dir_raw = os.path.join("data", dimension, "raw", f"set_{sequence_number}")
output_dir_npy = os.path.join("data", dimension, "npy", f"set_{sequence_number}")

# Create the output directories if they don't exist
os.makedirs(output_dir_raw, exist_ok=True)
os.makedirs(output_dir_npy, exist_ok=True)

# Load the labeled system
multiple = dpdata.LabeledSystem(file_name=input_file, fmt="gaussian/md")

print(multiple)
multiple.to(fmt="deepmd/raw", file_name=output_dir_raw, set_size=200)
multiple.to(fmt="deepmd/npy", file_name=output_dir_npy, set_size=200)
