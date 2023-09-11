from FourAtomCluster import FourAtomCluster
from GaussianWriter import GaussianWriter
import sys

if __name__ == "__main__":
    # Check the number of arguments. This must be in the header so that the
    # help message is printed if the user provides no arguments.
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <loop times to generate> <dimension>")
        sys.exit(1)

    loops = sys.argv[1]
    dimension = sys.argv[2]
    file_path = f"output_{dimension}.com"

    try:
        loops = int(sys.argv[1])
    except ValueError:
        print(f"Usage: {sys.argv[0]} <loop times to generate>")
        print("loops must be an integer")
        sys.exit(1)

    minimum_distance = 2.2
    max_distance = 5.8
    # 4つの異なるAtomインスタンスをNaとして作成。最短距離と最長距離を指定。
    atom_cluster = FourAtomCluster.from_atom_name(atom_name="Na", count=4, min=minimum_distance, max=max_distance)
    writer = GaussianWriter(atom_cluster)

    algorithm_map = {
        "1d": atom_cluster.place_atoms_in_a_line,
        "2d": atom_cluster.place_atoms_in_a_plane,
        "3d": atom_cluster.place_atoms_in_a_cube,
    }

    algorithm = algorithm_map.get(dimension)

    if algorithm is None:
        print(f"Invalid dimension: {dimension}. Must be '1d', '2d', or '3d'.")
        sys.exit(1)

    writer.write(file_path, loops, algorithm=algorithm)
