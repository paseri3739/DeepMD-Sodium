import os
import sys

# Get the input file from the command-line arguments
input_file = sys.argv[1]
output_dir = "splited"
counter = 0

# Check the number of arguments
if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <input_file>")
    sys.exit(1)

# Check if the input file exists
if not os.path.isfile(input_file):
    print(f"Input file '{input_file}' does not exist.")
    sys.exit(1)

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# The string to search for
search_string = "Initial command:"

# Initialize the output file
output_file = os.path.join(output_dir, f"output_{counter}.log")

# Read the text file line by line and split it into new files starting from the line after the one containing the search string
with open(input_file, "r") as file:
    for line in file:
        if search_string in line:
            counter += 1
            output_file = os.path.join(output_dir, f"output_{counter}.log")
        with open(output_file, "a") as output:
            output.write(line)

# remove first file
os.remove(os.path.join(output_dir, "output_0.log"))
