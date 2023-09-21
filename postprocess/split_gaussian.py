import os
import sys
import re

# Check the number of arguments
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <input_file> <dimension>")
    sys.exit(1)

# Get the input file and dimension from the command-line arguments
input_file = sys.argv[1]
dimension = sys.argv[2]
base_output_dir = "splited"
# Create the base output directory if it does not exist
if not os.path.exists(base_output_dir):
    os.makedirs(base_output_dir)
counter = 0

# Check if the input file exists
if not os.path.isfile(input_file):
    print(f"Input file '{input_file}' does not exist.")
    sys.exit(1)

# Check existing directories and find the next index
existing_dirs = [
    d
    for d in os.listdir(base_output_dir)
    if os.path.isdir(os.path.join(base_output_dir, d)) and re.match(rf"{dimension}_set_\d+", d)
]
existing_indexes = [int(match.group()) for d in existing_dirs if (match := re.search(r"\d+$", d)) is not None]

next_index = max(existing_indexes, default=0) + 1

# Create the output directory based on next_index and dimension
output_dir = os.path.join(base_output_dir, f"{dimension}_set_{next_index}")
os.makedirs(output_dir, exist_ok=True)

# The string to search for
search_string = "Initial command:"

# Initialize the output file
output_file = os.path.join(output_dir, f"{dimension}_output_{counter}.log")

# Read the text file line by line and split it into new files starting from the line after the one containing the search string
with open(input_file, "r") as file:
    for line in file:
        if search_string in line:
            counter += 1
            output_file = os.path.join(output_dir, f"{dimension}_output_{counter}.log")
        with open(output_file, "a") as output:
            output.write(line)

# Remove first file if it's empty or not needed
os.remove(os.path.join(output_dir, f"{dimension}_output_0.log"))
