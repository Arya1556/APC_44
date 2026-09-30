# 1. one dimensional array containing 10 integers and display its size data data type and number of dimensions
import numpy as np
arr1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Array:", arr1)
print("Size (number of elements):", arr1.size)
print("Data Type:", arr1.dtype)
print("Number of Dimensions:", arr1.ndim)

# 2. Create two one-dimensional arrays and perform addition, subtraction, multiplication, division, and modulus operations on them.
import numpy as np
a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 5, 8, 10])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

#3.Create a NumPy array containing 10 numbers. Find and display the maximum, minimum, sum, and average of the elements
import numpy as np
arr = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
print("Array:", arr)
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))      
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))

#4.	Create a NumPy array of integers from 1 to 20. Use Boolean indexing to separate and display the even and odd numbers.
import numpy as np
arr = np.arange(1, 21)  
even_numbers = arr[arr % 2 == 0]
odd_numbers = arr[arr % 2 != 0]
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)


#5.	Create a one-dimensional array containing numbers from 1 to 12. Reshape it into matrix 
import numpy as np
arr=np.arange(1,13)

print("Original Array:", arr)
print("2 x 6 Matrix:")
print(arr.reshape(2, 6))

print("3 x 4 Matrix:")
print(arr.reshape(3, 4))

print("4 x 3 Matrix:")
print(arr.reshape(4, 3))

# 6. Create two 3x3 NumPy matrices and perform matrix addition.
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

b = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

result = np.add(a, b)

print("Matrix A:")
print(a)

print("Matrix B:")
print(b)

print("Matrix Addition:")
print(result)

# 7. Create two compatible matrices using NumPy and perform matrix multiplication using an appropriate NumPy function.
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[7, 8],
              [9, 10],
              [11, 12]])

result = np.matmul(a, b)

print("Matrix A:")
print(a)

print("Matrix B:")
print(b)

print("Matrix Multiplication:")
print(result)

# 8. Create a 3x4 matrix and display its transpose.
import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print("Original Matrix:")
print(arr)

print("Transpose:")
print(arr.T)

# 9. Create a 4x4 NumPy array and display the first row, last column, diagonal elements, and elements from the second and third rows.
import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print("Array:")
print(arr)

print("First Row:", arr[0])
print("Last Column:", arr[:, -1])
print("Diagonal Elements:", np.diag(arr))
print("Second and Third Rows:")
print(arr[1:3])

# 10. Create a 4x4 matrix and calculate the sum of each row and each column separately.
import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print("Matrix:")
print(arr)

print("Sum of Each Row:", np.sum(arr, axis=1))
print("Sum of Each Column:", np.sum(arr, axis=0))

# 11. Create a NumPy array containing numbers from 1 to 20 and using slicing display the first 5 elements, last 5 elements, alternate elements, and elements in reverse order.
import numpy as np

arr = np.arange(1, 21)

print("Array:", arr)
print("First 5 elements:", arr[:5])
print("Last 5 elements:", arr[-5:])
print("Alternate elements:", arr[::2])
print("Reverse order:", arr[::-1])


# 12. Create an array of 10 integers and replace all elements greater than 50 with 0 using NumPy Boolean indexing.
import numpy as np

arr = np.array([10, 65, 30, 80, 45, 90, 25, 55, 40, 70])

arr[arr > 50] = 0

print("Updated Array:", arr)


# 13. Create an unsorted NumPy array and display it in ascending and descending order.
import numpy as np

arr = np.array([45, 12, 78, 23, 9, 56, 34])

ascending = np.sort(arr)
descending = np.sort(arr)[::-1]

print("Original Array:", arr)
print("Ascending Order:", ascending)
print("Descending Order:", descending)


# 14. Create an array containing duplicate values and find and display only the unique elements.
import numpy as np

arr = np.array([10, 20, 10, 30, 40, 20, 50, 30, 60, 40])

unique = np.unique(arr)

print("Original Array:", arr)
print("Unique Elements:", unique)


# 15. Create two NumPy arrays and concatenate them horizontally and vertically.
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

horizontal = np.hstack((a, b))
vertical = np.vstack((a, b))

print("Array A:")
print(a)

print("Array B:")
print(b)

print("Horizontal Concatenation:")
print(horizontal)

print("Vertical Concatenation:")
print(vertical)


# 16. Store marks of 10 students in a NumPy array and calculate the highest marks, lowest marks, average marks, median, and standard deviation.
import numpy as np

marks = np.array([78, 85, 92, 67, 88, 75, 95, 82, 70, 90])

print("Marks:", marks)
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))


# 17. Take marks of 20 students, calculate the class average, and display the marks of students who scored above the average.
import numpy as np

marks = np.array([65, 78, 90, 55, 82, 74, 95, 68, 88, 72,
                  60, 85, 91, 77, 69, 93, 80, 58, 87, 76])

average = np.mean(marks)
above_average = marks[marks > average]

print("Marks:", marks)
print("Class Average:", average)
print("Marks Above Average:", above_average)


# 18. Create a 3D NumPy array of shape (2, 3, 4) containing numbers from 1 to 24 and display the array, number of dimensions, shape, and size.
import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)

print("Number of Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)


# 19. Create a 3D array of shape (2, 3, 4) and access the first element, last element, and elements at indexes [0,1,2] and [1,2,3].
import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)

print("First Element:", arr[0, 0, 0])
print("Last Element:", arr[-1, -1, -1])
print("Element at [0,1,2]:", arr[0, 1, 2])
print("Element at [1,2,3]:", arr[1, 2, 3])

# 20. Create a (2, 3, 4) NumPy array and calculate the sum of all elements, sum of each layer, sum along rows, and sum along columns.
import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("Array:")
print(arr)

print("Sum of all elements:", np.sum(arr))
print("Sum of each layer:")
print(np.sum(arr, axis=(1, 2)))
print("Sum along rows:")
print(np.sum(arr, axis=2))
print("Sum along columns:")
print(np.sum(arr, axis=1))


# 21. Create a 3D array of random integers between 1 and 100 and replace all values greater than 50 with 0.
import numpy as np

arr = np.random.randint(1, 101, size=(2, 3, 4))

print("Original Array:")
print(arr)

arr[arr > 50] = 0

print("Updated Array:")
print(arr)


# 22. Generate a random 3D array of shape (3, 4, 5) and calculate its mean, median, standard deviation, variance, minimum, and maximum.
import numpy as np

arr = np.random.randint(1, 101, size=(3, 4, 5))

print("3D Array:")
print(arr)

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))


# 23. Create a 3D NumPy array of shape (2, 3, 4) containing numbers from 1 to 24, flatten the array, and display both the original and flattened arrays.
import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

flattened = arr.flatten()

print("Original 3D Array:")
print(arr)

print("Flattened Array:")
print(flattened)


# 24. Create a 3D array containing integers from 1 to 27, flatten the array, and calculate the sum, average, maximum, and minimum.
import numpy as np

arr = np.arange(1, 28).reshape(3, 3, 3)

flattened = arr.flatten()

print("3D Array:")
print(arr)

print("Flattened Array:")
print(flattened)

print("Sum:", np.sum(flattened))
print("Average:", np.mean(flattened))
print("Maximum:", np.max(flattened))
print("Minimum:", np.min(flattened))


# 25. Create a random 3D NumPy array of shape (3, 4, 5), flatten it, and display elements greater than 50, even numbers, and elements less than the average value.
import numpy as np

arr = np.random.randint(1, 101, size=(3, 4, 5))

flattened = arr.flatten()
average = np.mean(flattened)

print("3D Array:")
print(arr)

print("Flattened Array:")
print(flattened)

print("Elements Greater Than 50:")
print(flattened[flattened > 50])

print("Even Numbers:")
print(flattened[flattened % 2 == 0])

print("Average:", average)

print("Elements Less Than Average:")
print(flattened[flattened < average])
	

