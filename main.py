from Atom import Atom
from FourAtomCluster import FourAtomCluster
from GaussianWriter import GaussianWriter

if __name__ == "__main__":
    file_path = "output.txt"
    loops = 5
    min_val = 2.2
    max_val = 5.8

    atom_cluster = FourAtomCluster([Atom(atom_name="Na") for _ in range(4)])
    writer = GaussianWriter(atom_cluster, min_val, max_val)  # min_val, max_valを追加
    writer.write(file_path, loops)
