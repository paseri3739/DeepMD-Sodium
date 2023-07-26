import random

import matplotlib.pyplot as plt
import numpy as np

from Atom import Atom
from AtomClusterInterface import AtomClusterInterface


class FourAtomCluster(AtomClusterInterface):
    def __init__(self, atoms: list[Atom]):
        if len(atoms) != 4:
            raise ValueError("FourAtomCluster must have 4 atoms.")
        self.atoms = atoms

    def placing_atoms_in_a_plane(self, min: float, sum: float):
        origin: np.ndarray = np.array([0, 0, 0])
        randoms: list[float] = [1, 1, 1]
        angles: list[float] = [0.2, 0.2]
        NUMBER_OF_POINTS = 4
        NUMBER_OF_ANGLES = 2
        for i in range(NUMBER_OF_POINTS - 1):
            randoms_seed: float = random.uniform(0, 1)
            randoms[i] = randoms_seed * (sum - min) + min
        for i in range(NUMBER_OF_ANGLES):
            angle_seed: float = random.uniform(0, 1)
            angles[i] = angle_seed * np.pi
        p0: np.ndarray = origin
        p1: np.ndarray = np.array([p0[0] + randoms[0], p0[1], p0[2]])
        p2: np.ndarray = np.array(
            [p1[0] + randoms[1] * np.cos(angles[0]), p1[1] + randoms[1] * np.sin(angles[0]), p0[2]]
        )
        p3: np.ndarray = np.array(
            [
                p2[0] + randoms[2] * np.cos(angles[0] + angles[1]),
                p2[1] + randoms[2] * np.sin(angles[0] + angles[1]),
                p0[2],
            ]
        )
        points: list[np.ndarray] = [p0, p1, p2, p3]
        for i, atom in enumerate(self.atoms):
            atom.coordinates = points[i]

        return self

    def print_points(self, points: list[np.ndarray]):
        for point in points:
            print(point)

    def get_atoms_coordinates(self) -> list[np.ndarray]:
        return [atom.get_coordinates() for atom in self.atoms]

    def plot_points(self) -> None:
        points = self.get_atoms_coordinates()  # Get the coordinates of the atoms in the cluster
        plt.figure()
        plt.plot(*zip(*points), marker="o")
        for i, point in enumerate(points):
            plt.text(point[0], point[1], str(i), ha="right")
        plt.show()

    def placing_atoms_in_a_line(self, min_val: float, max_val: float):
        """
        Places the atoms in a line with a random distance between them.
        :param min_val: Minimum distance between atoms
        :param max_val: Maximum distance between atoms
        :return:
        """
        # Generate the points
        coords = np.zeros((len(self.atoms), 3))
        for i in range(1, len(self.atoms)):
            rand = np.random.uniform(0.0, 1.0)
            coords[i] = coords[i - 1] + [0.0, 0.0, rand * (max_val - min_val) + min_val]

        # Update the coordinates of the atoms with the generated points
        for i, coord in enumerate(coords):
            self.atoms[i].coordinates = coord

        return self
