import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import re
import argparse
import math
import numpy as np
from typing import Optional
from generate_gaussian_file import *

# Regular expression pattern for matching atomic coordinates
PATTERN = r"([A-Za-z]{1,2})\s+([-\d\.]+)\s+([-\d\.]+)\s+([-\d\.]+)"


def _match_coordinates(line: str) -> Optional[re.Match]:
    return re.match(PATTERN, line)


def _parse_line(line: str) -> Optional[tuple[str, float, float, float]]:
    match = _match_coordinates(line)
    if match:  # not None
        atom, x, y, z = match.groups()
        x, y, z = map(float, [x, y, z])
        return (atom, x, y, z)
    return None


def _is_new_molecule(line: str) -> bool:
    return line.startswith("--Link1--")


def parse_gaussian_file(filename: str) -> list[list[tuple[str, float, float, float]]]:
    molecules = []
    molecule = []

    with open(filename, "r") as file:
        for line in file:  # ここで直接ファイルから行を読み込む
            coord = _parse_line(line)
            if coord:
                molecule.append(coord)
            elif _is_new_molecule(line):
                molecules.append(molecule)
                molecule = []

    # 最後の分子を追加する（存在する場合）
    if molecule:
        molecules.append(molecule)

    return molecules


# get grid size to export
def _get_plot_dimensions(num_molecules: int) -> int:
    return int(math.ceil(math.sqrt(num_molecules)))


def _plot_molecule(ax: plt.Axes, molecule, index: int, plot_type: str) -> None:
    atoms, x, y, z = zip(*molecule)

    if plot_type == "3d":
        ax.plot(x + x[:1], y + y[:1], z + z[:1], color="blue")
        ax.scatter(x, y, z, color="red", s=100)
    elif plot_type == "2d":
        ax.plot(x + x[:1], y + y[:1], color="blue")
        ax.scatter(x, y, color="red", s=100)
    else:
        raise ValueError(f"Unsupported plot_type: {plot_type}")

    for j in range(len(x)):
        if plot_type == "3d":
            ax.text(x[j], y[j], z[j], f"{atoms[j]}{j + 1}", color="green", fontsize=12)
        else:
            ax.text(x[j], y[j], f"{atoms[j]}{j + 1}", color="green", fontsize=12)

    ax.set_title(f"Cluster {index+1}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    # Only for 3D plots. format axis length to 1:1:1
    if plot_type == "3d":
        ax.set_zlabel("Z")

        max_range = np.array([max(x) - min(x), max(y) - min(y), max(z) - min(z)]).max() / 2.0
        mean_x, mean_y, mean_z = np.mean(x), np.mean(y), np.mean(z)
        ax.auto_scale_xyz(
            [mean_x - max_range, mean_x + max_range],
            [mean_y - max_range, mean_y + max_range],
            [mean_z - max_range, mean_z + max_range],
        )


def plot_molecules(molecules, plot_type: str, show_plot: bool = False) -> None:
    n = _get_plot_dimensions(len(molecules))
    fig, axs = plt.subplots(
        n, n, figsize=(5 * n, 5 * n), subplot_kw={"projection": "3d" if plot_type == "3d" else None}
    )

    for i, ax in enumerate(axs.flat):
        if i < len(molecules):
            _plot_molecule(ax, molecules[i], i, plot_type)
        else:
            ax.axis("off")

    plt.tight_layout()
    plt.savefig("output.png")
    if show_plot:
        plt.show()


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("--plot", default="3d", choices=["2d", "3d"], help="Choose the type of plot: 2D or 3D.")
    parser.add_argument("--show", action="store_true", help="Display the plot.")
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    molecules = parse_gaussian_file(args.filename)
    plot_molecules(molecules, args.plot, args.show)


if __name__ == "__main__":
    main()
