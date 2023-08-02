from FourAtomCluster import FourAtomCluster
import GaussianWriter

if __name__ == "__main__":
    file_path = "output.com"
    loops = 10
    min_val = 2.2
    max_val = 5.8
    # 4つの異なるAtomインスタンスをNaとして作成。最短距離と最長距離を指定。
    atom_cluster = FourAtomCluster.from_atom_name(atom_name="Na", count=4, min=min_val, max=max_val)
    atom_cluster.place_atoms_in_a_cube().check_and_report_conditions(plot_type="none")
    atom_cluster.display_atoms()
    atom_cluster.plot_3d(line=True)

    # writer = GaussianWriter(atom_cluster)
    # writer.write(file_path, loops, algorithm=lambda cluster: atom_cluster.place_atoms_in_a_cube())
