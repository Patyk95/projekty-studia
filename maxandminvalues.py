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



def min_main(array):
    min= array[0]
    for i in range(1,len(array-1)):
        if array[i]<min:
            min=array[i]
    return min




max_sys=value.max()
print(max(value))
print(max_sys)

min_sys=value.min()
print(min(value))
print(min_sys)