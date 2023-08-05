from FourAtomCluster import FourAtomCluster
from GaussianWriter import GaussianWriter

if __name__ == "__main__":
    file_path = "output.com"
    loops = 10
    minimum_distance = 2.2
    max_distance = 5.8
    # 4つの異なるAtomインスタンスをNaとして作成。最短距離と最長距離を指定。
    atom_cluster_3d = FourAtomCluster.from_atom_name(atom_name="Na", count=4, min=minimum_distance, max=max_distance)
    atom_cluster_3d.place_atoms_in_a_cube()
    atom_cluster_3d.display_atoms()
    atom_cluster_3d.display_atom_distances()
    atom_cluster_3d.display_distance_condition()
    atom_cluster_3d.plot_3d(line=True)

    writer = GaussianWriter(atom_cluster_3d)
    writer.write(file_path, loops, algorithm=atom_cluster_3d.place_atoms_in_a_cube)
