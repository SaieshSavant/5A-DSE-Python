import numpy as np

a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])

print("Array a:",a)
print("Array b:",b)
print("Sum of arrays a and b is:",np.add(a,b))
print("Difference of arrays a and b is:",np.subtract(a,b))
print("Product of arrays a and b is:",np.multiply(a,b))
print("Division of arrays a and b is:",np.divide(a,b))
print("Square root of array a is:",np.sqrt(a))
print("Exponential of array a is:",np.exp(a))

print("Minimum value of array a is:",np.min(a))
print("Maximum value of array b is:",np.max(b))
print("Mean value of array a is:",np.mean(a))
print("Standard Deviation of array b is:",np.std(b))
print("Sum of all the elements in array a: ",np.sum(a))

#reshaping arrays
c=np.array([[1,2],[3,4],[5,6]])
print("Array c:")
print(c)
print("Reshaped array c(2 rows, 3 columns):")
print(np.reshape(c,(2,3)))

#transposing arrays
d=np.array([[1,2,3],[4,5,6]])
print("Array d:")
print(d)
print("Transposed array d:")
print(np.transpose(d))


'''
Array a: [1 2 3 4 5]
Array b: [ 6  7  8  9 10]
Sum of arrays a and b is: [ 7  9 11 13 15]
Difference of arrays a and b is: [-5 -5 -5 -5 -5]
Product of arrays a and b is: [ 6 14 24 36 50]
Division of arrays a and b is: [0.16666667 0.28571429 0.375      0.44444444 0.5       ]
Square root of array a is: [1.         1.41421356 1.73205081 2.         2.23606798]
Exponential of array a is: [  2.71828183   7.3890561   20.08553692  54.59815003 148.4131591 ]
Minimum value of array a is: 1
Maximum value of array b is: 10
Mean value of array a is: 3.0
Standard Deviation of array b is: 1.4142135623730951
Sum of all the elements in array a:  15
Array c:
[[1 2]
 [3 4]
 [5 6]]
Reshaped array c(2 rows, 3 columns):
[[1 2 3]
 [4 5 6]]
Array d:
[[1 2 3]
 [4 5 6]]
Transposed array d:
[[1 4]
 [2 5]
 [3 6]]
'''
