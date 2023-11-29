# The mathematical factorial function is defined as the product of integers up to and
# including the argument.
# That is, f(x) = f(x - 1) * x, and f(1) = 1

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
