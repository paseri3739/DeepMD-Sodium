from abc import ABC, abstractmethod

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from Atom import Atom
from typing import Union


class AtomClusterInterface(ABC):
    """
    AtomCluster is a class that represents a cluster of atoms.
    """

    origin = (0.0, 0.0, 0.0)

    def __init__(self, atoms: list[Atom], min: float, max: float):
        self.atoms = atoms
        self.min = min
        self.max = max
        self.SIZE_OF_SYSTEM: int = len(atoms)
        self.NUMBER_OF_ANGLES: int = len(atoms) - 2

    @classmethod
    def from_atom_name(cls, atom_name: str, count: int, min: float, max: float):
        return cls([Atom.from_name(atom_name) for _ in range(count)], min, max)

    def display_atoms(self) -> None:
        for i, atom in enumerate(self.atoms):
            print(f"Atom Name{i + 1}: {atom.atom_name}, Coordinates: {atom.coordinates}")

    def get_atoms_coordinates_by_list(self) -> list:
        return [atom.get_coordinates_as_list() for atom in self.atoms]

    @abstractmethod
    def place_atoms_in_a_line(self):
        pass

    @abstractmethod
    def place_atoms_in_a_plane(self):
        pass

    @abstractmethod
    def place_atoms_in_a_cube(self):
        pass

    @abstractmethod
    def is_possible(self) -> bool:
        """
        Checks if the atoms are writable by verifying the specific conditions of the atom cluster.
        :return: bool: True if the atoms are writable (i.e., conditions are met), False otherwise.
        """
        pass

    @abstractmethod
    def display_atom_distances(self) -> None:
        pass

    @abstractmethod
    def check_minimum_distance(self, checkall: bool = False) -> Union[str, list[str]]:
        pass

    @abstractmethod
    def display_vector_condition(self) -> None:
        pass

    @abstractmethod
    def display_distance_condition(self) -> None:
        pass

    def plot_2d(self) -> None:
        points = self.get_atoms_coordinates_by_list()
        fig, ax = plt.subplots()
        # split coordinates into x and y
        x = [point[0] for point in points]
        y = [point[1] for point in points]
        ax.plot(x + [x[0]], y + [y[0]], marker="o")  # Adding the first point to the end to create a closed loop
        for i, atom in enumerate(self.atoms):
            ax.text(
                points[i][0], points[i][1], atom.atom_name + str(i + 1), ha="right"
            )  # Adding index to the atom name
        ax.set_aspect("equal", "box")  # Set the aspect of the plot to 1:1
        plt.show()

    def plot_3d(self, line: bool = False) -> None:
        points = self.get_atoms_coordinates_by_list()
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")

        # split coordinates into x, y and add z=0 if not present
        x = [point[0] for point in points]
        y = [point[1] for point in points]
        z = [point[2] if len(point) > 2 else 0 for point in points]

        # plot lines between points if line is True, otherwise just plot points
        if line:
            ax.plot(
                x + [x[0]], y + [y[0]], z + [z[0]], marker="o"
            )  # Adding the first point to the end to create a closed loop
        else:
            ax.scatter(x, y, z, marker="o")

        for i, atom in enumerate(self.atoms):
            # Add a default z=0 coordinate if not present
            p = list(points[i])
            if len(p) == 2:
                p.append(0)
            ax.text(p[0], p[1], p[2], atom.atom_name + str(i + 1), ha="right")  # Adding index to the atom name
        plt.show()
