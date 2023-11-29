# # FIBONACCI

# Fibonacci series of 5 is : 0 1 1 2 3 5 8 13 21 34 55
#
# The 0th and 1st elements are 0 and 1
# Each subsequent element is the sum of the two preceding elements
# Write a function that returns the nth Fibonacci number

# Can use memoisation to speed this up

memo_fibonacci = []


def fibonacci(n):
    if len(memo_fibonacci) > n:
        return memo_fibonacci[n]
    if n == 0:
        memo_fibonacci.append(0)
        return 0
    if n == 1:
        memo_fibonacci.append(1)
        return 1
    sequence_number = fibonacci(n - 1) + fibonacci(n - 2)
    memo_fibonacci.append(sequence_number)
    return sequence_number


if __name__ == '__main__':
    result = fibonacci(40)
    print(result)