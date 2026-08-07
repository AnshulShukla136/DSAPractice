import numpy as np
import matplotlib.pyplot as plt
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],
    [2,130000, 220000, 180000, 240000],
    [3,140000, 160000, 180000, 220000],
    [4,160000, 180000, 110000, 190000],
    [5,190000, 200000, 150000, 200000],  
])

#print first 3 rows
print("Data for first 3 restraunt", sales_data[0:3])

#sum column wise
print("sum is:", np.sum(sales_data, axis = 0)) #axis 0 means col wise 1 means row wise

print(np.sum(sales_data[:, 1:], axis = 0))  #[row, col] [:, 1:] means all rows and cols starting from 1


cumsum = np.cumsum(sales_data[:, 1:], axis = 1)
print(cumsum)

# plt.figure(figsize = (8, 6))
# plt.plot(np.mean(cumsum, axis = 0))
# plt.title("Average cumulative sales across all restaurant: ")
# plt.xlabel("years")
# plt.ylabel("sales")
# plt.grid(True)
# plt.show()


vector1 = np.array([1,2,3,4,5])
vector2 = np.array([6,7,8,9,2])
print("Vector addition : " , vector1 + vector2) 
print("Vector multiplication : " , vector1 * vector2) 
print("dot product : " , np.dot(vector1 , vector2)) 