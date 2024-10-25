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
x = np.linspace(-10, 10, 1000)  # 从-1到2，总共1000个点
e_x = np.exp(x)
ln_x = np.log(x)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.plot(x, e_x, label=r"$y=e^x$")
plt.plot(x, ln_x, label=r"$y=\ln x$")
plt.plot(x, x + 1, label=r"$y=x+1$")
plt.plot(x, x - 1, label=r"$y=x-1$")
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
plt.title(r"$e^x$ and $\ln x$ tangent")
plt.savefig("./out/LogExFunction.eps", format="eps", dpi=600)
plt.show()
