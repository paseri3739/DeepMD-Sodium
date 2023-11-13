from ase import Atoms
from ase.constraints import FixBondLengths
from ase.io.gaussian import write_gaussian_in
from ase.visualize import view
from random import uniform
import numpy as np

# Define positions for a trigonal bipyramidal structure of Na atoms
positions = [
    (0, 0, 0),  # Central Na atom
    (0, 0, 1),  # Vertex of the trigonal bipyramid
    (np.sqrt(3) / 2, 0, -0.5),  # Base atoms of the bipyramid
    (-np.sqrt(3) / 2, 0, -0.5),  # Base atoms of the bipyramid
    (0, 1, -0.5),  # Base atoms of the bipyramid
]

# Create the Atoms object
atoms = Atoms("Na5", positions=positions)

# Create constraints for all bond lengths to be less than 6 Å
constraints = []
for i in range(1, 5):
    for j in range(i + 1, 5):
        constraints.append((i, j))

constraint = FixBondLengths(constraints)

# Apply the constraints to the Atoms object
atoms.set_constraint(constraint)


# Function to generate a random structure with bond length constraints
def generate_structure(atoms, distance=6.0):
    while True:
        new_positions = []
        for pos in atoms.get_positions():
            new_positions.append(pos + uniform(-0.5, 0.5))
        atoms.set_positions(new_positions)

        # Check if the bond lengths satisfy the constraints
        distances = atoms.get_all_distances()
        if np.all(distances[np.triu_indices(5, 1)] < distance):
            break

    return atoms


# Generate a random structure
random_structure = generate_structure(atoms)

# Output the optimized atomic positions
print("Optimized atomic positions:")
print(random_structure.positions)

# Save the optimized structure in XYZ file format
random_structure.write("optimized_structure.xyz")

# Write out the Gaussian input file including force calculation
with open("gaussian_input_with_forces.com", "w") as file:
    write_gaussian_in(
        file,
        random_structure,
        label="Na5",
        method="B3LYP",
        basis="6-31G(d)",
        extra="Force",
    )

print("Gaussian input file including force calculation has been generated.")
