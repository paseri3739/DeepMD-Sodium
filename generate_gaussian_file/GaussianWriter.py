from AtomClusterInterface import AtomClusterInterface
from typing import Callable


class GaussianWriter:
    def __init__(self, atom_cluster: AtomClusterInterface):
        self.atom_cluster = atom_cluster
        self.header = self.generate_header(atom_cluster.min, atom_cluster.max)

    @staticmethod
    def generate_header(min_distance: float, max_distance: float) -> str:
        return f"%NProcShared=16\n%mem=12GB\n%Chk=checkpoint.chk\n#p B3LYP/6-311+g(d) force\n\n!min_dist: {min_distance} max_dist: {max_distance}\n\n0 1\n"

    def set_header(self, header: str) -> None:
        self.header = header

    # Callableを書いておくことでatom_clusterに実装されたメソッドの補完が効く。中身はラムダ式？
    def write(self, file_path, write_times: int, algorithm: Callable[[], AtomClusterInterface]) -> None:
        if self.header is None:
            print("No header has been set.")
            return

        count = 0
        with open(file_path, "w") as file:
            while count < write_times:
                print(f"placing trial {count}")
                self.atom_cluster = algorithm()  # Use the specified algorithm

                if self.atom_cluster.is_possible():
                    print(self.atom_cluster.is_possible())
                    file.write(self.header)
                    self._write_atom_cluster(file)
                    print("cluster written")
                    if count < write_times - 1:
                        file.write("\n--Link1--\n")
                    count += 1  # Increment count only when condition is met
                file.write("\n")  # add a new line the end of the file
        print(f"Gaussian input file has been written to {file_path}")

    def _write_atom_cluster(self, file) -> None:
        for atom in self.atom_cluster.atoms:
            coordinates = atom.get_coordinates_as_list()
            # If there are only two coordinates provided (2D case), append 0 as the third coordinate
            if len(coordinates) == 2:
                coordinates.append(AtomClusterInterface.origin[2])  # add z coordinate if it is missing
            file.write(f"{atom.atom_name} {coordinates[0]} {coordinates[1]} {coordinates[2]}\n")
