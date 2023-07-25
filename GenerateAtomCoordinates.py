import random
from typing import List, Tuple

import numpy as np

import FourAtomCluster


class GenerateAtomCoordinates:
    def __init__(self, min: float, sum: float, atom_cluster: FourAtomCluster):
        self.min = min
        self.sum = sum
        self.atom_cluster = atom_cluster

    def generate_linear_random_coords(self) -> List[Tuple[float, float, float]]:
        points: List[Tuple[float, float, float]] = [(0.0, 0.0, 0.0)]  # initialize coords list
        for _ in range(3):  # 3 means x y z coords
            last_coord = points[-1]
            rand = random.uniform(0.0, 1.0)  # Use random.uniform for a range of 0.0 to 1.0
            new_coord = (
                last_coord[0],
                last_coord[1],
                last_coord[2] + rand * (self.sum - self.min) + self.min,  # r1,2,3
            )
            points.append(new_coord)
        return points

    def generate_two_dimensional_points(self) -> List[np.ndarray]:
        origin: np.ndarray = np.array([0, 0, 0])
        randoms: List[float] = [1, 1, 1]
        angles: List[float] = [0.2, 0.2]
        for i in range(3):
            randoms_seed: float = random.uniform(0, 1)
            randoms[i] = randoms_seed * (self.sum - self.min) + self.min
        for i in range(2):
            angle_seed: float = random.uniform(0, 1)
            angles[i] = angle_seed * np.pi

        p1: np.ndarray = np.array([origin[0] + randoms[0], origin[1], origin[2]])
        p2: np.ndarray = np.array(
            [p1[0] + randoms[1] * np.cos(angles[0]), p1[1] + randoms[1] * np.sin(angles[0]), origin[2]]
        )
        p3: np.ndarray = np.array(
            [
                p2[0] + randoms[2] * np.cos(angles[0] + angles[1]),
                p2[1] + randoms[2] * np.sin(angles[0] + angles[1]),
                origin[2],
            ]
        )
        points: List[np.ndarray] = [origin, p1, p2, p3]

        return points

    def format_coord(self, points: List[Tuple[float, float, float]]) -> str:
        lines: List[str] = []
        for i, coord in enumerate(points):
            line = f"{self.atom}    {coord[0]}    {coord[1]}    {coord[2]}\n"
            lines.append(line)
        return "".join(lines)
