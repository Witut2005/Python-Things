import random
import numpy as np

arr = np.array([1, 2, 3])
other = np.array([4, 5, 6])

print(arr.dot(other))

print(arr.sum())

arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d[0][:], "\n")

arr2d = arr2d.reshape(3, 2)
print(arr2d.shape)
print(arr2d[0][:])

# problem1 https://www.youtube.com/watch?v=QUT1VHiLmmIo

arrpr1 = np.full([5, 5], 1)
arrpr2 = np.full([3, 3], 0)
arrpr2[1][1] = 9

arrpr1[1:4, 1:4] = arrpr2[:4, :4]

arrc = np.array([1, 2, 3])
arrc1 = np.array(arrc)
print(arrpr1, "\n")

arrc1[0] = 4

arrc2 = arrc[arrc > 1]

print(arrc)
print(arrc1)
print(arrc2)
