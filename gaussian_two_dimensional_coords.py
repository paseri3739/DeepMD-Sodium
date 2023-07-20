import random

import numpy as np


def generate_points(min, sum):
    origin = np.array([0, 0, 0])  # 点0の座標
    randoms = [1, 1, 1]  # null safety
    angles = [0.2, 0.2]  # null safety
    for i in range(3):
        randoms_seed = random.uniform(0, 1)
        randoms[i] = randoms_seed * (sum - min) + min
    for i in range(2):
        angle_seed = random.uniform(0, 1)
        angles[i] = angle_seed * np.pi
    print(randoms)
    print(angles)

    p1 = np.array([origin[0] + randoms[0], origin[1], origin[2]])
    p2 = np.array(
        [
            p1[0] + randoms[1] * np.cos(angles[0]),
            p1[1] + randoms[1] * np.sin(angles[0]),
            origin[2],
        ]
    )
    p3 = np.array(
        [
            p2[0] + randoms[2] * np.cos(angles[0] + angles[1]),
            p2[1] + randoms[2] * np.sin(angles[0] + angles[1]),
            origin[2],
        ]
    )
    points = [origin, p1, p2, p3]

    return points


def main():
    # データの生成
    MIN = 2.2
    SUM = 5.8
    points = generate_points(MIN, SUM)

    for i, point in enumerate(points):
        print(f"Point {i}: {point}")


# main関数の実行
if __name__ == "__main__":
    main()
