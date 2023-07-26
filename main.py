from Atom import Atom
from FourAtomCluster import FourAtomCluster
from GaussianWriter import GaussianWriter

if __name__ == "__main__":
    file_path = "output.txt"
    loops = 5
    atom = Atom(atom_name="Na")

    # atom_cluster = FourAtomCluster([atom] * 4) このように記述すると4つのAtomはすべて同じインスタンスとして生成されるため1つの座標を変更するとすべてのAtomインスタンスの座標が変更されてしまう。
    atom_cluster = FourAtomCluster([Atom(atom_name="Na") for _ in range(4)])  # リスト内包表記を利用する。
    atom_cluster.placing_atoms_in_a_line(2.2, 5.8)  # 座標をアルゴリズムに従って配置する
    atom_cluster.display_atoms()
    writer = GaussianWriter(atom_cluster)
    writer.write(file_path, loops)
