import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "font.size": 14,
})
# 定义椭圆的参数
a = 5  # 长半轴
c = 3  # 焦点到原点的距离
b = np.sqrt(a ** 2 - c ** 2)  # 短半轴

# 创建椭圆的角度
theta = np.linspace(0, 2 * np.pi, 1000)

# 计算椭圆上点的坐标
x = a * np.cos(theta)
y = b * np.sin(theta)

# 创建图像
plt.figure(figsize=(8, 8))

# 绘制椭圆
plt.plot(x, y, label=r"$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$")

# 绘制焦点
plt.plot([c, -c], [0, 0], 'ro', label="Foci (F, F')")

# 绘制直线
plt.axvline(x=a ** 2 / c, color='g', linestyle='--', label="Line $l$")

# 添加x和y数轴
plt.axhline(y=0, color='black', linewidth=1)  # x轴
plt.axvline(x=0, color='black', linewidth=1)  # y轴

# 设置x轴和y轴范围
plt.xlim(-9, 9)
plt.ylim(-9, 9)

# 去掉图形的上和右边框，使其像数轴
plt.gca().spines['top'].set_color('none')
plt.gca().spines['right'].set_color('none')

# 将下和左边框与数轴对齐
plt.gca().spines['bottom'].set_position('zero')
plt.gca().spines['left'].set_position('zero')

# 去掉刻度线，只保留主要的标记
plt.gca().xaxis.set_ticks_position('bottom')
plt.gca().yaxis.set_ticks_position('left')

# 设置长宽比例
plt.gca().set_aspect('equal', adjustable='box')

# 将图例移到图像外部右侧
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# 添加标题和坐标轴标签
plt.title("Ellipse with Foci")

# 去掉网格
plt.grid(False)

# 调整图像的布局，使图例不会被裁剪
plt.tight_layout()
plt.savefig("./out/ConicSection2Define.eps", format="eps", dpi=600)
# 显示图像
plt.show()
