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

plt.plot((0, -5), (2, 0), color="black")
plt.text(0, 2.1, "$A$", font_title, color="black")
plt.text(-5.3, -0.3, "$B$",font_title, color="black")
plt.plot((0, -1), (2, 0), color="black")
plt.text(-1.2, -0.3, "$D$",font_title, color="black")
plt.plot((0, 2), (2, 0), color="black")
plt.text(2, -0.3, "$C$",font_title, color="black")
plt.plot((-5, 2), (0, 0), color="black")
plt.ylim(-1, 3)
plt.xlim(-6, 3)
plt.axis("off")
plt.show()
