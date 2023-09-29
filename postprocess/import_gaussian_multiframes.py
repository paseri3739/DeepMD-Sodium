import os
import sys
import re
import dpdata

# Check the number of arguments. This must be in the header so that the
# help message is printed if the user provides no arguments.
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
base_name = os.path.basename(input_file)  # Extract the file name from the path
name_without_ext = os.path.splitext(base_name)[0]  # Remove the extension from the file name

# Extract dimension and sequence number from the file name using regex
match = re.match(r"(\w+)_set_(\d+)", name_without_ext)
if not match:
    print(f"Invalid file name format: {name_without_ext}")
    sys.exit(1)

dimension, sequence_number = match.groups()
output_file_name = os.path.join("data", dimension, f"set{sequence_number}")

# Create the output directory if it doesn't exist
os.makedirs(output_file_name, exist_ok=True)

# Load the labeled system
multiple = dpdata.LabeledSystem(file_name=input_file, fmt="gaussian/md")

print(multiple)
multiple.to(fmt="deepmd/raw", file_name=output_file_name, set_size=200)
multiple.to(fmt="deepmd/npy", file_name=output_file_name, set_size=200)
