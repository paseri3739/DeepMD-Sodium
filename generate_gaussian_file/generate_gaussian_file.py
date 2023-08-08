from FourAtomCluster import FourAtomCluster
from GaussianWriter import GaussianWriter
import sys

if __name__ == "__main__":
    # Check the number of arguments. This must be in the header so that the
    # help message is printed if the user provides no arguments.
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <loop times to generate>")
        sys.exit(1)

    file_path = "output.com"
    loops = sys.argv[1]

    if type(loops) is not int:
        print(f"Usage: {sys.argv[0]} <loop times to generate>")
        print("loops must be an integer")
        sys.exit(1)

    minimum_distance = 2.2
    max_distance = 5.8
    # 4つの異なるAtomインスタンスをNaとして作成。最短距離と最長距離を指定。
    atom_cluster_3d = FourAtomCluster.from_atom_name(atom_name="Na", count=4, min=minimum_distance, max=max_distance)
    writer = GaussianWriter(atom_cluster_3d)
    writer.write(file_path, loops, algorithm=atom_cluster_3d.place_atoms_in_a_cube)
