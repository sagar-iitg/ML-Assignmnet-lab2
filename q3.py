import numpy as np

a=2
b=3

x = np.linspace(-10,11,100)

y=a*x+b

mu,sigma=0,1
noise=np.random.normal(mu,sigma,100)
#print("noise",noise)

y1=y+noise

M=np.zeros((100,2))

#print("M",M)
#print(M.shape)



M[:,0]=x  #1st column
M[:,1]=1  #2nd column

#print(M)

slope,intercept=np.linalg.pinv(M)@y1  #pseudo inverse 

print("a=",slope,"b=",intercept)







