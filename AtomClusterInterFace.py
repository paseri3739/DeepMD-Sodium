from abc import ABC, abstractmethod

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from Atom import Atom


class AtomClusterInterface(ABC):
    """
    AtomCluster is a class that represents a cluster of atoms.
    """

    def __init__(self, atoms: list[Atom], min, max):
        self.atoms = atoms
        self.min = min
        self.max = max

    @abstractmethod
    def placing_atoms_in_a_plane(self):
        pass

    @abstractmethod
    def placing_atoms_in_a_line(self):
        pass

    def plot_2d(self) -> None:
        points = self.get_atoms_coordinates()
        plt.figure()
        # split coordinates into x and y
        x = [point[0] for point in points]
        y = [point[1] for point in points]
        plt.plot(x, y, marker="o")
        for i, p in enumerate(points):
            plt.text(p[0], p[1], str(i), ha="right")
        plt.show()

    def plot_3d(self) -> None:
        points = self.get_atoms_coordinates()
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")

        # split coordinates into x, y and add z=0 if not present
        x = [point[0] for point in points]
        y = [point[1] for point in points]
        z = [point[2] if len(point) > 2 else 0 for point in points]

        ax.plot(x, y, z, marker="o")

        for i, p in enumerate(points):
            # Add a default z=0 coordinate if not present
            p = list(p)
            if len(p) == 2:
                p.append(0)
            ax.text(p[0], p[1], p[2], str(i), ha="right")
        plt.show()

    def plot_3d_with_line(self) -> None:
        points = self.get_atoms_coordinates()
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")

        # split coordinates into x, y and add z=0 if not present
        x = [point[0] for point in points]
        y = [point[1] for point in points]
        z = [point[2] if len(point) > 2 else 0 for point in points]

        # plot lines between points
        ax.plot(x, y, z, marker="o")

        for i, p in enumerate(points):
            # Add a default z=0 coordinate if not present
            p = list(p)
            if len(p) == 2:
                p.append(0)
            ax.text(p[0], p[1], p[2], str(i), ha="right")  # p0=x, p1=y, p2 = z
        plt.show()

    @classmethod
    def from_atom_name(cls, atom_name: str, count: int, min: float, max: float):
        return cls([Atom.from_name(atom_name) for _ in range(count)], min, max)

    def display_atoms(self) -> None:
        for i, atom in enumerate(self.atoms):
            print(f"Atom Name{i}: {atom.atom_name}, Coordinates: {atom.coordinates}")

    def get_atoms_coordinates(self) -> list[np.ndarray]:
        return [atom.get_coordinates() for atom in self.atoms]
