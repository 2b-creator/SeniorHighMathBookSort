import numpy as np
import matplotlib.pyplot as plt
font_title = {
    'family': 'Times New Roman',
    'weight': 'normal',
    'size': 20,
    'usetex': True,  # title 可以单独启用 usetex
}
# 定义两点 A 和 B
A = np.array([-1, 0])
B = np.array([1, 0])
plt.figure(figsize=(10,5))
# 定义比率 k
k_values = [0.5, 1.5, 2.0]  # 你可以选择多个不同的 k 值来绘制不同的阿波罗尼斯圆

# 绘制 A 和 B
plt.plot(A[0], A[1], 'ro', label='Point A')
plt.plot(B[0], B[1], 'bo', label='Point B')

# 为了不同的 k 值绘制不同的阿波罗尼斯圆
theta = np.linspace(0, 2 * np.pi, 400)

for k in k_values:
    # 阿波罗尼斯圆的中心和半径计算公式
    d = np.linalg.norm(A - B)  # A 和 B 之间的距离
    r = d / (k - 1)  # 半径
    center = (A + k * B) / (1 + k)  # 中心

    # 圆的参数方程
    x = center[0] + r * np.cos(theta)
    y = center[1] + r * np.sin(theta)

    plt.plot(x, y, label=f'Apollonian circle k={k}')

# 设置坐标轴等比例显示
plt.gca().set_aspect('equal', adjustable='box')

# 标注
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.grid(False)
plt.title("Apollonian Circles")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.savefig("./out/ApollonianCircles.eps",format="eps",dpi=600)
# 显示图形
plt.show()
