import numpy as np

arr=np.array([[1,2,3,4],
              [4,5,6,7],
              [7,8,9,10]])
print("Two dimensional Array:",arr)
print("Slicing of Two dimensional Array row wise:",arr[0:2])

print("Slicing of two dimensional array column wise:",arr[:,:2])
print("Slicing of two dimensional array column wise with step 2:",arr[:,::2])
print("Slicing of two dimensional array column wise with step 2 from index 0:",arr[:,0::2])
print("Slicing of two dimensional array column wise with step 2 from index 0 to 2:",arr[:,0:2:2])
print("Last element of the array:",arr[-1,-1])
print("First element of the array:",arr[0,0])

new_arr=np.where(arr>2,arr,0)
print("Condition:",arr>2)
print("Where condition is true:",np.where(arr>2))
print("Where condition is false:",np.where(arr<=2))
print("Where condition is true and false:",np.where(arr>2,arr,0))
print("Original array:",arr)
print("New array:",new_arr)