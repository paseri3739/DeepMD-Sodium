import numpy as np
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt


def place_points_in_a_cube(r, t, f):
    # Points
    p1 = np.array([0, 0, 0])
    p0 = np.array([-r[0] * np.sin(np.pi * t[0]), 0, -r[0] * np.cos(np.pi * t[0])])
    p2 = np.array([0, 0, r[1]])
    p33 = np.array(
        [
            -r[2] * np.sin(np.pi * t[1]) * np.cos(np.pi * f),
            -r[2] * np.sin(np.pi * t[1]) * np.sin(np.pi * f),
            r[1] - r[2] * np.cos(np.pi * t[1]),
        ]
    )
    return [p0, p1, p2, p33]


def distance_checks(points: list[np.ndarray], criteria: float):
    # Distance checks
    if euclidean(points[0], points[3]) < criteria:
        return "False0-3"
    elif euclidean(points[0], points[2]) < criteria:
        return "False0-2"
    elif euclidean(points[1], points[2]) < criteria:
        return "False1-3"
    else:
        return None


def plot_points(points: list[np.ndarray]):
    # Visualization
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(*zip(*points), s=100)
    ax.plot(*zip(*points))
    for i, point in enumerate(points):
        ax.text(point[0] + 0.2, point[1] + 0.2, point[2] + 0.2, str(i))
    plt.show()


# Parameters as lists
r = [1, 1, 1]
t = [0.2, 0.2]
f = 0.5

points4 = place_points_in_a_cube(r, t, f)
plot_points(points4)

result = distance_checks(points4, criteria=0.4)
if result is not None:
    print(result)
