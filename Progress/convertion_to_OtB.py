import numpy as np 

desired_ctB = np.array([ 0, 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
       18, 19, 20, -1, -2 ,-3 ,-4 ,-5 ,-6 ,-7, -8, -9, -10, -11, -12, -13 , -14,
       -15, -16, -17,-18,-19,-20])

desired_try = np.arange(-20,20,1)

sin_squared_weinberg = 0.2312215

ctz = []
ctZ = - np.sqrt(sin_squared_weinberg) * desired_ctB

for i in range(41): 
       ctZ = - np.sqrt(sin_squared_weinberg) * desired_try[i]
       print('Now I am doing', ctZ)

