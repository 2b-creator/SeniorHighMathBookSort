import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(11, 6))
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "font.size": 14,
})
x = np.linspace(-5, 2, 1000)  # 从-1到2，总共1000个点
x_1, y_1 = 1, np.exp(1)
x_0, y_0 = -2, np.exp(-2)
x_m, y_m, y_em = (x_1 + x_0) / 2, (y_1 + y_0) / 2, np.exp((x_1 + x_0) / 2)
slp = (y_1 - y_0) / (x_1 - x_0)
b = y_0 - slp * x_0
z = (y_1 - y_0) / (x_1 - x_0) * x + b
y = np.exp(x)
plt.plot(x, y)
plt.plot(x, z)
plt.scatter(x_0, y_0, label="$A(x_0,y_0)$")
plt.text(x_0, y_0, "A", verticalalignment='top', horizontalalignment='left')
plt.scatter(x_1, y_1, label="$B(x_1,y_1)$")
plt.text(x_1, y_1, "B", verticalalignment='top', horizontalalignment='left')
plt.scatter(x_m, y_m, label=r"$\displaystyle C(\frac{x_0+x_1}{2},\frac{y_0+y_1}{2})$")
plt.text(x_m, y_m, "C", verticalalignment='top', horizontalalignment='left')
plt.scatter(x_m, y_em, label=r"$\displaystyle D(\frac{x_0+x_1}{2},e^{ \frac{x_1+x_2}{2}})$")
plt.text(x_m, y_em, "D", verticalalignment='top', horizontalalignment='left')
plt.title(r"Concave function of $f(x)=e^x$")
plt.plot([x_m, x_m], [y_m, y_em], linestyle="--")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
# 去掉图形的上和右边框，使其像数轴
plt.gca().spines['top'].set_color('none')
plt.gca().spines['right'].set_color('none')

# 将下和左边框与数轴对齐
plt.gca().spines['bottom'].set_position('zero')
plt.gca().spines['left'].set_position('zero')

# 去掉刻度线，只保留主要的标记
plt.gca().xaxis.set_ticks_position('bottom')
plt.gca().yaxis.set_ticks_position('left')
plt.gca().set_aspect("equal")
plt.savefig("./out/ConcaveFunctionIntro.eps", format="eps", dpi=600)
plt.show()
