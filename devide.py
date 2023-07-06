import os
import sys

# Get the input file from the command-line arguments
input_file = sys.argv[1]
output_dir = "divided"
gaussian_version = 16
counter = 1

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
search_string = f"Normal termination of Gaussian {gaussian_version}"

# Initialize the output file flag
write_output = False

# Read the text file line by line and split it into new files starting from the line after the one containing the search string
with open(input_file, "r") as file:
    for line in file:
        if search_string in line:
            counter += 1
            write_output = True
            output_file = os.path.join(output_dir, f"output_{counter}.txt")
        if write_output:
            with open(output_file, "a") as output:
                output.write(line)
