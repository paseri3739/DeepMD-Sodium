from Atom import Atom
from FourAtomCluster import FourAtomCluster
from GaussianWriter import GaussianWriter

if __name__ == "__main__":
    file_path = "output.txt"
    loops = 5
    min_val = 2.2
    max_val = 5.8

    atom_cluster = FourAtomCluster.from_atom_name("Na", 4, min_val, max_val)  # 4つの異なるNaインスタンスを作成する
    atom_cluster.placing_atoms_in_a_plane()
    atom_cluster.display_atoms()
    atom_cluster.plot_points()
    # writer = GaussianWriter(atom_cluster, min_val, max_val)  # min_val, max_valを追加
    # writer.write(file_path, loops)
