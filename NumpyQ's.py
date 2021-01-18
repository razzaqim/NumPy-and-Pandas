import numpy as np

print("Q1.Create a 1D array of numbers from 0 to 9")
array1 = np.arange(10)
print(array1)
print()
print("Q2.Create a 3×3 NumPy array of all True’s")
array2 = np.ones((3, 3), dtype=bool)
print(array2)
print()
print("Q3.Extract all odd numbers from array of 1-10")
array3= np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(array3[0: : 2])
print("Q4.Replace all odd numbers in the above array with -1 (subtract by 1)")
print(array3[0: : 2]-1)
print()
print("Q5.Convert a 1D array to a 2D array with 2 rows")
array4= np.array([1, 2, 3, 4, 5 , 6, 7, 8, 9, 10, 11, 12])
print(array4)
new_array = array4.reshape((2,6))
print(new_array)
print()
print("Q6.Create two 1D arrays a and b, stack these two arrays vertically, use the np.dot and np.sum to calculate totals")
a = np.arange(1,5)
b = np.arange(5,9)
stacked = np.stack((a, b), axis = 1)
print(stacked)
c = np.dot(a, b)
d = np.sum(stacked)
print(c)
print(d)
print()
print("Q7.Create the following pattern without hardcoding. Use only NumPy functions and the below input array")
tile =(np.tile(A= [1,2,3], reps = 3))
repeat =(np.repeat(a= [1,2,3], repeats=3, axis = 0))
pattern = np.concatenate((repeat,tile))
print(pattern)
print()
print("Q8.In two arrays a(1,2,3,4,5) and b(4,5,6,7,8,9) – remove all repeating items present in array b.")
arr1 = [1,2,3,4,5] 
arr2 = [4,5,6,7,8,9]
new_arr2 = np.setdiff1d(arr2, arr1) 
print(new_arr2)
print("Q9.Get all items between 5 and 10 from a(1,2,3,4,5) and b(4,5,6,7,8,9) and sum them together")
print(np.sum(new_arr2))