import random
# random float between 0 and 1
print(random.random())

# random float between given values
print(random.uniform(1,5))

# random integer including both ends
print(random.randint(1,10))

# random integer excluding end value
print(random.randrange(1,10))

# random value from normal distribution
print(random.normalvariate(0,1))

# choose one random item
colors=["red","blue","green"]
print(random.choice(colors))

# choose unique random items
print(random.sample(colors,2))

# choose random items with replacement
print(random.choices(colors,k=3))

# shuffle list
nums=[1,2,3,4,5]
random.shuffle(nums)
print(nums)

# seed = same random result sequence
random.seed(1)
print(random.random())

random.seed(1)
print(random.random())

# secrets = secure random values
import secrets

# secure random integer from 0 to 9
print(secrets.randbelow(10))

# secure random bits
print(secrets.randbits(4))

# secure random choice
letters=["A","B","C","D"]
print(secrets.choice(letters))

# numpy random numbers
import numpy as np

# random floats
print(np.random.rand(3))

# random integers
print(np.random.randint(1,10,5))

# random 2d array
print(np.random.randint(1,10,(2,3)))

# random normal values
print(np.random.randn(3))

# shuffle numpy array
arr=np.array([1,2,3,4,5])
np.random.shuffle(arr)
print(arr)