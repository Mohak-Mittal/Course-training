# ============================================================
#                  COMPLETE NUMPY TUTORIAL
#              Beginner Friendly Teaching Program
# ============================================================

# WHAT IS NUMPY?
#
# NumPy stands for Numerical Python.
#
# NumPy is a Python library used for numerical calculations.
#
# It provides a special data structure called an ARRAY.
#
# An array can store multiple values in an organized structure.
#
# NumPy is generally faster and more convenient than normal
# Python lists for mathematical and numerical operations.
#
# NumPy is widely used in:
# 1. Data Science
# 2. Machine Learning
# 3. Artificial Intelligence
# 4. Scientific Computing

# 5. Statistics
# 6. Mathematics
# 7. Image Processing
#
# INSTALLATION:
# pip install numpy
#
# ============================================================


# Importing NumPy
#
# "import numpy as np" means we are importing the NumPy
# library and giving it the short name "np".
#
# Instead of writing numpy.array(), we can write np.array().

import numpy as np


print("\n========== 1. INTRODUCTION TO NUMPY ==========")

print("NumPy Version:", np.__version__)


# ============================================================
#              2. CREATING NUMPY ARRAYS
# ============================================================

print("\n========== 2. CREATING ARRAYS ==========")

# THEORY:
#
# An array is a collection of elements.
#
# A NumPy array can contain numbers, strings, or other values.
#
# Unlike Python lists, NumPy arrays are designed primarily
# for efficient numerical calculations.
#
# np.array() is used to create an array.


# Example 1: Creating a one-dimensional array

a = np.array([10, 20, 30, 40, 50])

print("One-dimensional array:")
print(a)


# Example 2: Creating a two-dimensional array
#
# A two-dimensional array looks like a table.
#
# It contains rows and columns.

b = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\nTwo-dimensional array:")
print(b)


# Example 3: Creating a three-dimensional array
#
# A three-dimensional array can be imagined as
# multiple tables stacked together.

c = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("\nThree-dimensional array:")
print(c)


# ============================================================
#                 3. SPECIAL ARRAY CREATION
# ============================================================

print("\n========== 3. SPECIAL ARRAY CREATION ==========")

# THEORY:
#
# NumPy provides functions that automatically create arrays.
# These are useful when we need arrays filled with zeros,
# ones, or a sequence of numbers.


# np.zeros()
#
# Creates an array containing only zeros.

zero_array = np.zeros((3, 4))

print("\nArray containing zeros:")
print(zero_array)


# np.ones()
#
# Creates an array containing only ones.

one_array = np.ones((2, 3))

print("\nArray containing ones:")
print(one_array)


# np.full()
#
# Creates an array filled with a particular value.

full_array = np.full((2, 3), 7)

print("\nArray filled with 7:")
print(full_array)


# np.eye()
#
# Creates an identity matrix.
#
# An identity matrix contains 1 on its main diagonal
# and 0 everywhere else.

identity = np.eye(3)

print("\nIdentity matrix:")
print(identity)


# np.arange()
#
# Similar to Python range().
#
# It generates numbers from the starting value
# up to, but not including, the ending value.

arr = np.arange(1, 11)

print("\nNumbers from 1 to 10:")
print(arr)


# np.arange(start, stop, step)
#
# Step determines the difference between consecutive values.

arr = np.arange(2, 21, 2)

print("\nEven numbers from 2 to 20:")
print(arr)


# np.linspace()
#
# Creates a specified number of equally spaced values
# between a starting point and ending point.
#
# Unlike arange(), linspace() specifies how many values
# we want.

arr = np.linspace(1, 10, 5)

print("\nFive equally spaced values:")
print(arr)


# ============================================================
#                4. ARRAY PROPERTIES
# ============================================================

print("\n========== 4. ARRAY PROPERTIES ==========")

# THEORY:
#
# Every NumPy array has some important properties.
#
# These properties help us understand the structure
# and data type of an array.


x = np.array([
    [10, 20, 30],
    [40, 50, 60]
])


# ndim
#
# Returns the number of dimensions.

print("\nNumber of dimensions:", x.ndim)


# shape
#
# Returns the number of rows and columns.
#
# For this array, shape is (2, 3).
# It means 2 rows and 3 columns.

print("Shape of array:", x.shape)


# size
#
# Returns the total number of elements.

print("Total elements:", x.size)


# dtype
#
# Returns the data type of the elements.

print("Data type:", x.dtype)


# itemsize
#
# Returns the memory occupied by one element in bytes.

print("Memory per element:", x.itemsize, "bytes")


# nbytes
#
# Returns the total memory occupied by array elements.

print("Total array memory:", x.nbytes, "bytes")


# ============================================================
#                 5. INDEXING IN NUMPY
# ============================================================

print("\n========== 5. ARRAY INDEXING ==========")

# THEORY:
#
# Indexing means accessing a particular element.
#
# Python indexing starts from 0.
#
# This means:
# First element  = index 0
# Second element = index 1
# Third element  = index 2


a = np.array([100, 200, 300, 400, 500])

print("\nOriginal array:", a)

print("First element:", a[0])

print("Second element:", a[1])

print("Last element:", a[-1])


# Two-dimensional indexing
#
# Syntax:
# array[row_index, column_index]


b = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\nTwo-dimensional array:")
print(b)

print("Element at row 0, column 1:", b[0, 1])

print("Element at row 1, column 2:", b[1, 2])

print("Element at row 2, column 0:", b[2, 0])


# ============================================================
#                  6. ARRAY SLICING
# ============================================================

print("\n========== 6. ARRAY SLICING ==========")

# THEORY:
#
# Slicing means extracting a portion of an array.
#
# General syntax:
#
# array[start : stop : step]
#
# start = starting index
# stop  = ending index (not included)
# step  = gap between selected elements


a = np.array([10, 20, 30, 40, 50, 60, 70])

print("\nOriginal array:", a)

print("First three elements:", a[0:3])

print("Elements from index 2:", a[2:])

print("Elements before index 4:", a[:4])

print("Every second element:", a[::2])

print("Reverse array:", a[::-1])


# Slicing a two-dimensional array
#
# Syntax:
# array[row_start:row_stop, column_start:column_stop]


b = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\nOriginal matrix:")
print(b)

print("\nFirst two rows:")
print(b[0:2, :])

print("\nFirst two columns:")
print(b[:, 0:2])

print("\nMiddle element:")
print(b[1, 1])


# ============================================================
#              7. MATHEMATICAL OPERATIONS
# ============================================================

print("\n========== 7. MATHEMATICAL OPERATIONS ==========")

# THEORY:
#
# NumPy allows us to perform mathematical operations
# directly on complete arrays.
#
# This is called vectorized computation.
#
# Instead of writing loops to calculate every element,
# NumPy performs the operation on all elements.


a = np.array([10, 20, 30, 40])

print("\nOriginal array:", a)

print("Addition:", a + 5)

print("Subtraction:", a - 5)

print("Multiplication:", a * 2)

print("Division:", a / 2)

print("Power:", a ** 2)

print("Remainder:", a % 3)


# Operations between two arrays
#
# Both arrays have the same shape.
# NumPy performs operations element by element.

x = np.array([10, 20, 30])

y = np.array([1, 2, 3])

print("\nArray X:", x)

print("Array Y:", y)

print("X + Y:", x + y)

print("X - Y:", x - y)

print("X * Y:", x * y)

print("X / Y:", x / y)


# ============================================================
#                 8. UNIVERSAL FUNCTIONS
# ============================================================

print("\n========== 8. NUMPY UNIVERSAL FUNCTIONS ==========")

# THEORY:
#
# Universal functions are commonly called ufuncs.
#
# They perform mathematical operations on array elements.
#
# They work element by element and are optimized by NumPy.


a = np.array([1, 4, 9, 16, 25])

print("\nOriginal array:", a)


# Square root

print("Square root:", np.sqrt(a))


# Square

print("Square:", np.square(a))


# Exponential

print("Exponential:", np.exp(a))


# Natural logarithm

print("Natural logarithm:", np.log(a))


# Base-10 logarithm

print("Base 10 logarithm:", np.log10(a))


# Absolute value

b = np.array([-10, -5, 0, 5, 10])

print("\nAbsolute values:", np.abs(b))


# Trigonometric functions
#
# NumPy trigonometric functions use radians.

angles = np.array([0, np.pi/2, np.pi])

print("\nSine values:", np.sin(angles))

print("Cosine values:", np.cos(angles))

print("Tangent values:", np.tan(angles))


# ============================================================
#                 9. STATISTICAL FUNCTIONS
# ============================================================

print("\n========== 9. STATISTICAL FUNCTIONS ==========")

# THEORY:
#
# NumPy provides functions for statistical calculations.
#
# These functions are especially useful in data analysis.


marks = np.array([70, 80, 90, 60, 100])

print("\nStudent marks:", marks)


# np.sum()
#
# Calculates the sum of all elements.

print("Total marks:", np.sum(marks))


# np.mean()
#
# Calculates the average.

print("Average marks:", np.mean(marks))


# np.median()
#
# Returns the middle value after sorting.

print("Median marks:", np.median(marks))


# np.min()
#
# Finds the smallest element.

print("Minimum marks:", np.min(marks))


# np.max()
#
# Finds the largest element.

print("Maximum marks:", np.max(marks))


# np.std()
#
# Calculates standard deviation.
#
# Standard deviation measures how spread out
# the values are around their mean.

print("Standard deviation:", np.std(marks))


# np.var()
#
# Calculates variance.
#
# Variance is the average squared deviation
# from the mean, using NumPy's default population
# variance convention (ddof=0).

print("Variance:", np.var(marks))


# np.argmax()
#
# Returns the index of the largest value.

print("Index of highest mark:", np.argmax(marks))


# np.argmin()
#
# Returns the index of the smallest value.

print("Index of lowest mark:", np.argmin(marks))


# ============================================================
#               10. RESHAPING ARRAYS
# ============================================================

print("\n========== 10. RESHAPING ARRAYS ==========")

# THEORY:
#
# Reshaping means changing the structure of an array
# without changing its data.
#
# The total number of elements must remain the same.
#
# Example:
# 12 elements can become:
# 3 rows and 4 columns
# 4 rows and 3 columns
# 2 rows and 6 columns


a = np.arange(1, 13)

print("\nOriginal array:")
print(a)


# Convert one-dimensional array into 3x4 matrix.

b = a.reshape(3, 4)

print("\n3x4 matrix:")
print(b)


# Convert into 2x6 matrix.

c = a.reshape(2, 6)

print("\n2x6 matrix:")
print(c)


# Flatten
#
# Converts a multidimensional array into one dimension.

print("\nFlattened array:")
print(b.flatten())


# Ravel
#
# Also returns a flattened one-dimensional array.
# It may return a view instead of a copy when possible.

print("\nRavel result:")
print(b.ravel())


# ============================================================
#              11. TRANSPOSE OF AN ARRAY
# ============================================================

print("\n========== 11. TRANSPOSE ==========")

# THEORY:
#
# Transpose means converting rows into columns
# and columns into rows.
#
# For example:
#
# Original:
# 1 2 3
# 4 5 6
#
# Transpose:
# 1 4
# 2 5
# 3 6


a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nOriginal matrix:")
print(a)


# .T returns the transpose.

print("\nTranspose:")
print(a.T)


# ============================================================
#              12. JOINING NUMPY ARRAYS
# ============================================================

print("\n========== 12. JOINING ARRAYS ==========")

# THEORY:
#
# Joining means combining multiple arrays.
#
# NumPy provides several functions:
#
# np.concatenate()
# np.vstack()
# np.hstack()


a = np.array([1, 2, 3])

b = np.array([4, 5, 6])


# concatenate()
#
# Joins arrays along an existing axis.

print("\nConcatenate:")
print(np.concatenate((a, b)))


# vstack()
#
# Stacks arrays vertically.

print("\nVertical stack:")
print(np.vstack((a, b)))


# hstack()
#
# Stacks arrays horizontally.

print("\nHorizontal stack:")
print(np.hstack((a, b)))


# ============================================================
#               13. SPLITTING ARRAYS
# ============================================================

print("\n========== 13. SPLITTING ARRAYS ==========")

# THEORY:
#
# Splitting is the opposite of joining.
#
# It divides one array into multiple smaller arrays.


a = np.array([10, 20, 30, 40, 50, 60])

print("\nOriginal array:")
print(a)


# np.split()
#
# Splits the array into equal sections.

parts = np.split(a, 3)

print("\nThree split arrays:")
print(parts)


# np.array_split()
#
# Can split arrays into sections that are not equal.

parts = np.array_split(a, 4)

print("\nFour possibly unequal sections:")
print(parts)


# ============================================================
#              14. COPY AND VIEW
# ============================================================

print("\n========== 14. COPY AND VIEW ==========")

# THEORY:
#
# A VIEW is another way of looking at the same data.
#
# A COPY creates a separate array with independent data.
#
# Changing a view can affect the original array.
# Changing a copy does not affect the original array.


original = np.array([10, 20, 30, 40])

# Creating a view

view_array = original.view()

# Creating a copy

copy_array = original.copy()


print("\nOriginal:", original)

print("View:", view_array)

print("Copy:", copy_array)


# Change the view.

view_array[0] = 999

print("\nAfter changing the view:")

print("Original:", original)

print("View:", view_array)

print("Copy:", copy_array)


# Change the copy.

copy_array[1] = 888

print("\nAfter changing the copy:")

print("Original:", original)

print("Copy:", copy_array)


# ============================================================
#              15. BOOLEAN FILTERING
# ============================================================

print("\n========== 15. BOOLEAN FILTERING ==========")

# THEORY:
#
# Boolean filtering means selecting array elements
# based on a condition.
#
# Conditions return True or False.
#
# We can use these Boolean values to filter an array.


marks = np.array([35, 80, 45, 90, 25, 75, 60])

print("\nOriginal marks:")
print(marks)


# Find marks greater than 50.

print("\nMarks greater than 50:")
print(marks[marks > 50])


# Find marks less than 40.

print("\nMarks less than 40:")
print(marks[marks < 40])


# Find marks equal to 75.

print("\nMarks equal to 75:")
print(marks[marks == 75])


# Find marks between 40 and 80.
#
# Use parentheses around each condition.
# Use & for element-wise AND.

print("\nMarks between 40 and 80:")
print(marks[(marks >= 40) & (marks <= 80)])


# ============================================================
#                 16. SORTING ARRAYS
# ============================================================

print("\n========== 16. SORTING ARRAYS ==========")

# THEORY:
#
# Sorting means arranging elements in a particular order.
#
# np.sort() returns a sorted array.
#
# np.argsort() returns the indices that would sort the array.


a = np.array([50, 10, 40, 20, 30])

print("\nOriginal array:")
print(a)


# Sort in ascending order.

print("\nAscending order:")
print(np.sort(a))


# Sort in descending order.

print("\nDescending order:")
print(np.sort(a)[::-1])


# Get sorting indices.

print("\nSorting indices:")
print(np.argsort(a))


# ============================================================
#                17. RANDOM FUNCTIONS
# ============================================================

print("\n========== 17. RANDOM FUNCTIONS ==========")

# THEORY:
#
# NumPy provides a random module for generating
# random numbers and samples.
#
# default_rng() creates a random number generator.
#
# A seed makes the results reproducible.


rng = np.random.default_rng(42)


# Random integer
#
# Generates integers from 1 up to, but not including, 100.

print("\nRandom integer:")
print(rng.integers(1, 100))


# Multiple random integers

print("\nFive random integers:")
print(rng.integers(1, 100, size=5))


# Random decimal numbers between 0 and 1.

print("\nRandom decimal numbers:")
print(rng.random(5))


# Random normal distribution
#
# Normal distribution is a bell-shaped probability
# distribution, often used in statistics.

print("\nNormal distribution values:")
print(rng.normal(loc=0, scale=1, size=5))


# Random choice
#
# Selects random elements from an array.

names = np.array(["Aman", "Rahul", "Priya", "Simran"])

print("\nRandom name:")
print(rng.choice(names))


# Shuffle
#
# Changes the order of elements in place.

numbers = np.array([1, 2, 3, 4, 5])

rng.shuffle(numbers)

print("\nShuffled numbers:")
print(numbers)


# ============================================================
#                 18. LINEAR ALGEBRA
# ============================================================

print("\n========== 18. LINEAR ALGEBRA ==========")

# THEORY:
#
# Linear algebra is an important branch of mathematics.
#
# It deals with vectors, matrices, determinants,
# matrix multiplication, and inverse matrices.
#
# NumPy provides the linalg module for these operations.


a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])


print("\nMatrix A:")
print(a)

print("\nMatrix B:")
print(b)


# Matrix multiplication
#
# np.matmul() performs matrix multiplication.
#
# This is different from a * b, which multiplies
# corresponding elements.

print("\nMatrix multiplication:")
print(np.matmul(a, b))


# Dot product

print("\nDot product:")
print(np.dot(a, b))


# Determinant
#
# A determinant is a special number calculated
# from a square matrix.

print("\nDeterminant of A:")
print(np.linalg.det(a))


# Inverse matrix
#
# The inverse of a matrix is the matrix that
# multiplies with the original matrix to produce
# the identity matrix.
#
# An inverse exists only when the matrix is invertible.

print("\nInverse of A:")
print(np.linalg.inv(a))


# Eigenvalues

print("\nEigenvalues of A:")
print(np.linalg.eigvals(a))


# ============================================================
#                 19. BROADCASTING
# ============================================================

print("\n========== 19. BROADCASTING ==========")

# THEORY:
#
# Broadcasting is a NumPy feature that allows
# mathematical operations between arrays of
# different but compatible shapes.
#
# NumPy automatically expands the smaller array
# conceptually to match the larger array.
#
# It does not usually need to create repeated copies
# of the smaller array in memory.


a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

b = np.array([1, 2, 3])


print("\nLarge array:")
print(a)

print("\nSmall array:")
print(b)


# NumPy adds the small array to each row.

print("\nBroadcasting result:")
print(a + b)


# Another example

numbers = np.array([10, 20, 30])

print("\nMultiply every element by 10:")
print(numbers * 10)


# ============================================================
#                20. HANDLING MISSING VALUES
# ============================================================

print("\n========== 20. MISSING VALUES ==========")

# THEORY:
#
# np.nan represents Not a Number.
#
# It is commonly used to represent missing numerical data.
#
# Normal comparisons with NaN behave unusually:
# NaN is not equal to itself.
#
# Use np.isnan() to detect missing values.


data = np.array([10, 20, np.nan, 40, 50])

print("\nArray with missing value:")
print(data)


# Detect NaN values.

print("\nMissing value locations:")
print(np.isnan(data))


# Count missing values.

print("\nNumber of missing values:")
print(np.isnan(data).sum())


# Mean with missing values.
#
# np.mean() returns NaN if the input contains NaN.

print("\nNormal mean:")
print(np.mean(data))


# np.nanmean() ignores NaN values.

print("\nMean ignoring missing values:")
print(np.nanmean(data))


# ============================================================
#             21. PRACTICAL EXAMPLE: STUDENT MARKS
# ============================================================

print("\n========== 21. PRACTICAL EXAMPLE ==========")

# THEORY:
#
# Suppose we have marks of five students in three subjects.
#
# Each row represents one student.
# Each column represents one subject.
#
# We can use NumPy to calculate total marks,
# average marks, highest marks, and lowest marks.


marks = np.array([
    [80, 90, 70],
    [60, 75, 85],
    [90, 95, 100],
    [50, 65, 70],
    [85, 80, 90]
])


print("\nStudent marks:")
print(marks)


# Total marks of each student.
#
# axis=1 means calculate across columns,
# producing one result for each row.

total = np.sum(marks, axis=1)

print("\nTotal marks of each student:")
print(total)


# Average marks of each student.

average = np.mean(marks, axis=1)

print("\nAverage marks of each student:")
print(average)


# Highest mark in each subject.
#
# axis=0 means calculate down rows,
# producing one result for each column.

highest = np.max(marks, axis=0)

print("\nHighest mark in each subject:")
print(highest)


# Lowest mark in each subject.

lowest = np.min(marks, axis=0)

print("\nLowest mark in each subject:")
print(lowest)


# Overall class average.

class_average = np.mean(marks)

print("\nOverall class average:")
print(class_average)


# ============================================================
#               22. PRACTICAL EXAMPLE: SALES
# ============================================================

print("\n========== 22. SALES ANALYSIS ==========")

# Suppose a shop records its sales for seven days.

sales = np.array([1200, 1500, 900, 2000, 1800, 2500, 1700])

print("\nWeekly sales:")
print(sales)


# Total sales

print("\nTotal sales:")
print(np.sum(sales))


# Average daily sales

print("\nAverage daily sales:")
print(np.mean(sales))


# Highest sales

print("\nHighest sales:")
print(np.max(sales))


# Lowest sales

print("\nLowest sales:")
print(np.min(sales))


# Days with sales greater than 1500

print("\nSales greater than 1500:")
print(sales[sales > 1500])


# ============================================================
#                    END OF TUTORIAL
# ============================================================

print("\n==========================================")
print("        NUMPY TUTORIAL COMPLETED!")
print("==========================================")

print("\nYou have learned the basic and important")
print("NumPy functions with practical examples.")

print("\nKeep experimenting with the arrays!")
