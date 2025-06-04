# Factorial Method

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

inp = int(input('Enter a number: '))
result = factorial(inp)
print('Factorial of ' + str(inp) + ' is: ' + str(result))