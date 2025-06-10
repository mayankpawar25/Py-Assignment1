'''
list = [1, 2, 3, 4, 5, '6', [7, '8', 9], (1,2,3,4,5), {'a':1, 'b':2}]

for i in list:
    print(type(i), i)

'''

data = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(data)
