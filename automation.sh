#!/bin/bash

# if $1 is none, exit 1
if [ -z "$1" ]; then
    echo "No loop times specified"
    exit 1
fi

# if $2 is none, exit 1
if [ -z "$2" ]; then
    echo "No dimension specified"
    exit 1
fi

# Generate the Gaussian input file based on loop times and dimension
python3 ./generate_gaussian_file/generate_gaussian_file.py "$1" "$2"

# Dynamically set the Gaussian input and output file names based on the dimension
input_file="output_${2}.com"
output_file="output_${2}.log"

echo "Gaussian Launching..."
g16 <"$input_file"> "$output_file"
echo "Gaussian Done"

# Execute post-processing steps
python3 ./postprocess/split_gaussian.py "$output_file"
python3 ./postprocess/import_gaussian_from_dir.py splited
