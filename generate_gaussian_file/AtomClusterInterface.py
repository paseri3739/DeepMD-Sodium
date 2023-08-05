from abc import ABC, abstractmethod

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from Atom import Atom
from typing import Union
import numpy as np


class AtomClusterInterface(ABC):
    """
    AtomCluster is a class that represents a cluster of atoms.
    """

    origin_xyz = (0.0, 0.0, 0.0)

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

    def plot_2d(self) -> None:
        """
        Plots the 2D projection of the atoms using matplotlib.
        """
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
        """
        Plots the 3D projection of the atoms using matplotlib.
        :param line: Optional boolean to draw lines between points. Defaults to False.
        """
        points = self.get_atoms_coordinates_by_list()
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")

        # split coordinates into x, y and add z=0 if not present
        x = [point[0] for point in points]
        y = [point[1] for point in points]
        z = [point[2] if len(point) > 2 else 0 for point in points]

        # Get maximum range of the coordinates to have equal scales
        max_range = np.array([max(x) - min(x), max(y) - min(y), max(z) - min(z)]).max() / 2.0

        # Get the mean of each coordinate
        mean_x = np.mean(x)
        mean_y = np.mean(y)
        mean_z = np.mean(z)

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

        # Set the limits of the plot to have equal scales
        ax.auto_scale_xyz(
            [mean_x - max_range, mean_x + max_range],
            [mean_y - max_range, mean_y + max_range],
            [mean_z - max_range, mean_z + max_range],
        )

        plt.show()
