from FourAtomCluster import FourAtomCluster
import GaussianWriter

if __name__ == "__main__":
    file_path = "output.com"
    loops = 10
    minimum_distance = 2.2
    max_distance = 5.8
    # 4つの異なるAtomインスタンスをNaとして作成。最短距離と最長距離を指定。
    atom_cluster = FourAtomCluster.from_atom_name(atom_name="Na", count=4, min=minimum_distance, max=max_distance)
    atom_cluster.place_atoms_in_a_cube().display_vector_condition()
    atom_cluster.display_atoms()
    atom_cluster.display_atom_distances()
    atom_cluster.plot_3d(line=True)

    # writer = GaussianWriter(atom_cluster)
    # writer.write(file_path, loops, algorithm=lambda cluster: atom_cluster.place_atoms_in_a_cube())
