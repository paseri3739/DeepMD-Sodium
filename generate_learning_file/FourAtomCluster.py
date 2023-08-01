import random

import numpy as np

from Atom import Atom
from AtomClusterInterface import AtomClusterInterface


class FourAtomCluster(AtomClusterInterface):
    def __init__(self, atoms: list[Atom], min: float, max: float):
        super().__init__(atoms, min, max)
        if len(atoms) != 4:
            raise ValueError(f"Expected 4 atoms, but got {len(atoms)}.")

    def place_atoms_in_a_line(self) -> "FourAtomCluster":
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
            coords[i] = coords[i - 1] + [0.0, 0.0, rand * (self.max - self.min) + self.min]

        # Update the coordinates of the atoms with the generated points
        for i, coord in enumerate(coords):
            self.atoms[i].coordinates = coord

        return self

    def place_atoms_in_a_plane(self) -> "FourAtomCluster":
        """
        Places the atoms in a plane with a random distance between them.
        :param min_val: Minimum distance between atoms
        :param max_val: Maximum distance between atoms
        :return:
        """
        origin: np.ndarray = np.array(AtomClusterInterface.origin[:2])  # initialize
        randoms: list[float] = [1, 1, 1]  # initialize
        angles: list[float] = [0.2, 0.2]  # initialize
        NUMBER_OF_POINTS = 4
        NUMBER_OF_ANGLES = 2
        for i in range(NUMBER_OF_POINTS - 1):
            randoms_seed: float = random.uniform(0, 1)
            randoms[i] = randoms_seed * (self.max - self.min) + self.min
        for i in range(NUMBER_OF_ANGLES):
            angle_seed: float = random.uniform(0, 1)
            angles[i] = angle_seed * np.pi
        p0: np.ndarray = origin
        p1: np.ndarray = np.array([p0[0] + randoms[0], p0[1]])
        p2: np.ndarray = np.array([p1[0] + randoms[1] * np.cos(angles[0]), p1[1] + randoms[1] * np.sin(angles[0])])
        p3: np.ndarray = np.array(
            [
                p2[0] + randoms[2] * np.cos(angles[0] + angles[1]),
                p2[1] + randoms[2] * np.sin(angles[0] + angles[1]),
            ]
        )
        points: list[np.ndarray] = [p0, p1, p2, p3]
        for i, atom in enumerate(self.atoms):  # クラス設計にあたっての変更点
            atom.coordinates = points[i]

        return self

    def place_atoms_in_a_cube(self) -> "FourAtomCluster":
        # Parameters as lists
        r = np.random.rand(3)  # Create an array of the given shape and populate it with random samples
        t = np.random.rand(2)
        f = np.random.rand()

        # Generate points
        p1 = np.array(AtomClusterInterface.origin)
        p0 = np.array([-r[0] * np.sin(np.pi * t[0]), 0, -r[0] * np.cos(np.pi * t[0])])
        p2 = np.array([0, 0, r[1]])
        p33 = np.array(
            [
                -r[2] * np.sin(np.pi * t[1]) * np.cos(np.pi * f),
                -r[2] * np.sin(np.pi * t[1]) * np.sin(np.pi * f),
                r[1] - r[2] * np.cos(np.pi * t[1]),
            ]
        )
        points = [p0, p1, p2, p33]
        for i, atom in enumerate(self.atoms):
            atom.coordinates = points[i]

        return self

    def check_distances_in_cube(self, criteria: float) -> str:
        points = np.array(self.get_atoms_coordinates())
        if np.linalg.norm(points[0] - points[3]) < criteria:
            return "False0-3"
        elif np.linalg.norm(points[0] - points[2]) < criteria:
            return "False0-2"
        elif np.linalg.norm(points[1] - points[2]) < criteria:
            return "False1-3"
        else:
            return "distances okay"

    def _calculate_vectors(self) -> list[np.ndarray]:
        v01: np.ndarray = self.atoms[1].coordinates - self.atoms[0].coordinates  # 変更したatomの座標を利用するようにした
        v23: np.ndarray = self.atoms[3].coordinates - self.atoms[2].coordinates
        return [v01, v23]

    def _check_intersection(self, vectors: list[np.ndarray]) -> list[float]:
        result: np.ndarray = np.linalg.solve(
            np.vstack((vectors[0], -vectors[1])).T, self.atoms[2].coordinates - self.atoms[0].coordinates
        )
        s: float = result[0]
        t: float = result[1]

        return [s, t]

    def _is_parallel(self, cos_theta: float) -> bool:
        cos_pi: float = 0.999
        return np.abs(cos_theta) >= cos_pi

    def _check_conditions(self, s: float, t: float) -> str:
        if np.linalg.norm(self.atoms[0].coordinates - self.atoms[3].coordinates) < self.min:  # ハードコーディングを変更
            return "False0-3"
        if np.linalg.norm(self.atoms[0].coordinates - self.atoms[2].coordinates) < self.min:
            return "False0-2"
        if np.linalg.norm(self.atoms[1].coordinates - self.atoms[3].coordinates) < self.min:
            return "False1-3"
        if 0 < s < 1 and 0 < t < 1:
            return "crossed"
        else:
            return "not crossed"

    def _plot_points(self, plot_type: str) -> None:
        if plot_type == "2D":
            self.plot_2d()

        elif plot_type == "3D":
            self.plot_3d()

    def check_and_report_conditions(self, plot_type: str) -> str:
        vectors = self._calculate_vectors()
        s, t = self._check_intersection(vectors)

        cos_theta = np.dot(vectors[0], vectors[1]) / (np.linalg.norm(vectors[0]) * np.linalg.norm(vectors[1]))
        if self._is_parallel(cos_theta):
            s = 10
            t = 10

        condition = self._check_conditions(s, t)
        if plot_type == "none":
            print(condition)
            return condition

        if condition in ["not crossed", "crossed"]:
            self._plot_points(plot_type)
            print(condition)
            return condition

        return "exception: unknown condition"
