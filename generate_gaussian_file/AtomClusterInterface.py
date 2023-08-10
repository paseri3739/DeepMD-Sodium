from abc import ABC, abstractmethod

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from Atom import Atom
from typing import Union, Optional
import numpy as np


class AtomClusterInterface(ABC):
    """
    AtomCluster is a class that represents a cluster of atoms.
    """

    origin = (0.0, 0.0, 0.0)

    def __init__(self, atoms: list[Atom], min: float, max: float):
        """
        Initializes an AtomCluster with the given atoms, minimum and maximum values.
        :param atoms: List of Atom objects.
        :param min: Minimum value for the system.
        :param max: Maximum value for the system.
        """
        self.atoms = atoms
        self.min = min
        self.max = max
        self.SIZE_OF_SYSTEM: int = len(atoms)
        self.NUMBER_OF_ANGLES: int = len(atoms) - 2

    @classmethod
    def from_atom_name(cls, atom_name: str, count: int, min: float, max: float):
        """
        Creates an AtomCluster from the given atom name, count, minimum, and maximum values.
        :param atom_name: The name of the atom.
        :param count: The count of atoms in the cluster.
        :param min: Minimum value for the system.
        :param max: Maximum value for the system.
        :return: An AtomCluster object.
        """
        return cls([Atom.from_name(atom_name) for _ in range(count)], min, max)

    def display_atoms(self) -> None:
        """
        Prints the names and coordinates of all the atoms in the cluster.
        """
        for i, atom in enumerate(self.atoms):
            print(f"Atom Name{i + 1}: {atom.atom_name}, Coordinates: {atom.coordinates}")

    def get_atoms_coordinates_by_list(self) -> list:
        """
        Retrieves the coordinates of all the atoms in the cluster.
        :return: A list of coordinates for the atoms.
        """
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
    def display_2d_vector_condition(self) -> None:
        pass

    @abstractmethod
    def display_distance_condition(self) -> None:
        pass

    def plot_2d(self, show: bool = True) -> Optional[plt.Axes]:
        points = self.get_atoms_coordinates_by_list()
        fig, ax = plt.subplots()
        x = [point[0] for point in points]
        y = [point[1] for point in points]
        ax.plot(x + [x[0]], y + [y[0]], marker="o")
        for i, atom in enumerate(self.atoms):
            ax.text(points[i][0], points[i][1], atom.atom_name + str(i + 1), ha="right")
        ax.set_aspect("equal", "box")

        if show:
            plt.show()
            return None
        else:
            return ax

    def plot_3d(self, show: bool = True) -> Optional[plt.Axes3D]:
        points = self.get_atoms_coordinates_by_list()
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        x = [point[0] for point in points]
        y = [point[1] for point in points]
        z = [point[2] if len(point) > 2 else 0 for point in points]

        max_range = np.array([max(x) - min(x), max(y) - min(y), max(z) - min(z)]).max() / 2.0
        mean_x, mean_y, mean_z = np.mean(x), np.mean(y), np.mean(z)

        ax.plot(x + [x[0]], y + [y[0]], z + [z[0]], marker="o")

        for i, atom in enumerate(self.atoms):
            p = list(points[i])
            if len(p) == 2:
                p.append(0)
            ax.text(p[0], p[1], p[2], atom.atom_name + str(i + 1), ha="right")

        ax.auto_scale_xyz(
            [mean_x - max_range, mean_x + max_range],
            [mean_y - max_range, mean_y + max_range],
            [mean_z - max_range, mean_z + max_range],
        )

        if show:
            plt.show()
            return None
        else:
            return ax
