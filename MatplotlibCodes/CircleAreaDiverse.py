import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "font.size": 14,
})
# 定义大圆的半径r和小圆的半径r - Δr
r = 5  # 大圆的半径
delta_r = 1  # Δr
r_small = r - delta_r  # 小圆的半径

# 创建角度数组, 用于绘制圆
theta = np.linspace(0, 2 * np.pi, 100)

# 计算大圆和小圆的x, y坐标
x_large_circle = r * np.cos(theta)
y_large_circle = r * np.sin(theta)

x_small_circle = r_small * np.cos(theta)
y_small_circle = r_small * np.sin(theta)

# 重新绘制圆并标出两个圆的半径, 同时去除坐标轴
plt.figure(figsize=(11,6))

# 绘制大圆和小圆
plt.plot(x_large_circle, y_large_circle, label=f'Large Circle (r={r})', color='blue')
plt.plot(x_small_circle, y_small_circle, label=f'Small Circle (r={r_small})', color='green')

# 在圆上添加半径的标注线及文字
plt.plot([0, r], [0, 0], 'blue', linestyle='--')  # 大圆半径线
plt.text(r/2, 0.2, f'r = {r}', color='blue', fontsize=12)

plt.plot([0, r_small], [0, 0], 'green', linestyle='--')  # 小圆半径线

# 设置图形的比例, 使圆形不会被拉伸成椭圆
plt.gca().set_aspect('equal')

# 去除坐标轴
plt.axis('off')

# 添加图例和标题
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.title(f'Circles with Radius r={r} and $r-\Delta r$={r_small}')
plt.savefig("./out/CircleAreaDiverse.eps", format="eps", dpi=600)
# 显示图形
plt.show()

