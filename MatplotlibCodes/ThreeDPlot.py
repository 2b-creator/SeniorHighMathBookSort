import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.colors import Normalize
from numpy.ma.core import outer

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "font.size": 14,
})
font_title = {
    'family': 'Times New Roman',
    'weight': 'normal',
    'size': 20,
    'usetex': True,  # title 可以单独启用 usetex
}
# 创建图形和3D坐标轴
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 定义球体的经纬度线
u = np.linspace(0, 2 * np.pi, 100)  # 定义经度
v = np.linspace(0, np.pi, 100)  # 定义纬度

# 球体的参数方程
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))
# 选择颜色映射并使用Normalize来调整颜色范围
colormap = plt.cm.plasma  # 你可以替换为其他颜色映射
norm = Normalize(vmin=-1, vmax=1)  # 将z的范围映射到0到1
ax.plot_surface(x, y, z, rstride=3, cstride=3, facecolors=colormap(norm(z)), edgecolor='k', linewidth=0.5)
# 设置正交投影去除透视效果
ax.set_proj_type('ortho')
# 绘制球面网格
# ax.plot_wireframe(x, y, z, color='b', linewidth=0.5)

# 设置图形参数
ax.set_xlabel('$X$', font_title)
ax.set_ylabel('$Y$', font_title)
ax.set_zlabel('$Z$', font_title)
ax.set_title('Spherical Grid', font_title)
ax.set_aspect('equal')
plt.savefig("./out/Spherical_Grid.eps", format="eps", dpi=600)
plt.show()
