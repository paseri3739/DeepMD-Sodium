import os
import sys

import dpdata

# Check the number of arguments. This must be in the header so that the
# help message is printed if the user provides no arguments.
if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <input_directory>")
    sys.exit(1)

# Get the input file from the command-line arguments
input_dir = sys.argv[1]
output_dir = "dumped"

# Check if the input file exists
if not os.path.isdir(input_dir):
    print(f"Input directory '{input_dir}' does not exist.")
    sys.exit(1)

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# classmethod from_dir(dir_name, file_name, fmt='auto', type_map=None) 入力形式
multiple = dpdata.MultiSystems.from_dir(
    dir_name=input_dir, file_name="*.log", fmt="gaussian/log"
)  # 正規表現で捕捉する

print(multiple)
multiple.to_deepmd_raw(output_dir)
multiple.to("deepmd/npy", "data", set_size=1000)
