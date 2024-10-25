import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from PIL.ImageOps import scale

font_title = {
    'family': 'Times New Roman',
    'weight': 'normal',
    'size': 20,
    'usetex': True,  # title 可以单独启用 usetex
}

plt.quiver(0, 0, 4, 0, angles='xy', scale=1, scale_units="xy", color="orange")  # 向量 a
plt.text(2, 2, "$P$", font_title, color="red")
plt.quiver(0, 0, 2, 2, angles='xy', scale=1, scale_units="xy", color="red")  # 向量 b
plt.text(-0.3, -0.3, "$O$", font_title, color="black")
plt.quiver(0, 0, 3, 1, angles='xy', scale=1, scale_units="xy", color="navy")  # 向量 b
plt.text(3, 1, "$A$", font_title, color="navy")
plt.text(4, 0, "$B$", font_title, color="orange")

plt.text(-0.5, 2.5, "$a+b=1$", font_title, color="black")
# 修改 plt.plot() 参数，使直线从 a 的终点到 a+b 的终点
plt.axline((4, 0), (2, 2))
plt.axline((5, 1), (3, 3), ls="-.")
plt.text(3.5, 2.5, "$a+b=x$", font_title, color="black")
plt.quiver(0, 0, 4, 2, angles='xy', scale=1, scale_units="xy", color="red")
plt.text(4, 2, "$P'$", font_title, color="red")
plt.ylim(-1, 3)
plt.xlim(-1, 7)
plt.axis("off")
plt.show()
