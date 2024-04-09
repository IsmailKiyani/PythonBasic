import numpy as np

my_arr = np.arange(100000)

my_list = list(range(10000))


%time for _ in range(6): my_arr2 = my_arr * 2

 %time for _ in range(10): my_list2 = [x * 2 for x in my_list]

"""### Multidimenssion array"""
data = np.random.randn(3,2)
data

mul =data *10
mul

addd = data + data
addd

data.shape

data.dtype

data1 = [6,7.5,8,0,1]

arr1=np.array(data1)
arr1

data2 = np.array([[1,2,3,4],[5,6,7,8]])

print(data2)
print(data2.shape)
print(data2.ndim)
print(data2.dtype)

np.zeros(10)

np.zeros((3,6))

np.empty((2,3,2))

np.arange(15)

arrid=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])

print(arrid)
print(arrid.shape)
print(arrid.ndim)

arrid[0:1,1:,:2]

"""## Data type for ndarrays"""

arr1 = np.array([1,2,4], dtype=np.float64)

arr2 = np.array([1,2,4], dtype=np.int32)

print(arr1.dtype)
print(arr2.dtype)

arr = np.array([1,2,3,4])

arr.dtype

float_arr = arr.astype(np.float64)

float_arr.dtype

"""##  Arthmetic with NumPy array"""

arr = np.array([[1,2,3],[4,5,6]])

arr

arr + arr

arr * arr

arr -arr

arr / arr

arr ** 0.5

arr2 = np.array([[0,4,1],[7,2,12]])
print(arr)
print(arr2)

arr2 > arr

"""### Indexing and Slicing"""

arr = np.arange(10)
arr

arr[5]

arr[5:8]

arr[5:8] = 12
arr

arr_slice = arr[5:8]
arr_slice

arr_slice[1] = 12345
arr_slice

arr_slice[:]=64
arr_slice

arr

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2d

arr2d[2]

arr2d[0][2]

arr3d= np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3d)
print(arr3d.shape)
print(arr3d.ndim)
print(arr.item)

arr3d[0]

old_value = arr3d[0].copy()
old_value

arr3d[0]=42
arr3d

arr3d[0] = old_value
arr3d

arr3d[1,0]

x=arr3d[1]
x

arr

arr[1:6]

arr2d

arr2d[:2]

arr2d[:2,1:]

arr2d[1,:2]

arr2d[:,:1]

"""## Boolean indexing"""

names = np.array(['Bob','Joe','Will','Joe','Joe'])
names

data = np.random.randn(7,4)
data

names == 'Joe'

data[names == 'Bob']

data[names == 'Bob',2:]

data[names == 'Bob',3]

data[~(names == 'Bob')]

mask = (names == 'Bob') | (names == 'will')

mask

names

"""## Fancy indexing"""

arr = np.arange(15).reshape(3,5)
arr

arr.T

arr = np.random.randn(6,3)
arr

np.dot(arr.T,arr)

arr=np.arange(16).reshape((2,2,4))
arr

arr.transpose(1,0,2)
arr

arr.swapaxes(1,2)

from math import sin

x=3.14
y=sin(x)
print(y)

from math import sin, cos

x=3.14
y=sin(x)
print(y)
y=cos(x)
print(y)

from math import *

x=3.14
y=sin(x)
print(y)
y=cos(x)
print(y)

import math

x=3.14
y=sin(x)
print(y)
y=cos(x)
print(y)

"""## Matplotlib"""

import matplotlib as plt

x=3
y=np.sin(x)
print(y)

x=3
y=math.sin(x)
print(y)
y=np.sin(x)
print(y)

from matplotlib.pyplot import *
x=[1,2,3,4,5,6,7,8,9,10]
y=[5,2,4,4,8,7,4,8,10,9]
plot(x, y)
xlabel('Time (s)')
ylabel('Temprature (degC)')
show()

x = [1, 2, 3]
y = [1, 4, 9]
z = [10, 5, 0]
plot(x, y)
plot(x, z)
title("test plot")
xlabel("x")
ylabel("y and z")
legend(["this is y", "this is z"])
show()

import matplotlib.pyplot as plt

x=[0,1,2,3,4,5,6,7]
y=np.sin(x)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('Y')
plt.show()

xsart = 0
xstop = 2*np.pi
increment =0.1
x=np.arange(xsart, xstop, increment)
y=np.sin(x)
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

"""## Broadcasting"""

arr = np.arange(5)
arr

arr * 4

arr = np.random.randn(4, 3)
arr

arr.mean(0)

demeaned = arr - arr.mean(0)
demeaned

demeaned.mean(0)

arr

row_mean =arr.mean(1)
row_mean
row_mean.shape

row_mean.reshape((4,1))

demeaned = arr - row_mean.reshape((4,1))
demeaned

arr = np.zeros((4,3))
arr

arr[:] = 5
arr

col = np.array([1.28, -.42, .44, 1.6])
col

arr[:] =col[:, np.newaxis]
arr

arr[:2]=[[-1.37],[.509]]
arr

arr = np.arange(10)
arr

np.sqrt(arr)

np.exp(arr)

x = np.random.randn(8)
y = np.random.randn(8)
print(x)
print(y)

np.maximum(x,y)

np.random.randn(7) * 5

remainder, whole_part = np.modf(arr)
print(remainder)
print(whole_part)

points = np.arange(-5, 5, 0.01) #1000 equally spaced points
xs, ys = np.meshgrid(points, points)
ys
z=np.sqrt(xs ** 2 + ys ** 2)
z

plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()

plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")

"""## Sorting"""

arr = np.random.randn(6)
arr

arr.sort()
arr

arr =np.random.randn(5,3)
arr

arr.sort(1)
arr

large_arr = np.random.randn(1000)

large_arr.sort()

large_arr[int(0.05 * len(large_arr))] # 5% quantile

"""## Unique and other set logic:"""

names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
names

np.unique(names)

ints =np.array([3,3,3,2,2,2,1,1,1,4,4])
ints

np.unique(ints)

sorted(set(names))