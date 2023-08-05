import numpy as np

from Atom import Atom
from AtomClusterInterface import AtomClusterInterface
from typing import Union


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
        r = np.random.rand(self.SIZE_OF_SYSTEM - 1) * (self.max - self.min) + self.min  # Update this line
        t = np.pi * np.random.rand(self.NUMBER_OF_ANGLES)  # Multiply pi directly here
        f = np.pi * np.random.rand()  # Multiply pi directly here

        # Generate points
        p0 = np.array(AtomClusterInterface.origin)  # Changed from p1 to p0
        p1 = np.array([-r[0] * np.sin(t[0]), 0, -r[0] * np.cos(t[0])])  # Changed from p0 to p1
        p2 = np.array([0, 0, r[1]])
        p33 = np.array(
            [
                -r[2] * np.sin(t[1]) * np.cos(f),
                -r[2] * np.sin(t[1]) * np.sin(f),
                r[1] - r[2] * np.cos(t[1]),
            ]
        )
        points = [p0, p1, p2, p33]  # Also changed the order here
        for i, atom in enumerate(self.atoms):
            atom.coordinates = points[i]

        return self

    def _calculate_vectors(self) -> tuple[np.ndarray, np.ndarray]:
        v01: np.ndarray = self.atoms[1].coordinates - self.atoms[0].coordinates  # 変更したatomの座標を利用するようにした
        v23: np.ndarray = self.atoms[3].coordinates - self.atoms[2].coordinates
        return (v01, v23)

    def check_minimum_distance(self, checkall: bool = False) -> Union[str, list[str]]:
        points = np.array(self.get_atoms_coordinates_by_list())
        # Distance checks for all atomic combinations
        fails = []
        for i in range(self.SIZE_OF_SYSTEM - 1):
            for j in range(i + 1, self.SIZE_OF_SYSTEM):
                if np.linalg.norm(points[i] - points[j]) >= self.min:
                    continue
                fails.append(f"False{i + 1}-{j + 1}")
                if not checkall:
                    return fails[0]
        # failsに値が入っていればfailsを返し、入っていなければ(falseでなければ)"distances okay"を返す。距離が通る場合str型になる。
        return fails if fails else "distances okay"

    def display_atom_distances(self) -> None:
        for i in range(self.SIZE_OF_SYSTEM):
            for j in range(i + 1, self.SIZE_OF_SYSTEM):
                distance = np.linalg.norm(self.atoms[i].coordinates - self.atoms[j].coordinates)
                print(f"Distance between atom {i + 1} and atom {j +1}: {distance}")

    def _check_intersection(self, vectors: tuple[np.ndarray, np.ndarray]) -> tuple[float, float]:
        result: np.ndarray = np.linalg.solve(
            np.vstack((vectors[0], -vectors[1])).T, self.atoms[2].coordinates - self.atoms[0].coordinates
        )
        s: float = result[0]
        t: float = result[1]

        return (s, t)

    def _is_parallel(self, cos_theta: float) -> bool:
        cos_pi: float = 0.999
        return np.abs(cos_theta) >= cos_pi

    def _check_crossing(self, s: float, t: float) -> str:
        if 0 < s < 1 and 0 < t < 1:
            return "crossed"
        else:
            return "not crossed"

    def _check_2d_vector_condition(self) -> str:
        vectors = self._calculate_vectors()  # get 2 vectors (v01, v23)
        s, t = self._check_intersection(vectors)

        cos_theta = np.dot(vectors[0], vectors[1]) / (np.linalg.norm(vectors[0]) * np.linalg.norm(vectors[1]))
        if self._is_parallel(cos_theta):
            s = 10
            t = 10

        condition = self._check_crossing(s, t)
        return condition

    def display_2d_vector_condition(self) -> None:
        print(self._check_2d_vector_condition())

    def display_distance_condition(self) -> None:
        print(self.check_minimum_distance())

    def is_possible(self) -> bool:
        """
        Checks if the atoms are writable by verifying two conditions:
            1. The minimum distance between any two atoms is not less than self.min.
            2. The atoms are not crossing each other.
        :return: bool: True if the atoms are writable (i.e., conditions are met), False otherwise.
        """
        # Check the minimum distance condition
        min_distance_check = self.check_minimum_distance(checkall=True)
        if isinstance(min_distance_check, list):  # 距離チェックが通っている時はstr型
            # If any pair of atoms are too close to each other, return False
            return False

        # Check the crossing condition
        condition = self._check_2d_vector_condition()
        if condition == "crossed":
            # If the atoms are crossing each other, return False
            return False

        # If none of the conditions failed, return True
        return True
