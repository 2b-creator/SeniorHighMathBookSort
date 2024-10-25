import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(11, 6))
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "font.size": 14,
})
# 定义圆心和半径
x_c, y_c = 0, 0  # 圆心坐标
r = 1  # 圆的半径
x_0, y_0 = 0.9, (1 - 0.9 ** 2) ** (1 / 2)
x_1, y_1 = 0.9, 0
x_2, y_2 = 1, 1 / 0.9 * y_0
# 绘制圆
theta = np.linspace(0, 2 * np.pi, 100)
x_circle = x_c + r * np.cos(theta)
y_circle = y_c + r * np.sin(theta)

plt.plot(x_circle, y_circle, label="Circle")  # 画圆
plt.plot([0, x_2], [0, y_2])
plt.plot([x_1, x_0], [y_1, y_0])
plt.plot([0, 1], [0, 0])
plt.plot([1, x_2], [0, y_2])

plt.scatter(0, 0, label="$O$")
plt.text(0, 0, "$O$", verticalalignment='top', horizontalalignment='left')
plt.scatter(x_0, y_0, label="$A$")
plt.text(x_0, y_0, "$A$", verticalalignment='top', horizontalalignment='left')
plt.scatter(x_1, y_1, label="$B$")
plt.text(x_1, y_1, "$B$", verticalalignment='top', horizontalalignment='left')
plt.scatter(1, 0, label="$C$")
plt.text(1, 0, "$C$", verticalalignment='top', horizontalalignment='left')
plt.scatter(x_2, y_2, label="$D$")
plt.text(x_2, y_2, "$D$", verticalalignment='top', horizontalalignment='left')
plt.gca().set_aspect('equal', adjustable='box', )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.axis("off")
plt.savefig("./out/CircleSinTan.eps", format="eps", dpi=600)
plt.show()
