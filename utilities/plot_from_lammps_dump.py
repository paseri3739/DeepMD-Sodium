import numpy as np
import matplotlib.pyplot as plt
import os
import sys


def read_dump(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()

    timesteps = []
    atom_positions = []

    i = 0
    while i < len(lines):
        if "TIMESTEP" in lines[i]:
            timesteps.append(int(lines[i + 1].strip()))
            i += 2
        elif "ITEM: ATOMS" in lines[i]:
            i += 1
            positions = []
            while i < len(lines) and "ITEM: TIMESTEP" not in lines[i]:
                parts = lines[i].split()
                x, y, z = float(parts[2]), float(parts[3]), float(parts[4])
                positions.append((x, y, z))
                i += 1
            atom_positions.append(np.array(positions))
        else:
            i += 1

    return timesteps, atom_positions


def plot_atoms_3d_and_save(atoms, timestep, output_directory):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(atoms[:, 0], atoms[:, 1], atoms[:, 2], s=50, c="blue", marker="o")
    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")
    ax.set_zlabel("Z Coordinate")
    ax.set_title(f"3D Atomic Positions - Timestep {timestep}")
    plt.savefig(os.path.join(output_directory, f"timestep_{timestep}.png"))  # Save the plot in the specified directory
    plt.close(fig)  # Close the plot to free up memory


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py path_to_dump_file")
        sys.exit()

    file_path = sys.argv[1]
    timesteps, atom_positions = read_dump(file_path)

    # Extract the file name without extension and create a new directory
    base_name = os.path.basename(file_path)
    dir_name = os.path.splitext(base_name)[0]
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # Loop through all timesteps and save each 3D plot as PNG in the specified directory
    for t, atoms in zip(timesteps, atom_positions):
        plot_atoms_3d_and_save(atoms, t, dir_name)
