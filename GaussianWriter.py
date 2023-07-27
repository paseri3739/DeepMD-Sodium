from typing import List

from Atom import Atom
from AtomClusterInterface import AtomClusterInterface


class GaussianWriter:
    # インスタンス全てで共有するデフォルト値はここで定義しておく
    default_header: str = "%NProcShared=16\n%mem=12GB\n%Chk=checkpoint.chk\n#p B3LYP/6-311+g(d) force\n\nTest\n\n0 1\n"

    # コンストラクタ。原子クラスタを受け取る。インスタンス毎に変えるべき初期値はここで定義する。
    def __init__(self, atom_cluster: AtomClusterInterface, placing_algorithm):
        self.header = self.default_header  # デフォルトヘッダを代入
        self.atom_cluster = atom_cluster
        self.min_val = atom_cluster.min  # FourAtomClusterのmin_valを参照
        self.max_val = atom_cluster.max  # FourAtomClusterのmax_valを参照
        self.placing_algorithm = placing_algorithm  # 座標配置アルゴリズムをインスタンス変数として保持

    def set_header(self, header: str = default_header) -> None:
        self.header = header

    def write(self, file_path, loops: int) -> None:
        with open(file_path, "w") as file:
            for i in range(loops):
                if self.header is not None:
                    file.write(self.header)
                self.placing_algorithm()  # 配置アルゴリズムを実行
                self._write_atom_cluster(file)
                if i < loops - 1:
                    file.write("\n--Link1--\n")
            file.write("\n")
        print(f"Gaussian input file has been written to {file_path}")

    def _write_atom_cluster(self, file) -> None:
        for atom in self.atom_cluster.atoms:
            coordinates = atom.get_coordinates()
            # If there are only two coordinates provided (2D case), append 0 as the third coordinate
            if len(coordinates) == 2:
                coordinates.append(0.0)
            file.write(f"{atom.atom_name} {coordinates[0]} {coordinates[1]} {coordinates[2]}\n")
