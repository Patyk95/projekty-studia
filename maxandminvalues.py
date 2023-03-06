import numpy as np
from random import random, randint



#max values from array
value=np.random.uniform(-1000,1020,500)

def max_main(array):
    max= array[0]
    for i in range(1,len(array-1)):
        if array[i]>max:
            max=array[i]
    return max

print(max(value))
max_sys=value.max()
print(max_sys)