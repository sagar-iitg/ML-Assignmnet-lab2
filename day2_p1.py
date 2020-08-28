import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
a=2
b=3
x=np.linspace(start=-10,stop=10,num=100)
#print(x)
y=a*x+b
#print(y)
plt.plot(x,y,color='black')
mu,sigma=0,1
s=np.random.normal(mu,sigma,100)
#print("random points",s)
y1=2*x+3+s
#print(y1)
plt.scatter(x,y1,color='red')
plt.show()