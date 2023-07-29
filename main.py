from FourAtomCluster import FourAtomCluster
from GaussianWriter import GaussianWriter

if __name__ == "__main__":
    file_path = "output.log"
    loops = 4
    min_val = 2.2
    max_val = 5.8

    atom_cluster = FourAtomCluster.from_atom_name("Na", 4, min_val, max_val)  # 4つの異なるAtomインスタンスをNaとして作成。最短距離と最長距離を指定。
    #atom_cluster.place_atoms_in_a_plane()
    #atom_cluster.plot_3d(line=True)  # 線を引くかどうかはline引数で指定。デフォルトはFalse。
    writer = GaussianWriter(atom_cluster)
    writer.write(file_path, loops, algorithm=lambda x: atom_cluster.place_atoms_in_a_plane()) #ラムダ式を使うとメソッドを実行せずに別のメソッドに渡せる
