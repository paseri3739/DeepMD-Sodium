from ase import Atoms
import numpy as np
from ase.constraints import FixBondLengths
from random import uniform

# Na原子5つの初期配置を作成（三方両錐形）
positions = [
    (0, 0, 0),  # 中心のNa原子
    (0, 0, 1),  # 三方両錐形の一つの頂点
    (np.sqrt(3) / 2, 0, -0.5),  # 底面のNa原子
    (-np.sqrt(3) / 2, 0, -0.5),  # 底面のNa原子
    (0, 1, -0.5),  # 底面のNa原子
]

# Atomsオブジェクトを作成
atoms = Atoms("Na5", positions=positions)

# 結合距離の制約を作成（すべての結合距離を6Å以内に）
constraints = []
for i in range(1, 5):
    for j in range(i + 1, 5):
        constraints.append((i, j))

constraint = FixBondLengths(constraints)

# Atomsオブジェクトに制約を適用
atoms.set_constraint(constraint)


# 構造をランダムに生成する関数
def generate_structure(atoms, distance=6.0):
    while True:
        new_positions = []
        for pos in atoms.get_positions():
            new_positions.append(pos + uniform(-0.5, 0.5))
        atoms.set_positions(new_positions)

        # 結合距離が制約を満たしているかをチェック
        distances = atoms.get_all_distances()
        if np.all(distances[np.triu_indices(5, 1)] < distance):
            break

    return atoms


# ランダムな構造を生成
random_structure = generate_structure(atoms)

# スクリプトの最後に以下を追加します。

# 最適化された原子の位置を出力
print("最適化された原子の位置:")
print(atoms.positions)

# 最適化された構造をXYZファイル形式で保存
atoms.write("optimized_structure.xyz")
