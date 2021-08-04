import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

file_path = "C:/Users/10269/Desktop/Paper writing2/Experiment/EXP_3/3D/3D.csv"
df = pd.read_csv(file_path)
df = df.loc[df["interval_begin"] >= 1000]
df = df.loc[df["interval_begin"] <= 4450]
print(df)

fig = plt.figure()
ax = Axes3D(fig)

# 数据录入
x1 = 1000
array_1 = []
while x1 <= 4450:
    array_1.append(x1)
    x1 = x1 + 50
X = array_1

y1 = 1
array_2 = []
while y1 <= 60:
    # 这里小于等于的60是探测器的数目
    juli = (y1-1)*50 + 6800
    array_2.append(juli)
    y1 = y1 + 1
Y = array_2

X, Y = np.meshgrid(X, Y)
print("网格化后的X=",X)
print("X维度信息",X.shape)
print("网格化后的Y=",Y)
print("Y维度信息", Y.shape)

df1 = df.loc[df.interval_begin == 1000]
Z = np.array(df1.interval_speed)
i = 1050
while i <= 4450:
    df2 = df.loc[df.interval_begin == i]
    A = np.array(df2.interval_speed)
    Z = np.vstack((Z, A))
    i = i + 50
print(Z)
print("维度调整前的Z轴数据维度",Z.shape)
Z = Z.T
print("维度调整后的Z轴数据维度",Z.shape)

# 绘制三维曲面图
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
#设置三个坐标轴信息
ax.set_xlabel('Time(s)', color='b')
ax.set_ylabel('Location (m)', color='g')
ax.set_zlabel('Speed(m/s)', color='r')

# ax.set_zlim(0, 12)
ax.view_init(28, -63 )  # 第一个参数是高度，第二个参数是顺时针旋转角度(elev=elev,azim=azim),这个在最后的图中可以调整
plt.gca().invert_zaxis()
# plt.gca().invert_xaxis()


# 添加colorbar,需要有surf
fig.colorbar(surf, shrink=0.5, aspect=20, orientation='horizontal')
plt.show()
