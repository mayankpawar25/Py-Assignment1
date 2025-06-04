# Demonstrate List Slicing

# data = list(range(1, 11))
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Original list: ', data)
slicedData = data[:5]
print('Extracted first five elements: ', slicedData)
reverseSlicedData = slicedData[::-1]
print('Reverse extracted elements: ', reverseSlicedData)