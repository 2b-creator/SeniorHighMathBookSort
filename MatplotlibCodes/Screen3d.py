import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "font.size": 14,
    })
# 创建球体的网格
phi, theta = np.mgrid[0:np.pi:30j, 0:2*np.pi:30j]
x = np.sin(phi) * np.cos(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(phi)

# 绘制球体
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='c', alpha=0.6, rstride=1, cstride=1, edgecolor='none')

# 选取侧面的一个四边形面
# 例如选取靠近 x 轴正方向的一个四边形
i, j = 17, 11  # 选取网格的某个中间位置，避免在顶端或底端
vertices = np.array([
    [x[i, j], y[i, j], z[i, j]],
    [x[i+1, j], y[i+1, j], z[i+1, j]],
    [x[i+1, j+1], y[i+1, j+1], z[i+1, j+1]],
    [x[i, j+1], y[i, j+1], z[i, j+1]]
])

# 连接面到球心形成四棱锥
for v in vertices:
    ax.plot([0, v[0]], [0, v[1]], [0, v[2]], color='r')

# 绘制四边形面
ax.add_collection3d(art3d.Poly3DCollection([vertices], color='r', alpha=0.5))

# 设置显示比例
ax.set_box_aspect([1,1,1])
plt.savefig("./out/GetOne.eps",format="eps",dpi=600)
plt.show()