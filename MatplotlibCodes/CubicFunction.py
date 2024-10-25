import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(11, 6))
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "font.size": 14,
})
# 定义x的范围和精度
x = np.linspace(-2, 0.5, 1000)  # 从-1到2, 总共1000个点
slope = 3 * (-2 / 3) ** 2 + 4 * (-2 / 3) + 1
a = 1
b = 2
c = 1
d = 1
# 定义函数
y = a * x ** 3 + b * x ** 2 + c * x + d
z = slope * (x - (-2 / 3)) + (a * (-2 / 3) ** 3 + b * (-2 / 3) ** 2 + c * (-2 / 3) + d)
# 使用plot()函数绘制函数图像
plt.plot(x, y, color='blue', label=r"$y=x^3+2x^2+x+1$")
plt.plot(x, z, color="red", label="Tangent")
plt.scatter(-2 / 3, a * (-2 / 3) ** 3 + b * (-2 / 3) ** 2 + c * (-2 / 3) + d, color="navy", label="Middle point")
plt.text(-2 / 3, a * (-2 / 3) ** 3 + b * (-2 / 3) ** 2 + c * (-2 / 3) + d,
         r"$\displaystyle O\left ( -\frac{2}{3},f\left ( -\frac{2}{3} \right )  \right ) $", verticalalignment='top',
         horizontalalignment='right', fontsize=12)

plt.text(-1.9, 1.05, "I")
plt.text(-1, 1.5, "II")
plt.text(-1, 0.25, "III")
plt.text(0.25, 1, "IV")

plt.xlim(-2, 0.5)
plt.gca().set_aspect("equal")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
# 添加标题
plt.title(r'Function $f(x) =ax^3+bx^2+cx+d $')
# 去掉图形的上和右边框, 使其像数轴
plt.gca().spines['top'].set_color('none')
plt.gca().spines['right'].set_color('none')

# 将下和左边框与数轴对齐
plt.gca().spines['bottom'].set_position('zero')
plt.gca().spines['left'].set_position('zero')

# 去掉刻度线, 只保留主要的标记
plt.gca().xaxis.set_ticks_position('bottom')
plt.gca().yaxis.set_ticks_position('left')
# 显示图像
plt.savefig("./out/CubicFunction.eps", format="eps", dpi=600)
plt.show()
