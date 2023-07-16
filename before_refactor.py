import matplotlib.pyplot as plt
import numpy as np

p = [np.array([0, 0])]  # 点0の座標

# rand0-1 * (SUM - min) + min それぞれ生成
r = [1, 1, 1]

# 0~1
t = [0.2, 0.2]

# 点1の座標
p.append(p[0] + r[0])

# 点2の座標
p.append(
    np.array(
        [
            p[1][0] + r[1] * np.cos(np.pi * t[0]),
            p[1][1] + r[1] * np.sin(np.pi * t[0]),
        ]
    )
)

# 点3の座標
p.append(
    np.array(
        [
            p[2][0] + r[2] * np.cos(np.pi * (t[0] + t[1])),
            p[2][1] + r[2] * np.sin(np.pi * (t[0] + t[1])),
        ]
    )
)

points3 = p

v = [p[1] - p[0], p[3] - p[2]]  # v01とv23

# 辺0-1と2-3が交点をもつかどうかを判定する
result = np.linalg.solve(np.vstack((v[0], -v[1])).T, p[2] - p[0])
ss = result[0]  # 判定条件ssが0と1の間にあり
tt = result[1]  # かつttが0と1の間にあると辺0-1と2-3は交わる

costheta = np.dot(v[0], v[1]) / (
    np.linalg.norm(v[0]) * np.linalg.norm(v[1])
)  # 辺01と辺23が平行か否かを判定

if np.abs(costheta) >= 0.999:
    ss = 10
    tt = 10

if 0 < ss < 1 and 0 < tt < 1:
    print("crossed")
else:
    if np.linalg.norm(p[0] - p[3]) < 0.2:
        print("False0-3")
    elif np.linalg.norm(p[0] - p[2]) < 0.2:
        print("False0-2")
    elif np.linalg.norm(p[1] - p[3]) < 0.2:
        print("False1-3")
    else:
        plt.figure()
        plt.plot(*zip(*points3), marker="o")
        for i, point in enumerate(points3):
            plt.text(point[0], point[1], str(i), ha="right")
        plt.show()
