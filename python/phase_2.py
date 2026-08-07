import numpy as np
arr = np.arange(1,13)
print("Normal Slicing: ", arr[3:7])

arr_2d = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print("Element: ", arr_2d[1,2]) #1st row's second element
print("Element: ", arr_2d[1][2]) 
print("Entire col:" ,arr_2d[:,1])   # selecting all rows and 1st column

#Sorting

arr2 = np.array([2,5,3,4,8,5,6,0,1])
print("Sorted arr", np.sort(arr2))

arr_2d_sort = np.array([[3,2], [1,2], [2,3]])
print("array sorted by col", np.sort(arr_2d_sort, axis = 0))

#Filter
nums = np.array([1,2,3,4,18,5,6,7,88,9,10])
even_nums = nums[nums % 2 == 0]
print(even_nums)


# #filter with mask
mask = nums > 5
print("number greater than 5 are ", mask) #it will give true false
print("number greater than 5 are ", nums[mask])
print("number grerater than 5: ", nums[nums > 5])

#np.where()

where_result = np.where(nums > 5)
print("indices are :", where_result)
print("np Where results: ", nums[where_result])

#concatenation
arr1 =  np.array([1,2,3,4])
arr2 =  np.array([5,6,7,8])

combined = np.concatenate((arr1,arr2))
print(combined)

#Array compatibility
a =  np.array([1,2,3])
b =  np.array([4,5,6])
c =  np.array([7,8,9])

print(a.shape == b.shape)

#insert new row vstack

original = np.array([[1,2], [3,4]])
new_row = np.array([[5,6]])

with_new = np.vstack((original, new_row))
print(with_new)