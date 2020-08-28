import numpy as np
from mpl_toolkits.mplot3d import Axes3D
# Axes3D import has side effects, it enables using projection='3d' in add_subplot
import matplotlib.pyplot as plt
a0=0
b0=0
initial_values=[-9,8]
alpha=1
out_arr= [initial_values.copy()]
print(out_arr)

a=2
b=3

x = np.linspace(-10,11,100)

y=a*x+b
normal_dp=np.random.normal(0,1,size=100)
y1=y+normal_dp
computed_values=[0,0]
iteration=500e100
n=0
beta=0.9
delf=1
err= 500e100
olderr=derr=err
def fun(a, b):

        yt = a * x + b
        e1 = (y1 - yt) ** 2


        e = np.sum(e1) /100

        return e
print(out_arr)
while((derr)>=1.0e-4 and alpha>=1.0e-2):
    print(out_arr)
    for i in range(x.shape[0]):
        for j in range(2):
            ct=x[i]
            if j==1:
                ct=1
            yt=initial_values[0]*x[i]+initial_values[1]
            delf2=0.02 * (y1[i] - yt) * x[i]
            delf1=0.02 * (y1[i] - yt) * ct
            initial_values[j]=initial_values[j]+alpha*delf1

    print(out_arr,"im her")
    cerr=fun(initial_values[0],initial_values[1])

    err = min(err, cerr)
    if err<=olderr:
        derr = olderr - err
    olderr=err


    delf
    n+=1
    if fun(initial_values[0]-delf2,initial_values[1]-delf1)>\
            cerr-alpha/2*(abs(delf1)+abs(delf2))**2:
        alpha=alpha*beta

    """    if cerr>\
            cerr-beta/2*(abs(delf1)+abs(delf2))**2:
        alpha=alpha*beta
        """
    print(derr)
    print(n,alpha)
    print(delf1,delf2)
    print(out_arr,"here",)
    templist=[initial_values[0],initial_values[1]]
    out_arr.append(templist)
    print(initial_values)

print(out_arr)

#x = np.linspace(-10, 11, 100)
e = np.zeros((44100))
a = b = np.arange(-10,11,step=0.1)
#y=2*x+3

def fun(a, b):
    for i in range(44100):
        yt = a[i] * x + b[i]

        normal_dp = np.random.normal(0, 1, size=100)
        y1 = yt + normal_dp
        e1 = (y - y1) ** 2


        e[i] = np.sum(e1) /100

    return e

fig = plt.figure(figsize=[20,20],dpi=150)
ax = fig.add_subplot()
X, Y = np.meshgrid(a, b)
zs = np.array(fun(np.ravel(X), np.ravel(Y)))
#print(zs.shape)
#print(X.shape,Y.shape)
Z = zs.reshape(X.shape)
#print(Z.shape,Z)
#print(X,np.ravel(X), Y,np.ravel(Y))
ax.contour(X, Y, Z,cmap='viridis',levels=30)

#out_arr=[[10, -8], [0.9754337587679227, 5.39993674117442], [1.3313989394919574, 4.463947219077937], [1.6271797205036425, 3.8954664859642265], [1.7997264474957515, 3.5417257181380415], [1.8913635326251763, 3.319839170719737], [1.9381004889946665, 3.179479111422788], [1.9619334783470175, 3.089631716359583], [1.9748841291095216, 3.031253857186406], [1.9830331581088754, 2.992698902743374], [1.989237992349129, 2.9668423599679863], [1.9909757529293781, 2.9477530047655938]]
zo=np.array(out_arr)
#out_arr.append([10,8])
#out_arr.reverse()
plt.plot(zo[:,0],zo[:,1],'xb-')
print(out_arr[:][0])
plt.show()