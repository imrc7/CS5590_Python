import numpy as np
# take random values ranging between 0 and 20 of specified size 15
x=np.random.randint(0,20,15)
print(x)
maxRepeated = np.bincount(x)
print (str("Most frequent item in the list is: ")+(str((np.argmax(maxRepeated)))))

