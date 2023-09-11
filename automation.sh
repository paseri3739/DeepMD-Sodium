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
python3 ./generate_gaussian_file/generate_gaussian_file.py "$1" "$2"


# Run the Gaussian simulation
echo "Gaussian Launching..."
g16 < "output_${2}.com" > "output_${2}.log"
echo "Gaussian Done"

# Run the Python scripts for post-processing
python3 ./postprocess/split_gaussian.py "output_${2}.log" "$2"
python3 ./postprocess/import_gaussian_from_dir.py "splited/${2}_set_1"  # Assuming you want to process the latest set
