
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

def main():
    ion()
    plt.show(block=True)

    arr = np.array([1,2,3,4,5], dtype=float)
    print(arr)
    print(arr.dtype)

    arr_dim = np.array([[1,2,3], [4,5,6]])
    print(arr_dim[1,0])
    print(arr_dim.ndim)
    print(arr_dim.shape)
    print("arr size:", arr_dim.size)

    arr_arng = np.arange(0, 10, 2);

    for x in arr_arng:
        print(x)

    #arr_arng = np.random.permutation(arr_arng)

    print("after random permutation:")

    for x in arr_arng:
        print(x)

    #new_arr = arr_arng.reshape(2, 5)
    #plt.hist(arr_arng, bins = 2)
    #print(arr_arng[1:2])
    #index = np.argwhere(arr_arng == 2)
    #print(index)

    arr2d = np.array([ [3,2,1] , [5,4,6]], dtype=int)

    index = np.argwhere(arr2d[:,:] == 2)
    print(index)

    arr2d[:].sort(axis=1)
    print(arr2d)

    anot_arr = arr[(arr > 4) & (arr < 8)]

    #print(anot_arr[[0,2,4]])

    input()

if __name__ == '__main__':
    main()

