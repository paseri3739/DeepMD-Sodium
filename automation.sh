#!/bin/bash

# if $1 (loop times) or $2 (dimension) is none, exit 1
if [ -z "$1" ]; then
    echo "No loop times specified"
    exit 1
fi

if [ -z "$2" ]; then
    echo "No dimension specified"
    exit 1
fi

echo "Running Python script with: $1 $2"

# Run the Python script and capture the last line containing the specific message into a variable
last_line=$(python3 ./generate_gaussian_file/generate_gaussian_file.py "$1" "$2" | grep "Gaussian input file has been written to" | tail -n 1)

# Extract the file path from the message
file_path=$(echo "$last_line" | awk -F" " '{print $NF}')

# Now $file_path should contain the file path
echo "File path extracted: $file_path"

# Replace the extension of $file_path from .com to .log
log_path="${file_path%.com}.log"

# Run the Gaussian simulation
echo "Gaussian Launching..."
g16 < "$file_path" > "$log_path"
echo "Gaussian Done"

# Run the Python scripts for post-processing
python3 ./postprocess/split_gaussian.py "$log_path" "$2"
python3 ./postprocess/import_gaussian_from_dir.py "splited/${2}_set_1"  # Assuming you want to process the latest set
