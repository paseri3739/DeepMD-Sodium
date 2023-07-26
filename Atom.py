import numpy as np


class Atom:
    def __init__(self, atom_name: str, coordinates=None):
        self.atom_name = atom_name
        if coordinates is None:
            coordinates = [0, 0, 0]
        self.coordinates = np.array(coordinates)

    def get_coordinates(self):
        return self.coordinates
