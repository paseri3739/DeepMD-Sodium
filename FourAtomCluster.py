import random

import numpy as np

from Atom import Atom
from AtomClusterInterFace import AtomClusterInterface


class FourAtomCluster(AtomClusterInterface):
    def __init__(self, atoms: list[Atom]):
        if len(atoms) != 4:
            raise ValueError("FourAtomCluster must have 4 atoms.")
        self.atoms = atoms

    def placing_atoms_in_a_plane(self, min_val: float, max_val: float) -> list[np.ndarray]:
        # Updated to assign different coordinates to each atom
        points = []
        for atom in self.atoms:
            origin = np.array([0.0, 0.0, 0.0])
            randoms = [1.0, 1.0, 1.0]
            angles = [0.2, 0.2]

            random.seed()  # Seed the random number generator once

            for i in range(3):
                randoms[i] = random.uniform(min_val, max_val)

            for i in range(2):
                angles[i] = random.uniform(0, np.pi)

            p1 = np.array([origin[0] + randoms[0], origin[1], origin[2]])
            p2 = np.array([p1[0] + randoms[1] * np.cos(angles[0]), p1[1] + randoms[1] * np.sin(angles[0]), origin[2]])
            p3 = np.array(
                [
                    p2[0] + randoms[2] * np.cos(angles[0] + angles[1]),
                    p2[1] + randoms[2] * np.sin(angles[0] + angles[1]),
                    origin[2],
                ]
            )
            points = [origin, p1, p2, p3]

            # Update the coordinates of the atoms with the generated points
            for i, point in enumerate(points):
                self.atoms[i].coordinates = point

        return points

    def print_points(self, points: list[np.ndarray]):
        for point in points:
            print(point)

    def placing_atoms_in_a_line(self, min_val: float, max_val: float) -> list[np.ndarray]:
        coords = np.zeros((len(self.atoms), 3))
        for i in range(1, len(self.atoms)):
            rand = np.random.uniform(0.0, 1.0)
            coords[i] = coords[i - 1] + [0.0, 0.0, rand * (max_val - min_val) + min_val]

        # Update the coordinates of the atoms with the generated points
        for i, coord in enumerate(coords):
            self.atoms[i].coordinates = coord

        return coords
