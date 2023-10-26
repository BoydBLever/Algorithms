# Recursive implementation of n! (n-factorial) calculation
# One of the simplest recursive algorithms
# One-branch Time Complexity: O(n) Space Complexity: O(n)
def factorial(n):
    # Base case: n = 0 or 1
    if n <= 1:
        return 1

    # Recursive case: n! = n * (n - 1)!
    return n * factorial(n - 1)
# ---------------
# Two-branch Time Complexity: O(2^n)
# Recursive implementation to calculate the n-th Fibonacci number
# The Fibonacci numbers are the numbers in the following integer sequence, called the Fibonacci sequence, and characterized by the fact that every number after the first two is the sum of the two preceding ones.
# Formula: fib(n) = fib(n - 1) + fib(n - 2)
def fibonacci(n): 
    # Base case: n = 0 or 1
    if n <= 1:
        return n

    # Recursive case: fib(n) = fib(n - 1) + fib(n - 2)
    return fibonacci(n - 1) + fibonacci(n - 2)

# ---------------
# The base case is the simplest case of the problem that can be solved directly.
# The recursive case is the case where the function calls itself to solve a simpler version of the problem. 
#         fib(5)
#        /      \
#   fib(4)      fib(3)
#   /    \     /    \
# fib(3) fib(2) fib(2) fib(1)
# ... and so on
