# # FIBONACCI

# Fibonacci series of 5 is : 0 1 1 2 3 5 8 13 21 34 55
#
# The 0th and 1st elements are 0 and 1
# Each subsequent element is the sum of the two preceding elements
# Write a function that returns the nth Fibonacci number

# Can use memoisation to speed this up

memo_fibonacci = []


def fibonacci(n: int) -> int:
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


def fibonacci_doubled(n: int) -> int:
    def fibonacci_double(number: int) -> tuple[int, int]:
        if number == 0:
            return 0, 1
        previous_result = fibonacci_double(number - 1)
        return previous_result[1], previous_result[0] + previous_result[1]

    return fibonacci_double(n)[0]


def fibonacci_without_recursion(n):
    previous = 1
    before_that = 0
    for i in range(n):
        next_value = previous + before_that
        before_that = previous
        previous = next_value
    return before_that


if __name__ == '__main__':
    result = fibonacci_without_recursion(40)
    print(result)
