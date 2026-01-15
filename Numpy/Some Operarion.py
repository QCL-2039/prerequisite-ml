import numpy as np

rand=np.random.default_rng()

arr=rand.integers(low=1,high=6,size=(3,3))
print("Your first array:",arr)

arr2=rand.integers(low=3,high=8,size=(3,3))

print("Your second array:",arr2)

print("Concatenate this two array:",np.concatenate((arr,arr2)))

print("Concatenate along a axis:",np.concatenate((arr,arr2),axis=1))

print("Unique array:",np.unique(arr))

print("Insert element on your array:",np.insert(arr,2,[7],axis=1))