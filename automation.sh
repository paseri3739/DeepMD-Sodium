#!/bin/bash

# if $1 is none, exit 1
if [ -z "$1" ]; then
    echo "No loop times specified"
    exit 1
fi

python3 ./generate_gaussian_file/generate_gaussian_file.py "$1"
echo "Gaussian Launching..."
g16 <output.com> output.log
echo "Gaussian Done"
python3 ./postprocess/split_gaussian.py output.log
python3 ./postprocess/import_gaussian_from_dir.py splited
