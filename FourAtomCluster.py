import random
from typing import List

import numpy as np

from Atom import Atom
from AtomClusterInterFace import AtomClusterInterface  # from ファイル名 import クラス名


class FourAtomCluster(AtomClusterInterface):
    def __init__(self, atoms: list[Atom]):
        super().__init__(atoms)

    def placing_atoms_in_a_plane(self, min, max):
        pass
