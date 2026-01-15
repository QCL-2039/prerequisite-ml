import numpy as np
import random


rand=np.random.default_rng()

arr2D=rand.integers(low=0,high=10,size=(3,3))
print("Your 2D array is:",arr2D)

arr3D=rand.integers(low=30,high=50,size=(3,3,3))
print("Your 3D Array is:",arr3D)


print("Now I am going to shuffle my array.")

rand.shuffle(arr3D)
rand.shuffle(arr3D)

print("After shuffled:",arr3D,"\n",arr3D)


rand=np.random.default_rng()

arr=rand.integers(low=1,high=10,size=(2,2))
print(arr)

arr=np.random.randint(low=1,high=10,size=(2,2))
print(arr)

arr=random.randint(1,6)
print(arr)

