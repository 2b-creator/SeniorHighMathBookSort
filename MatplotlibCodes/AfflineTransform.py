import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "font.size": 14,
})
font_title = {
    'family': 'Times New Roman',
    'weight': 'normal',
    'size': 15,
    'usetex': True,  # title 可以单独启用 usetex
}
# 椭圆参数
a, b = 3, 1

# 生成椭圆的参数化方程
theta = np.linspace(0, 2 * np.pi, 100)
x = a * np.cos(theta)
y = b * np.sin(theta)

# 仿射变换矩阵（将椭圆变成半径为1的圆）
transform_matrix = np.array([[1 / a, 0], [0, 1 / b]])

# 椭圆的点进行仿射变换
transformed_points = np.dot(transform_matrix, np.vstack((x, y)))

# 画图
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# 左图：原始椭圆
ax[0].plot(x, y, label=r"Ellipse $\displaystyle \frac{x^2}{9}+y^2=1$")
ax[0].set_title("Ellipse")
ax[0].set_aspect('equal')
ax[0].grid(True)
ax[0].legend()

# 右图：仿射变换后的圆
ax[1].plot(transformed_points[0], transformed_points[1],
           label=r"Transformed Circle $\displaystyle x'=\frac{1}{3}x,y'=y$")
ax[1].set_title("Transformed Circle")
ax[1].set_aspect('equal')
ax[1].grid(True)
ax[1].legend()

plt.tight_layout()
plt.savefig("./out/AffineTransform.eps", format="eps", dpi=600)
plt.show()
