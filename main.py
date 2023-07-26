from Atom import Atom
from FourAtomCluster import FourAtomCluster
from GaussianWriter import GaussianWriter

if __name__ == "__main__":
    file_path = "output.txt"
    loops = 5
    atom = Atom(atom_name="Na")

    atom_cluster = FourAtomCluster([atom] * 4)  # 4つの原子が原点に配置された状態でインスタンスが作成される
    atom_cluster.placing_atoms_in_a_plane(2.2, 5.8)  # 座標をアルゴリズムに従って配置する
    atom_cluster.display_atoms()
    # writer = GaussianWriter(atom_cluster)
    # writer.write(file_path, loops)
