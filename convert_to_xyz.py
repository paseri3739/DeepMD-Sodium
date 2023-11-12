import pandas as pd
import zipfile
import os


# Function to convert CSV to XYZ format and package into a ZIP
def csv_to_xyz_zip(csv_path, zip_path, atom_type="Na", num_points=7):
    df = pd.read_csv(csv_path, header=None)

    # Re-extracting all rows and the first 7 sets of XYZ coordinates, skipping the first row as it contains headers
    all_points = df.iloc[1:, 1 : (3 * num_points) + 1].values.reshape(-1, num_points, 3)

    # Create a zip file and write each xyz content
    with zipfile.ZipFile(zip_path, "w") as zipf:
        for i, points in enumerate(all_points):
            # Create a DataFrame for each set of points
            xyz_data = pd.DataFrame(points, columns=["X", "Y", "Z"])
            xyz_data.insert(0, "Atom", atom_type)

            # Prepare the content for each .xyz file
            num_atoms = len(xyz_data)
            header = f"{num_atoms}\nXYZ coordinates of {num_atoms} points\n"
            xyz_content = header + xyz_data.to_csv(sep=" ", index=False, header=False)

            # Define the xyz file name
            xyz_file_name = f"coordinates_{i+1}.xyz"
            # Define the full path
            xyz_file_path = os.path.join("coordinates", xyz_file_name)
            # Write the content to the file within the zip
            zipf.writestr(xyz_file_path, xyz_content)


# Example usage
csv_path = "path_to_your_input.csv"
zip_path = "path_to_your_output.zip"
csv_to_xyz_zip(csv_path, zip_path)
