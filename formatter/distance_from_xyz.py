from ase.io import read
from ase import Atoms
import numpy as np


# XYZファイルを読み込む
atoms = read("./coordinates/coordinates_1.xyz")

# 原子間の距離を計算する
distances = []
for i in range(len(atoms)):
    for j in range(i + 1, len(atoms)):
        distance = atoms.get_distance(i, j)
        distances.append((i, j, distance))

# 距離を出力する
for pair in distances:
    print(f"原子 {pair[0]} と 原子 {pair[1]} の距離: {pair[2]:.2f} Å")
