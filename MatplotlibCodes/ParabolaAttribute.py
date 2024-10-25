import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "font.size": 14,
})
# 定义参数
p = 1  # 可以根据需要调整这个值
x0 = 1  # P 点的 x 坐标
y0 = np.sqrt(2 * p * x0)  # 根据抛物线方程计算 y 坐标

# 计算 P 点
P = (x0, y0)
F = (p/2, 0)  # 焦点 F
# 计算 PT = PF 的长度
distance = np.sqrt((P[0] - F[0])**2 + (P[1] - F[1])**2)
T_x = -p/2  # 准线的 x 坐标
T_y = P[1]  # T 点的 y 坐标与 P 点相同

# 确保 PT = PF
T = (T_x, T_y)

# 绘制抛物线
x = np.linspace(-1, 3, 400)
y = np.sqrt(2 * p * x)
y_neg = -y
plt.plot(x, y, label=r'$y^2=2px$', color='blue')
plt.plot(x, y_neg, color='blue')

# 绘制 P, F, T
plt.plot(P[0], P[1], 'ro', label='Point P')
plt.plot(F[0], F[1], 'go', label='Focus F')
plt.plot(T[0], T[1], 'bo', label='Point T')
plt.axvline(x=-p/2, color='orange', linestyle='--', label='Directrix')

# 标注
plt.text(P[0], P[1], ' P', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
plt.text(F[0], F[1], ' F', fontsize=12, verticalalignment='top', horizontalalignment='right')
plt.text(T[0], T[1], ' T', fontsize=12, verticalalignment='top', horizontalalignment='left')

# 画线段 PF 和 PT
plt.plot([P[0], F[0]], [P[1], F[1]], 'r', label='PF')
plt.plot([P[0], T[0]], [P[1], T[1]], 'b', label='PT')

# 设置坐标轴和图例
plt.xlim(-1.5, 3)
plt.ylim(-2, 2)
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Parabola with Points P, F, and T')
plt.legend()
plt.savefig("./out/ParabolaFocusRadius.eps", format="eps", dpi=600)
plt.show()
