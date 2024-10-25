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
# 定义圆心和半径
x_c, y_c = 0, 0  # 圆心坐标
r = 5  # 圆的半径

# 定义圆外的点
x_0, y_0 = 8, 10

# 绘制圆
theta = np.linspace(0, 2*np.pi, 100)
x_circle = x_c + r * np.cos(theta)
y_circle = y_c + r * np.sin(theta)

# 计算切线的斜率
dx = x_0 - x_c
dy = y_0 - y_c
d = np.sqrt(dx**2 + dy**2)

# 计算切线的交点
l = r**2 / d
h = np.sqrt(r**2 - l**2)

# 第一条切线的交点
x_tangent1 = x_c + l * (x_0 - x_c) / d - h * (y_0 - y_c) / d
y_tangent1 = y_c + l * (y_0 - y_c) / d + h * (x_0 - x_c) / d

# 第二条切线的交点
x_tangent2 = x_c + l * (x_0 - x_c) / d + h * (y_0 - y_c) / d
y_tangent2 = y_c + l * (y_0 - y_c) / d - h * (x_0 - x_c) / d

# 计算切线的斜率
m1 = (y_tangent1 - y_0) / (x_tangent1 - x_0)
m2 = (y_tangent2 - y_0) / (x_tangent2 - x_0)

# 计算连接两个切点的直线斜率
m_between = (y_tangent2 - y_tangent1) / (x_tangent2 - x_tangent1)

# 定义直线方程
def tangent_line(m, x_0, y_0, x_range):
    return m * (x_range - x_0) + y_0

# 设定x的范围，用于延伸直线
x_range = np.linspace(-10, 20, 100)

# 绘制圆
plt.plot(x_circle, y_circle, label="Circle")  # 画圆
plt.scatter(x_0, y_0, color='red', label="Point")  # 画点
plt.text(x_0, y_0, f"$P(x_0,y_0)$",font_title, verticalalignment='top', horizontalalignment='left')

# 画切线，扩展为直线
plt.plot(x_range, tangent_line(m1, x_0, y_0, x_range), 'g-', label="Tangent 1")
plt.plot(x_range, tangent_line(m2, x_0, y_0, x_range), 'b-', label="Tangent 2")

# 标出切点
plt.scatter([x_tangent1, x_tangent2], [y_tangent1, y_tangent2], color='orange', zorder=5)
# 标出圆心
plt.scatter(x_c,y_c)
plt.text(x_c, y_c, f"$O$",font_title, verticalalignment='bottom', horizontalalignment='right')
# 添加切点注释
plt.text(x_tangent1, y_tangent1, f"$A$",font_title, verticalalignment='bottom', horizontalalignment='right')
plt.text(x_tangent2, y_tangent2, f"$B$",font_title, verticalalignment='top', horizontalalignment='left')

# 画出连接两个切点的直线
plt.plot(x_range, tangent_line(m_between, x_tangent1, y_tangent1, x_range), 'r--')

plt.gca().set_aspect('equal', adjustable='box',)
plt.axis("off")
plt.grid(True)
plt.xlim(-10, 20)
plt.ylim(-10, 20)
plt.legend()
plt.savefig("./out/TangentOfCircle.eps",format="eps",dpi=600)
plt.show()
