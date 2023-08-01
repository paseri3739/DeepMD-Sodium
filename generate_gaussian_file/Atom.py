import numpy as np


class Atom:
    def __init__(self, atom_name: str, coordinates=None):
        self.atom_name = atom_name
        if coordinates is None:
            coordinates = [0.0, 0.0, 0.0]  # default to origin
        self.coordinates = np.array(coordinates)

    @classmethod
    def from_name(cls, atom_name: str):
        return cls(atom_name, coordinates=None)  # return new atom object

    def get_coordinates(self):
        # return a copy of the coordinates as a list
        return self.coordinates.tolist()
