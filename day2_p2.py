#import numpy as np
#import matplotlib.pyplot as plt
#from mpl_toolkits import mplot3d
#
#
#np.set_printoptions(precision=2)
#
#a = np.linspace(start=-10, stop=10, num=200)
## print(a)
#
#b = np.linspace(start=-10, stop=10, num=200)
## print(b)
#
#x = np.linspace(start=-10, stop=10, num=100)
## print(x)
#
#mu, sigma = 0, 1
#s = np.random.normal(mu, sigma, 100)
#
#yi = 2 * x + 3 + s

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


np.set_printoptions(precision=2)

a = np.linspace(start=-10, stop=10, num=200)
# print(a)

b = np.linspace(start=-10, stop=10, num=200)
# print(b)

x = np.linspace(start=-10, stop=10, num=100)
# print(x)

mu, sigma = 0, 1
s = np.random.normal(mu, sigma, 100)

yi = 2 * x + 3 + s

yi_cap = 2 * x + 3

element_wise_error = (yi - yi_cap)

# print(element_wise_error)

# print(yi.tolist(),yi_cap.tolist(),element_wise_error.tolist())

# for i in range(100):
#        print(yi[i],yi_cap[i],element_wise_error[i])
#        print("\n")


avg_error = np.multiply(element_wise_error, element_wise_error)
avg_error = avg_error / 100

# print("Avg Error",avg_error)


yicap = []
yi_1 = []
p = 0
q = 0
r = 0

E = np.zeros((200, 200))
# a_list=list(a)
# b_list=list(b)
for i in range(200):
    p = p + 1
    for j in range(200):
        q = q + 1
        # for k in x:
        arr = a[i] * x + b[j]
        arr1 = a[i] * x + b[j] + np.random.normal(0, 1)
        arr3 = np.sum((arr - arr1) * (arr - arr1)) / 100
        #print(arr3)
        E[i][j] = arr3
        #print(E[i][j])

#         yi_1.append(arr1)
#         r=r+1
#         yicap.append(arr)

#print(np.shape(E))
#print(E)
# yi_1=np.array(yi_1)
# yicap=np.array(yicap)
# error2=(yi_1-yicap)*(yi_1-yicap)
# error3=np.sum(error2)/4000000


# print(yicap)


fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(a,b,E,cmap='viridis', edgecolor='none')
ax.set_title('Surface plot')
plt.show()
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('E')
yi_cap = 2 * x + 3

element_wise_error = (yi - yi_cap)
# print(element_wise_error)

# print(yi.tolist(),yi_cap.tolist(),element_wise_error.tolist())

# for i in range(100):
#        print(yi[i],yi_cap[i],element_wise_error[i])
#        print("\n")

avg_error = np.multiply(element_wise_error, element_wise_error)
avg_error = avg_error / 100
# print("Avg Error",avg_error)


yicap = []
yi_1 = []
p = 0
q = 0
r = 0

E = np.zeros((200, 200))
# a_list=list(a)
# b_list=list(b)
for i in range(200):
    p = p + 1
    for j in range(200):
        q = q + 1
        # for k in x:
        arr = a[i] * x + b[j]
        arr1 = a[i] * x + b[j] + np.random.normal(0, 1)
        arr3 = np.sum((arr - arr1) * (arr - arr1)) / 100
        #print(arr3)
        E[i][j] = arr3
        #print(E[i][j])

#         yi_1.append(arr1)
#         r=r+1
#         yicap.append(arr)

#print(np.shape(E))
#print(E)
# yi_1=np.array(yi_1)
# yicap=np.array(yicap)
# error2=(yi_1-yicap)*(yi_1-yicap)
# error3=np.sum(error2)/4000000


# print(yicap)


fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(a,b,E,cmap='viridis', edgecolor='none')
ax.set_title('Surface plot')
plt.show()
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('E')


plt.show()
