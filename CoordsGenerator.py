import random
from typing import List, Tuple


class CoordsGenerator:
    def __init__(self, min: float, sum: float, atom: str):
        self.min = min
        self.sum = sum
        self.atom = atom

    def generate_linear_random_coords(self) -> List[Tuple[float, float, float]]:
        coords: List[Tuple[float, float, float]] = [(0.0, 0.0, 0.0)]  # initialize coords list
        for _ in range(3):  # 3 means x y z coords
            last_coord = coords[-1]
            rand = random.uniform(0.0, 1.0)  # Use random.uniform for a range of 0.0 to 1.0
            new_coord = (
                last_coord[0],
                last_coord[1],
                last_coord[2] + rand * (self.sum - self.min) + self.min,  # r1,2,3
            )
            coords.append(new_coord)
        return coords

    def format_coord(self, coords: List[Tuple[float, float, float]]) -> str:
        lines: List[str] = []
        for i, coord in enumerate(coords):
            line = f"{self.atom}    {coord[0]}    {coord[1]}    {coord[2]}\n"
            lines.append(line)
        return "".join(lines)
