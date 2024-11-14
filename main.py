import numpy as np #numpy array converts to matrix

my_list = [2,3,5,6,7]
print(my_list)

#convert list into numpy array

np_array = np.array(my_list)
print(np_array)

#multidimensional array
np_array = np.array([[1,2],[3,4]])
print(np_array)

dimensions = np.ndim
print(dimensions)

shape = np_array.shape
print(shape) 

np_array2 = np.array([[[1,2] , [3,4]] , [[5,6] , [7,8]]])
print(np_array2)

#accessing 2 from 2D arrays created above 
print(np_array[0,1])
#access 3
print(np_array[1,0])

#how to create an np array with ranges

arr = np.arange(0,12,1) #0 is starting number, 12 is ending number but it is excluded, 2 is the number of times the nect number is coming
print(arr)

#reshape - changing the dimension of the array without changing the values on it
reshaped = np_array.reshape(1,4)
print(reshaped)

reshaped2 = np_array.reshape(4,1)
print(reshaped)


#random permutation - returns a permutated range or a random sequence
per = np.random.permutation(arr)
print(per)

#sort the array

sorted_arr = np.sort(per) # sorts in ascending order
print(sorted_arr)