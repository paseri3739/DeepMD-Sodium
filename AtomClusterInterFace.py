from abc import ABC, abstractmethod

from Atom import Atom


class AtomClusterInterface(ABC):
    """
    AtomCluster is a class that represents a cluster of atoms.
    """

    def __init__(self, atoms: list[Atom]):
        self.atoms = atoms

    @abstractmethod
    def placing_atoms_in_a_plane(self, min, max):
        pass

    @abstractmethod
    def placing_atoms_in_a_line(self, min, max):
        pass

    def display_atoms(self) -> None:
        for i, atom in enumerate(self.atoms):
            print(f"Atom Name{i}: {atom.atom_name}, Coordinates: {atom.coordinates}")
