# import the required libraries # combinations
from itertools import combinations

# Read the input list and the value for the combinations we want to make
# In this case we want o find triplet(3) combination

inputData = list(combinations([1,3,6,2,-1,2,8,-2,9],3))

# Create an empty list
tripletsFound = []

# Initialise a variable index so that list value at particular index can be stored
index=0

# Find the length of the list to iterate the combinations
length=len(inputData)

# Iterate using range function, It starts looping from 0 to provided value
for i in range(length):
  if (sum(inputData[index])==0):  #check if the sum of the cmbination is 0
    tripletsFound.append(inputData[index]) # if a combination triplet is found append to list
  index+=1 # Increment the index so that the next element can be checked

# Print the triplet output
print("Triplets are: ",tripletsFound)