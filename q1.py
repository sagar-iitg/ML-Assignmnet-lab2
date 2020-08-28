import numpy as np
import matplotlib.pyplot as plt
a=2
b=3

x = np.linspace(-10,11,100)

y=a*x+b
plt.plot(x, y, linestyle='solid',color='Black')
normal_dp=np.random.normal(0,1,size=100)
y1=y+normal_dp
plt.plot(x,y1,"r.")
plt.show()


