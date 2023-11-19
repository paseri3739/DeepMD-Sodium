import os
import re

# Replace this with the directory containing your Gaussian log files.
log_files_dir = "./initial/coordinates_for_gaussian/log/"
com_files_dir = "./initial/coordinates_for_gaussian/"


# Function to check the termination status of Gaussian log files
def check_gaussian_logs(directory):
    # Regex pattern to match the log files with the format 'coordinates_N.log'
    pattern = re.compile(r"coordinates_(\d+)\.log")

    # List to hold indices of log files with abnormal termination
    abnormal_termination_indices = []

    # Iterate over files in the specified directory
    for filename in os.listdir(directory):
        if pattern.match(filename):
            # Open and read the file
            with open(os.path.join(directory, filename), "r") as file:
                # Read the file's content
                lines = file.readlines()
                # Check if the last line indicates normal termination
                if not lines or "Normal termination of Gaussian" not in lines[-1]:
                    # Extract the index from the filename and add to the list
                    match = pattern.match(filename)
                    if match:
                        abnormal_termination_indices.append(int(match.group(1)))

    return abnormal_termination_indices


def delete_abnormal_com_files(log_directory, com_directory):
    # Get the indices of log files with abnormal termination
    abnormal_indices = check_gaussian_logs(log_directory)

    # Iterate over these indices and delete corresponding .com files
    for index in abnormal_indices:
        com_file_path = os.path.join(com_directory, f"coordinates_{index}.com")
        if os.path.exists(com_file_path):
            os.remove(com_file_path)
            print(f"Deleted file: {com_file_path}")


# Example usage:
delete_abnormal_com_files(log_files_dir, com_files_dir)
