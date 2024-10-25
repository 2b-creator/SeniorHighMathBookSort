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
x = np.linspace(-2, 10, 1000)  # 从-1到2, 总共1000个点
x_0, y_0 = 5, np.log(5)
x_1, y_1 = 0.25, np.log(0.25)
x_m, y_m, y_lm = (x_0 + x_1) / 2, (y_0 + y_1) / 2, np.log((x_0 + x_1) / 2)
y = np.log(x)
slp = (y_1 - y_0) / (x_1 - x_0)
b = y_0 - slp * x_0
z = (y_1 - y_0) / (x_1 - x_0) * x + b
plt.scatter(x_0, y_0)
plt.scatter(x_1, y_1)
plt.scatter(x_m, y_m, color="red", label="Middle of AB")
plt.text(x_m, y_m, r"$\displaystyle \frac{f\left ( \displaystyle  \frac{1}{4} \right ) +f\left ( 5 \right ) }{2} $",
         verticalalignment='top', horizontalalignment='left', color='red')
plt.scatter(x_m, y_lm, color="navy")
plt.plot([x_m, x_m], [y_m, y_lm], linestyle="--")
plt.text(x_m, y_lm, r"$\displaystyle f\left ( \frac{\displaystyle  \frac{1}{4}+5 }{2}  \right ) $",
         verticalalignment='bottom', horizontalalignment='right', color='navy')
plt.text(x_0, y_0, r"$A(5,\ln 5)$", verticalalignment='top', horizontalalignment='left')
plt.text(x_1, y_1, r"$\displaystyle B(\frac{1}{4},-2\ln 2)$", verticalalignment='top', horizontalalignment='left')

plt.plot(x, y, label=r"$f(x)=\ln x$")
plt.plot(x, z)
plt.title(r"Convex function of $f(x)=\ln x$")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
# 去掉图形的上和右边框, 使其像数轴
plt.gca().spines['top'].set_color('none')
plt.gca().spines['right'].set_color('none')

# 将下和左边框与数轴对齐
plt.gca().spines['bottom'].set_position('zero')
plt.gca().spines['left'].set_position('zero')

# 去掉刻度线, 只保留主要的标记
plt.gca().xaxis.set_ticks_position('bottom')
plt.gca().yaxis.set_ticks_position('left')
plt.gca().set_aspect("equal")
plt.savefig("./out/ConvexFunctionIntro.eps", format="eps", dpi=600)
plt.show()
