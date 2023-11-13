from FourAtomCluster import FourAtomCluster
from GaussianWriter import GaussianWriter
import sys
import os
import re

if __name__ == "__main__":
    print("Arguments received:", sys.argv)

    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <loop times to generate> <dimension>")
        sys.exit(1)

    loops = int(sys.argv[1])
    dimension = sys.argv[2]
    # スクリプトのあるディレクトリを取得
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # スクリプトのあるディレクトリの1つ上のディレクトリをカレントディレクトリに設定
    os.chdir(os.path.join(script_dir, "../"))
    directory_path = f"./comfile/{dimension}/"

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    def get_next_file_number():
        """Get the next file number based on existing files in the directory."""
        files = os.listdir(directory_path)
        pattern = re.compile(rf"{dimension}_set_(\d+).com")
        max_number = 0
        for file in files:
            match = pattern.match(file)
            if match:
                max_number = max(max_number, int(match.group(1)))
        return max_number + 1

    start_counter = get_next_file_number()

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

    counter = get_next_file_number()
    # file_pathの行を変更します。
    file_path = f"{directory_path}{dimension}_set_{counter}.com"

    writer.write(file_path, loops, algorithm=algorithm)
