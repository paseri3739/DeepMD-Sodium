from abc import ABC, abstractmethod

import numpy as np

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

    @abstractmethod
    def plot_2d(self) -> None:
        pass

    @abstractmethod
    def plot_3d(self) -> None:
        pass

    @classmethod
    def from_atom_name(cls, atom_name: str, count: int, min: float, max: float):
        return cls([Atom.from_name(atom_name) for _ in range(count)], min, max)

    def display_atoms(self) -> None:
        for i, atom in enumerate(self.atoms):
            print(f"Atom Name{i}: {atom.atom_name}, Coordinates: {atom.coordinates}")

    def get_atoms_coordinates(self) -> list[np.ndarray]:
        return [atom.get_coordinates() for atom in self.atoms]
