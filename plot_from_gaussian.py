import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import re
import sys
import argparse
import math


# Function to parse the Gaussian input file
def parse_gaussian_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    # Regular expression pattern for matching atomic coordinates
    pattern = r"Na\s+([-\d\.]+)\s+([-\d\.]+)\s+([-\d\.]+)"

    # Extract the atomic coordinates for each molecule
    molecules = []
    molecule = []
    for line in lines:
        match = re.match(pattern, line)
        if match:
            # Convert the matched strings to floats
            x, y, z = map(float, match.groups())
            molecule.append((x, y, z))
        elif line.startswith("--Link1--"):
            # Start a new molecule when encountering a "--Link1--" line
            molecules.append(molecule)
            molecule = []
    # Append the last molecule
    if molecule:
        molecules.append(molecule)

    return molecules


# Function to plot the atomic coordinates for each molecule
def plot_molecules(molecules, plot_type):
    n = int(math.ceil(math.sqrt(len(molecules))))  # Compute the grid size
    fig, axs = plt.subplots(
        n, n, figsize=(5 * n, 5 * n), subplot_kw={"projection": "3d" if plot_type == "3d" else None}
    )

    for i, ax in enumerate(axs.flat):
        if i < len(molecules):
            molecule = molecules[i]
            x, y, z = zip(*molecule)

            if plot_type == "2d":
                ax.plot(x, y, color="blue")  # Plot line
                ax.scatter(x, y, color="red", s=100)  # Plot points
                for j in range(len(x)):  # Add labels
                    ax.text(x[j], y[j], str(j + 1), color="green", fontsize=12)
            else:
                ax.plot(x, y, z, color="blue")  # Plot line
                ax.scatter(x, y, z, color="red", s=100)  # Plot points
                for j in range(len(x)):  # Add labels
                    ax.text(x[j], y[j], z[j], str(j + 1), color="green", fontsize=12)

            ax.set_title(f"Cluster {i+1}")
            ax.set_xlabel("X")
            ax.set_ylabel("Y")

            if plot_type == "3d":
                ax.set_zlabel("Z")
        else:
            ax.axis("off")  # Hide unused subplots

    plt.tight_layout()
    plt.savefig("output.png")  # Save the figure to a file
    plt.show()


# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument("--plot", default="3d")
args = parser.parse_args()

# Use the functions
molecules = parse_gaussian_file(args.filename)
plot_molecules(molecules, args.plot)
