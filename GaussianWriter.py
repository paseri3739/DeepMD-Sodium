
from AtomClusterInterface import AtomClusterInterface


class GaussianWriter:
    default_header: str = "%NProcShared=16\n%mem=12GB\n%Chk=checkpoint.chk\n#p B3LYP/6-311+g(d) force\n\nTest\n\n0 1\n"

    def __init__(self, atom_cluster: AtomClusterInterface, placing_algorithm):
        self.header = self.default_header
        self.atom_cluster = atom_cluster
        self.min_val = atom_cluster.min
        self.max_val = atom_cluster.max
        self.placing_algorithm = placing_algorithm

    def set_header(self, header: str = default_header) -> None:
        self.header = header

    def write(self, file_path, loops: int) -> None:
        with open(file_path, "w") as file:
            for i in range(loops):
                # Execute the placing algorithm and get the resulting cluster
                resulting_cluster = self.placing_algorithm()
                # Check the conditions of the cluster and get the result
                check_result = resulting_cluster.check_and_report_conditions("none")

                # If the conditions are met, write the cluster to the file
                if check_result in ["crossed", "not crossed"]:
                    if self.header is not None:
                        file.write(self.header)
                    self._write_atom_cluster(file)
                    if i < loops - 1:
                        file.write("\n--Link1--\n")
            file.write("\n")
        print(f"Gaussian input file has been written to {file_path}")

    def _write_atom_cluster(self, file) -> None:
        for atom in self.atom_cluster.atoms:
            coordinates = atom.get_coordinates()
            if len(coordinates) == 2:
                coordinates.append(AtomClusterInterface.origin[2]) # add z coordinate if it is missing
            file.write(f"{atom.atom_name} {coordinates[0]} {coordinates[1]} {coordinates[2]}\n")
