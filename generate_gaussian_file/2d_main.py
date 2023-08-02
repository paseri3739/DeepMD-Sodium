from FourAtomCluster import FourAtomCluster
from GaussianWriter import GaussianWriter

if __name__ == "__main__":
    file_path = "../output.com"
    loops = 10
    min_val = 2.2
    max_val = 5.8
    # 4つの異なるAtomインスタンスをNaとして作成。最短距離と最長距離を指定。
    atom_cluster = FourAtomCluster.from_atom_name(atom_name="Na", count=4, min=min_val, max=max_val)

    # リファクタリングによりメソッドチェーンによる記述が可能となった
    # atom_cluster.place_atoms_in_a_plane().check_and_report_conditions(plot_type="2D")

    writer = GaussianWriter(atom_cluster)
    # ラムダ式を使うとメソッドを実行せずに別のメソッドに渡せる
    writer.write(file_path, loops, algorithm=lambda cluster: atom_cluster.place_atoms_in_a_plane())
