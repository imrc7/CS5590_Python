import numpy as np

# to generate random integers from 0-100 with 10x10
r=np.random.randint(0,100,(10,10))

# to generate random numbers(float vales) from 0-100 with 10x10
# r=np.random.rand(10,10)

minimum=r.min()
maximum=r.max()

# printing the random integers data
print(r)

# to print minimum and maximum values from the array
print("minimum - ",minimum,"maximum -",maximum)

