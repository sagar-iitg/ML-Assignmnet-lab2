import numpy as np
from mpl_toolkits.mplot3d import Axes3D
# Axes3D import has side effects, it enables using projection='3d' in add_subplot
import matplotlib.pyplot as plt

x = np.linspace(-10, 11, 100)
e = np.zeros((44100))
a = b = np.arange(-10,11,step=0.1)
y=2*x+3

def fun(x, y):

    z=1.7*np.exp(-((x-3)**2/10+(y-3)**2/10))+ \
      np.exp(-((x + 5) ** 2 / 8 + (y + 5) ** 2 / 8))+ \
         2 * np.exp(-((x) ** 2 / 4 + (y) ** 2 / 5))+\
            1.5* np.exp(-((x-4)**2/18+(y+4)**2/16))+\
                1.2*np.exp(-((x+4)**2/18+(y-4)**2/16))

    return z


fig = plt.figure(1)
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
fig2 = plt.figure(2)
ax2 = fig2.add_subplot()
ax2.contour(X, Y, Z,cmap='viridis',levels=50)
plt.show()


