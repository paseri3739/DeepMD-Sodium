from FourAtomCluster import FourAtomCluster
from GaussianWriter import GaussianWriter
import sys
import os

if __name__ == "__main__":
    print("Arguments received:", sys.argv)

    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <loop times to generate> <dimension>")
        sys.exit(1)

    loops = sys.argv[1]
    dimension = sys.argv[2]

    # ディレクトリを作成
    directory_path = f"./comfile/{dimension}/"
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    try:
        loops = int(sys.argv[1])
    except ValueError:
        print(f"Usage: {sys.argv[0]} <loop times to generate>")
        print("loops must be an integer")
        sys.exit(1)

    minimum_distance = 2.2
    max_distance = 5.8
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

    for counter in range(1, loops + 1):
        # ファイルパスと命名規則を変更
        file_path = f"{directory_path}output_{dimension}_{counter}.com"
        writer.write(file_path, loops, algorithm=algorithm)
        print(f"{file_path} successfully generated.")
