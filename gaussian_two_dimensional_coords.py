import random
from typing import List, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np


def generate_points(min: float, sum: float) -> List[np.ndarray]:
    origin: np.ndarray = np.array([0, 0, 0])
    randoms: List[float] = [1, 1, 1]
    angles: List[float] = [0.2, 0.2]
    for i in range(3):
        randoms_seed: float = random.uniform(0, 1)
        randoms[i] = randoms_seed * (sum - min) + min
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


def main() -> None:
    # データの生成
    MIN: float = 2.2
    SUM: float = 5.8
    points: List[np.ndarray] = generate_points(MIN, SUM)

    for i, point in enumerate(points):
        print(f"Point {i}: {point}")


# main関数の実行
if __name__ == "__main__":
    main()
