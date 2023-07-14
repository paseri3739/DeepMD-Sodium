import random
import sys

# Check the number of arguments. This must be in the header so that the
# help message is printed if the user provides no arguments.
if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <number of loops>")
    sys.exit(1)

# constants
MIN = 2.2  # MIN
SUM = 5.8  # A+B(MIN)
NUMBER_OF_SYSTEMS = 4
ATOM_LABELS = ["Na"] * NUMBER_OF_SYSTEMS  # make a list that has 4 Na atoms
HEADER = "%NProcShared=16\n%mem=12GB\n%Chk=checkpoint.chk\n#p B3LYP/6-311+g(d) force\n\nTest\n\n0 1\n"  # header
FILE_PATH = "./output/rand.com"
NUMBER_OF_LOOPS = int(sys.argv[1])  # number of loops to generate

def generate_linear_random_coords(min):  # randomly generate coordinates
    coords = [(0.0, 0.0, 0.0)]  # initialize coords list
    for _ in range(3):  # 3 means x y z coords
        last_coord = coords[-1]
        rand = random.uniform(
            0.0, 1.0
        )  # Use random.uniform for a range of 0.0 to 1.0
        new_coord = (
            last_coord[0],
            last_coord[1],
            last_coord[2] + rand * (SUM - min) + min, #r1,2,3
        )
        coords.append(new_coord)
    return coords

def generate_2d_random_coords(min):# randomly generate coordinates
    coords = [(0.0, 0.0, 0.0)]
    return coords

def format_coord(coords):
    lines = []
    for i, coord in enumerate(coords):
        line = f"{ATOM_LABELS[i]}    {coord[0]}    {coord[1]}    {coord[2]}\n"
        lines.append(line)
    return "".join(lines)


# main
def main():
    with open(FILE_PATH, "w") as file:
        for i in range(NUMBER_OF_LOOPS):
            coords = generate_linear_random_coords(MIN)
            file.write(HEADER)
            file.write(format_coord(coords))
            if i < NUMBER_OF_LOOPS - 1:
                file.write("\n--Link1--\n")
            file.write("\n")


if __name__ == "__main__":
    main()
    print("completed!")
