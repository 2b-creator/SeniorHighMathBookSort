import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "font.size": 14,
})
# 设置图形
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# 1. 抛物线的光学性质
a = 1
focus = (0, 1/(4*a))
directrix_y = -1/(4*a)
x_parabola = np.linspace(-5, 5, 400)
y_parabola = a * x_parabola**2

axs[0].plot(x_parabola, y_parabola, label="Parabola")
axs[0].scatter(*focus, color='red', label='Focus (F)', zorder=5)
axs[0].axhline(directrix_y, color='green', linestyle='--', label="Directrix")

ray_x = np.array([-2, 0, 2])
ray_y = np.full_like(ray_x, focus[1])
ray_reflected_y = np.linspace(focus[1], 5, 100)
for xi in ray_x:
    axs[0].plot([focus[0], xi], [focus[1], a * xi**2], color='orange', linestyle='--')
    axs[0].plot([xi, xi], [a * xi**2, 5], color='blue', linestyle=':')

axs[0].set_xlim(-5, 5)
axs[0].set_ylim(-2, 5)
axs[0].set_aspect('equal', adjustable='box')
axs[0].set_title("Parabola")
axs[0].legend()

# 2. 椭圆的光学性质
a = 4
b = 3
focus1_ellipse = (-np.sqrt(a**2 - b**2), 0)
focus2_ellipse = (np.sqrt(a**2 - b**2), 0)
theta = np.linspace(0, 2*np.pi, 400)
x_ellipse = a * np.cos(theta)
y_ellipse = b * np.sin(theta)

axs[1].plot(x_ellipse, y_ellipse, label="Ellipse")
axs[1].scatter(*focus1_ellipse, color='red', label='Focus 1 (F1)', zorder=5)
axs[1].scatter(*focus2_ellipse, color='blue', label='Focus 2 (F2)', zorder=5)

# 模拟光线反射
ray_x_ellipse = np.array([-2, 0, 2])
for xi in ray_x_ellipse:
    y_ray = np.sqrt((1 - (xi**2 / a**2)) * b**2)
    axs[1].plot([focus1_ellipse[0], xi], [focus1_ellipse[1], y_ray], color='orange', linestyle='--')
    axs[1].plot([xi, focus2_ellipse[0]], [y_ray, focus2_ellipse[1]], color='blue', linestyle=':')

axs[1].set_xlim(-5, 5)
axs[1].set_ylim(-4, 4)
axs[1].set_aspect('equal', adjustable='box')
axs[1].set_title("Ellipse")
axs[1].legend()

# 3. 双曲线的光学性质
a = 3
b = 2
focus1_hyperbola = (-np.sqrt(a**2 + b**2), 0)
focus2_hyperbola = (np.sqrt(a**2 + b**2), 0)
x_hyperbola = np.linspace(-5, 5, 400)
y_hyperbola_pos = b/a * np.sqrt(x_hyperbola**2 - a**2)
y_hyperbola_neg = -y_hyperbola_pos

axs[2].plot(x_hyperbola, y_hyperbola_pos, label="Hyperbola")
axs[2].plot(x_hyperbola, y_hyperbola_neg)
axs[2].scatter(*focus1_hyperbola, color='red', label='Focus 1 (F1)', zorder=5)
axs[2].scatter(*focus2_hyperbola, color='blue', label='Focus 2 (F2)', zorder=5)

# 模拟光线反射
ray_x_hyperbola = np.array([4, 5])
for xi in ray_x_hyperbola:
    y_ray = b/a * np.sqrt(xi**2 - a**2)
    axs[2].plot([focus1_hyperbola[0], xi], [focus1_hyperbola[1], y_ray], color='orange', linestyle='--')
    axs[2].plot([xi, xi + 1], [y_ray, y_ray + 1], color='blue', linestyle=':')

axs[2].set_xlim(-6, 6)
axs[2].set_ylim(-5, 5)
axs[2].set_aspect('equal', adjustable='box')
axs[2].set_title("Hyperbola")
axs[2].legend()

# 显示图像
plt.tight_layout()
plt.savefig("./out/ConicCurveLightAttribute.eps", format="eps", dpi=600)
plt.show()
