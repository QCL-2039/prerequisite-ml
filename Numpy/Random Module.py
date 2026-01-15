import numpy as np

rand=np.random.default_rng(seed=1)
rand_numpy=rand.integers(low=0,high=100,size=(3,3))

print("Random numbers with numpy:",rand_numpy)
print(type(rand_numpy))

rand_numpy_float=rand.random(size=(3,3))
print("Random numbers with numpy float:",rand_numpy_float)
print(type(rand_numpy_float))


import random
print("Here I am going to generate numbers with random module")
random_number = random.randint(0,100)
print(type(random_number))
print(random_number)
print("Random numbers(1-6):",random.randint(1,6))
print("Random numbers(1-6):",random.randrange(1,6))
print("Random numbers(1-6):",random.choice([1,2,3,4,5,6]))
print("Random numbers(1-6):",random.shuffle([1,2,3,4,5,6]))
print("Random numbers(1-6):",random.random())
print("Random numbers(1-6):",random.uniform(1,6))