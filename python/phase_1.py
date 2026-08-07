import numpy as np
py_list = [1,2,3,4]
print("python list multiplication: ", py_list * 2) #[1,2,3,4,1,2,3,4]
np_array = np.array([1,2,3,4])
print("python array multiplication: ", np_array * 2) #[2,4,6,8]

zeros = np.zeros((3,4))
print("zeroes array", zeros)

ones = np.ones((3,4))
print("zeroes array", ones)

full = np.full((3,4), 7)
print("zeroes array", full)

rand = np.random.random((3,4))
print("zeroes array", rand)

seq = np.arange(0, 11, 2)
print("array", seq)

arr = np.array([[1,2,3],[4,5,6]])
print("shape :", arr.shape)  #gives rows and cols
print("dimensions :", arr.ndim)  #2d matrix or 3d
print("size :", arr.size)  
print("data type :", arr.dtype)


#Reshape the array
arr = np.arange(12)
print("original Array: ", arr)

reshape = arr.reshape((3,4))
print("Reshaped array: ", reshape)

flatten = reshape.flatten()
print(flatten)


transpose = reshape.T
print(transpose)

#Line Space
nums = np.linspace(0, 20, 5)        #start with 0 end at 20 and 5 evenly spaced numbers 
print(nums)
