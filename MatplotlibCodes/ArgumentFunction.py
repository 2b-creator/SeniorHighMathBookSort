import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from PIL.ImageOps import scale
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
plt.quiver(-5, 0, 10, 0, angles='xy', scale=1, scale_units="xy", color="black")  # 向量 b
plt.quiver(0, -5, 0, 10, angles='xy', scale=1, scale_units="xy", color="black")  # 向量 b
plt.quiver(1, 1, 3, 3, angles='xy', scale=1, scale_units="xy", color="orange")  # 向量 b
plt.text(5, -0.5, "$x$", font_title)
plt.text(0.3, 5, "$y$", font_title)
plt.text(2, 2.7, "$\overrightarrow{v}$", font_title,color="orange")
plt.scatter(0.8, -1.2, color="navy")
plt.scatter(3.2, 1.2, color="navy")
plt.axline((2, 0), (0, -2), color="navy")

plt.text(0.9, -2, "$P_0(x_0,y_0)$", font_title)
plt.text(-0.8, -0.8, "$O$", font_title)
plt.text(3.2, 0.6, "$P(x,y)$", font_title)
plt.text(-2, -4.6, "$M$", font_title,color="navy")
plt.text(5, 2.4, "$N$", font_title,color="navy")
ax = plt.gca()
ax.set_aspect(1)
plt.ylim(-5, 5)
plt.xlim(-5, 5)

plt.axis("off")

fig = plt.gcf()
fig.savefig("./out/ArgumentFunctions.eps",format="eps",dpi=600)
plt.show()