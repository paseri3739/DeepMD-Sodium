import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import re
import argparse
import math
import numpy as np
from typing import Optional
from Atom import Atom
from GeneralAtomCluster import GeneralAtomCluster

# Regular expression pattern for matching atomic coordinates. plz ask chatgpt if you don't understand
# each () is grouping. Name, x, y, z
PATTERN = r"([A-Za-z]{1,2})\s+([-\d\.]+)\s+([-\d\.]+)\s+([-\d\.]+)"


def _match_coordinates(line: str) -> Optional[re.Match]:
    return re.match(PATTERN, line)


def _parse_line_and_make_atom(line: str) -> Optional[Atom]:
    match = _match_coordinates(line)
    if match:  # not None
        atom, x, y, z = match.groups()
        x, y, z = map(float, [x, y, z])
        return Atom(atom, [x, y, z])
    return None


def extract_min_max_from_line(line: str) -> Optional[tuple[float, float]]:
    pattern = r"!min_dist:\s*(\d+\.\d+)\s*max_dist:\s*(\d+\.\d+)"
    match = re.match(pattern, line)
    if match:
        min_dist, max_dist = map(float, match.groups())
        return min_dist, max_dist
    return None


def _is_new_molecule(line: str) -> bool:
    return line.startswith("--Link1--")


def parse_gaussian_file(filename: str) -> list[GeneralAtomCluster]:
    clusters = []

    with open(filename, "r") as file:
        atoms = []
        min_val, max_val = None, None  # これをデフォルト値として設定

        for line in file:
            # max, minの情報を取得する
            if line.startswith("!min_dist"):
                min_val, max_val = extract_min_max_from_line(line)
                continue

            atom = _parse_line_and_make_atom(line)
            if atom:
                atoms.append(atom)
            elif _is_new_molecule(line):
                if atoms and min_val is not None and max_val is not None:
                    clusters.append(GeneralAtomCluster(atoms, min_val, max_val))
                    atoms = []
                    min_val, max_val = None, None  # 値をリセット

        if atoms and min_val is not None and max_val is not None:
            clusters.append(GeneralAtomCluster(atoms, min_val, max_val))

    return clusters


# get grid size to export
def _get_plot_dimensions(num_molecules: int) -> int:
    return int(math.ceil(math.sqrt(num_molecules)))


def plot_molecules(clusters: list[GeneralAtomCluster], plot_type: str, show_plot: bool = False) -> None:
    if not clusters:
        return

    n = _get_plot_dimensions(len(clusters))
    fig, axs = plt.subplots(n, n, figsize=(5 * n, 5 * n))

    for i, cluster in enumerate(clusters):
        ax = axs.flat[i]
        if plot_type == "3d":
            ax = cluster.plot_3d(show=False)
        else:
            ax = cluster.plot_2d(show=False)
        ax.figure = fig  # Update the figure associated with the Axes
        fig.axes.append(ax)  # Manually add Axes to the figure
        fig.add_axes(ax)  # More formally add the Axes

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
