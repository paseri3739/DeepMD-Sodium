from typing import List

from Atom import Atom
from AtomClusterInterFace import AtomClusterInterface


class GaussianWriter:
    # インスタンス全てで共有するデフォルト値はここで定義しておく
    default_header: str = "%NProcShared=16\n%mem=12GB\n%Chk=checkpoint.chk\n#p B3LYP/6-311+g(d) force\n\nTest\n\n0 1\n"

    # コンストラクタ。ファイルパスと原子の種類を受け取る。インスタンス毎に変えるべき初期値はここで定義する。
    def __init__(self, atom_cluster: AtomClusterInterface):
        self.header = self.default_header  # デフォルトヘッダを代入
        self.atom_cluster = atom_cluster

    def set_header(self, header: str = default_header) -> None:
        self.header = header

    def write(self, file_path, loops: int) -> None:
        with open(file_path, "w") as file:
            for i in range(loops):
                if self.header is not None:
                    file.write(self.header)
                self._write_atom_cluster()
                if i < loops - 1:
                    file.write("\n--Link1--\n")
            file.write("\n")

    @staticmethod
    def _write_atom_cluster() -> None:
        for coord in self.atom_cluster:
            file.write(f"{Atom.atom_name} {coord[0]} {coord[1]} {coord[2]}\n")
