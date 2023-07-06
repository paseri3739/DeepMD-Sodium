import random

# constants
A = 3.6  # a + b = 5.8
B = 2.2  # MIN
NUMBER_OF_SYSTEMS = 4
ATOM_LABELS = ["Na"] * NUMBER_OF_SYSTEMS  # make a list that has 4 Na atoms
HEADER = "%NProcShared=16\n%mem=12GB\n%Chk=checkpoint.chk\n#p B3LYP/6-311+g(d) force\n\nTest\n\n0 1\n"  # header
FILE_PATH = "./output/rand.com"
NUMBER_OF_LOOPS = 3  # number of loops to generate


def generate_random_coords(a, b):  # randomly generate coordinates
    coords = [(0.0, 0.0, 0.0)]  # initialize coords list
    for _ in range(3):
        last_coord = coords[-1]
        rand = random.uniform(
            0.0, 1.0
        )  # Use random.uniform for a range of 0.0 to 1.0
        new_coord = (
            last_coord[0],
            last_coord[1],
            last_coord[2] + rand * a + b,
        )
        coords.append(new_coord)
    return coords


def write_coord(file, coords):
    for i, coord in enumerate(coords):
        file.write(
            f"{ATOM_LABELS[i]}    {coord[0]}    {coord[1]}    {coord[2]}\n"
        )


# main
def main():
    with open(FILE_PATH, "w") as file:
        for i in range(NUMBER_OF_LOOPS):
            coords = generate_random_coords(A, B)
            text = HEADER
            file.write(text)
            write_coord(file, coords)
            if i < NUMBER_OF_LOOPS - 1:
                file.write("\n--Link1--\n")
            file.write("\n")


if __name__ == "__main__":
    main()
