
import numpy as np


x1=np.linspace(start=-10,stop=10,num=100)
y1=np.linspace(start=-10,stop=10,num=100)

x, y = np.meshgrid(x1, y1)



z1=1.7*np.exp(-((x-3)**2/10+(y-3)**2/10))
z2=np.exp(-((x+5)**2/8+(y+5)**2/8))
z3=2*np.exp(-((x)**2/4+(y)**2/5))
z4=1.5*np.exp(-((x-4)**2/18+(y+4)**2/16))
z5=1.2*np.exp(-((x+4)**2/18+(y-4)**2/16))
z=z1+z2+z3+z4+z5
print(z)
len(z)



import matplotlib.pyplot as plt

plt.figure()
cp = plt.contour(x, y, z, colors='black', linestyles='dashed')
plt.clabel(cp, inline=True,
          fontsize=10)
plt.title('Contour Plot')
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')


from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z)
plt.show()