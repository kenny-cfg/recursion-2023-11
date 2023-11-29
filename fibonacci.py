# # FIBONACCI

# Fibonacci series of 5 is : 0 1 1 2 3 5 8 13 21 34 55
#
# The 0th and 1st elements are 0 and 1
# Each subsequent element is the sum of the two preceding elements
# Write a function that returns the nth Fibonacci number

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
