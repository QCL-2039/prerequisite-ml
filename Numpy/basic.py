import numpy as np

print("Version of your numpy:",np.__version__)

arr=np.array([1,2,3,4])
print("One dimensional array with numpy:",arr)
print("Dimension of your array:",arr.ndim)
print("Shape of your array:",arr.shape)
print("Slicing of 1D array:",arr[0:2])
arr=np.array([
            [1,2,3],
            [4,5,6],
            [7,8,9],
            ])
print("Two dimensional Array:",arr)  
print("Dimension of your array:",arr.ndim) 
print("Shape of your array:",arr.shape)
print("Slicing of 2D array:",arr[0:2,0:2])

arr=np.array([
            [[1,2,3],
            [4,5,6],
            [7,8,9]],

            [[10,11,12],
            [13,14,15],
            [16,17,18]],

            [[19,20,21],
            [22,23,24],
            [25,26,27]]
            ])
print("Three dimensional Array:",arr)  
print("Dimension of your array:",arr.ndim) 
print("Shape of your array:",arr.shape)
print("First element of my 3D array is:",arr[0][0][0])
print("Last element of my 3D array is:",arr[2][2][2])

print("Array slicing:",arr[0:2,0:2,0:2])

arr=np.array([
            [1,2,3],
            [4,5,6],
            [7,8,9],
            ])
print("Maximum value of the array:",np.max(arr))            
print("Minimum value of the array:",np.min(arr))
print("Sum of the array:",np.sum(arr))
print("Mean of the array:",np.mean(arr))
print("Median of the array:",np.median(arr))
# print("Mode of the array:",np.mod(arr))
print("Standard deviation of the array:",np.std(arr))
print("Variance of the array:",np.var(arr))
print("Correlation of the array:",np.corrcoef(arr))
print("Covariance of the array:",np.cov(arr))
print("Minimum value's index of the array:",np.argmin(arr))
print("Maximum value's index of the array:",np.argmax(arr))
print("Sorting of the array:",np.sort(arr))
print("Sorting of the array in descending order:",np.sort(arr)[::-1])
print("Sorting of the array in ascending order:",np.sort(arr))