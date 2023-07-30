
from AtomClusterInterface import AtomClusterInterface


class GaussianWriter:
    default_header: str = "%NProcShared=16\n%mem=12GB\n%Chk=checkpoint.chk\n#p B3LYP/6-311+g(d) force\n\nTest\n\n0 1\n"

    def __init__(self, atom_cluster: AtomClusterInterface):
        self.header = self.default_header
        self.atom_cluster = atom_cluster

    def set_header(self, header: str = default_header) -> None:
        self.header = header

    def write(self, file_path, loops: int, algorithm=lambda x: x.place_atoms_in_a_plane()) -> None:
        print("write called")
        if self.header is None:
            print("No header has been set.")
            return

        count = 0
        with open(file_path, "w") as file:
            for i in range(loops):
                print(f"placing trial {count}")
                cluster = algorithm(self.atom_cluster)  # Use the passed algorithm

                print(f"condition check {count}")
                condition = cluster.check_and_report_conditions(plot_type="none")

                if condition == "not crossed":
                    file.write(self.header)
                    self._write_atom_cluster(file)
                    print("cluster written")
                    if i < loops - 1:
                        file.write("\n--Link1--\n")
                    count += 1  # Increment count only when condition is met
                    print(count)

                # Break the loop if we have met the condition enough times
                if count >= loops:
                    break

        print(f"Gaussian input file has been written to {file_path}")



    def _write_atom_cluster(self, file) -> None:
        for atom in self.atom_cluster.atoms:
            coordinates = atom.get_coordinates()
            # If there are only two coordinates provided (2D case), append 0 as the third coordinate
            if len(coordinates) == 2:
                coordinates.append(AtomClusterInterface.origin[2]) # add z coordinate if it is missing
            file.write(f"{atom.atom_name} {coordinates[0]} {coordinates[1]} {coordinates[2]}\n")
