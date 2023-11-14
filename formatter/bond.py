from ase.io import read
from ase.neighborlist import neighbor_list

# .xyzファイルを読み込む
atoms = read("./coordinates/coordinates_1.xyz")

# カットオフ半径を設定（単位はアングストローム）
cutoff_radius = 6.0  # 例として1.5 Åをカットオフ半径とする

# 各原子の近傍原子と結合を設定する
i, j = neighbor_list("ij", atoms, cutoff_radius)

# 結果を表示（あるいは結合を設定するためのデータとして利用）
for index in range(len(i)):
    print(f"Atom {i[index]} is bonded to atom {j[index]}")
