import numpy as np
import random
array = np.random.randint(1,51,size=(3,4)) #ranom array 
print(array)
mean = np.mean(array)
median = np.median(array)
stddev = np.std(array)
print("Mean of the array is: ",mean)
print("Median of the array is: ",median)
print("Standard Deviation of the array is: ",stddev)
msum = np.sum(array)
rsum = np.sum(array,axis=1)
print(f"Sum of the elements is {msum} and sum of each row is{rsum}")
rarray = array.reshape(2,6)
print(rarray)
