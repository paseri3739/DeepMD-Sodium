# %%
from FourAtomCluster import FourAtomCluster
from GaussianWriter import GaussianWriter

if __name__ == "__main__":
    file_path = "../output.com"
    loops = 10
    minimum_distance = 2.2
    max_distance = 5.8
    # 4つの異なるAtomインスタンスをNaとして作成。最短距離と最長距離を指定。
    atom_cluster = FourAtomCluster.from_atom_name(atom_name="Na", count=4, min=minimum_distance, max=max_distance)

    # リファクタリングによりメソッドチェーンによる記述が可能となった
    atom_cluster.place_atoms_in_a_plane().display_2d_vector_condition()
    atom_cluster.check_minimum_distance(checkall=True)
    atom_cluster.display_distance_condition()
    atom_cluster.display_atoms()
    atom_cluster.display_atom_distances()
    atom_cluster.plot_2d()
    # %%
    writer = GaussianWriter(atom_cluster)
    # ラムダ式を使うとメソッドを実行せずに別のメソッドに渡せる
    writer.write(file_path, loops, algorithm=atom_cluster.place_atoms_in_a_plane)

# %%
