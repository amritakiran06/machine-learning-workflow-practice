import numpy as np


arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("1D Array:", arr1)
print("2D Array:\n", arr2)


print("Shape of arr2:", arr2.shape)
print("Data type:", arr1.dtype)
print("Number of dimensions:", arr2.ndim)
print("Total elements:", arr2.size)

print("Array + 5:", arr1 + 5)
print("Array * 2:", arr1 * 2)
print("Sum of arr1:", np.sum(arr1))
print("Mean of arr1:", np.mean(arr1))