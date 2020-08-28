import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
x=np.linspace(start=-10,stop=10,num=100)

#y=2*x+3

mu,sigma=0,1
s=np.random.normal(mu,sigma,100)
#let a=0

y1=2*x+3+s


M=np.zeros((100,2))
M[:,0]=x  #1st column
M[:,1]=1 

a,b= np.linalg.pinv(M)@y1



#np.shape(mat_inverse)
print(a,b)