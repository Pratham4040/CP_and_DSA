from array import *
import numpy as np

array_1 = array('i',[10,20,30])
array_2 = array('b',[68,67,97])
for x in array_1:
    print(x)
print(array_1[0])
print("\n")      
array_1.insert(3,40)
for x in array_1:
    print(x)
print("\n")     
array_1.remove(20)
for x in array_1:
    print(x)
for x in array_2:
    print(x)
print(type(array_2)) 
array_numpy= np.array(['str','sunil','sachin'])   
print(array_numpy)
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix)