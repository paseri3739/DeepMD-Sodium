import random

import numpy as np

from Atom import Atom
from AtomClusterInterface import AtomClusterInterface


class FourAtomCluster(AtomClusterInterface):
    def __init__(self, atoms: list[Atom], min: float, max: float):
        super().__init__(atoms, min, max)
        if self.SIZE_OF_SYSTEM != 4:
            raise ValueError(f"Expected 4 atoms, but got {self.SIZE_OF_SYSTEM}.")

    def place_atoms_in_a_line(self) -> "FourAtomCluster":
        """
        Places the atoms in a line with a random distance between them.
        The minimum and maximum distances between atoms are determined by the self.min and self.max attributes.
        :return: self
        """
        prev_z = self.origin[2]  # initial z coordinate = 0
        for i in range(self.SIZE_OF_SYSTEM):
            if i != 0:  # For the first atom, keep the coordinates at zero.
                rand = np.random.uniform(0.0, 1.0)
                z_offset = rand * (self.max - self.min) + self.min
                prev_z += z_offset

            self.atoms[i].coordinates = np.array([self.origin[0], self.origin[1], prev_z])

        return self

    def place_atoms_in_a_plane(self) -> "FourAtomCluster":
        """
        Places the atoms in a plane with a random distance between them.
        The minimum and maximum distances between atoms are determined by the self.min and self.max attributes.
        :return: self
        """
        prev_point = np.array(self.origin[:2])  # set origin(0.0,0.0)
        # set an array initialized with 0.0 for the number of angles (size of system -2), here is 2
        angles = [0.0] * self.NUMBER_OF_ANGLES
        points = [prev_point]

        for i in range(self.SIZE_OF_SYSTEM - 1):
            # Calculate the random distance and angle
            random_distance = np.random.uniform(self.min, self.max)
            if i < self.NUMBER_OF_ANGLES:
                angles[i] = np.random.uniform(0, np.pi)

            # Generate the next point based on the random distance and angle
            next_point = prev_point + random_distance * np.array(
                [np.cos(np.sum(angles[: i + 1])), np.sin(np.sum(angles[: i + 1]))]
            )
            points.append(next_point)

            # Update prev_point
            prev_point = next_point

        for i, atom in enumerate(self.atoms):
            atom.coordinates = points[i]

        return self

    def place_atoms_in_a_cube(self) -> "FourAtomCluster":
        # Parameters as lists
        # Create an array of the given shape and populate it with random samples
        r = np.random.rand(self.SIZE_OF_SYSTEM - 1)
        t = np.random.rand(self.NUMBER_OF_ANGLES)
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

    def _calculate_vectors(self) -> list[np.ndarray]:
        v01: np.ndarray = self.atoms[1].coordinates - self.atoms[0].coordinates  # 変更したatomの座標を利用するようにした
        v23: np.ndarray = self.atoms[3].coordinates - self.atoms[2].coordinates
        return [v01, v23]

    def _check_minimum_distance(self) -> str:
        points = np.array(self.get_atoms_coordinates_by_list())
        # Distance checks for all atomic combinations
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                if np.linalg.norm(points[i] - points[j]) < self.min:
                    return f"False{i}-{j}"
        return "distances okay"

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

    def _plot_points(self, plot_type: str) -> None:
        if plot_type == "2D":
            self.plot_2d()

        elif plot_type == "3D":
            self.plot_3d()

    def _check_conditions(self, s: float, t: float) -> str:
        if 0 < s < 1 and 0 < t < 1:
            return "crossed"
        else:
            return "not crossed"

    def check_and_report_conditions(self, plot_type: str) -> str:
        min_distance_check = self._check_minimum_distance()
        print(min_distance_check)
        if min_distance_check != "distances okay":
            return min_distance_check  # FALSE {I}-{J}

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
