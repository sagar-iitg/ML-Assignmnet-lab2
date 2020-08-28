import numpy as np
from mpl_toolkits.mplot3d import Axes3D
# Axes3D import has side effects, it enables using projection='3d' in add_subplot
import matplotlib.pyplot as plt

x = np.linspace(-10, 11, 100)
e = np.zeros((44100))
a = b = np.arange(-10,11,step=0.1)
y=2*x+3


def fun(a, b):
    for i in range(44100):
        yt = a[i] * x + b[i]

        normal_dp = np.random.normal(0, 1, size=100)
        y1 = yt + normal_dp
        e1 = (y - y1) ** 2


        e[i] = np.sum(e1) /100

    return e

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
X, Y = np.meshgrid(a, b)
zs = np.array(fun(np.ravel(X), np.ravel(Y)))
#print(zs.shape)
#print(X.shape,Y.shape)
Z = zs.reshape(X.shape)
#print(Z.shape,Z)
#print(X,np.ravel(X), Y,np.ravel(Y))
ax.plot_surface(X, Y, Z,cmap='viridis',linewidth=0)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()