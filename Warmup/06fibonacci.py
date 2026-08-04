# Write a function fib(n) that returns the nth Fibonacci number. 
# The Fibonacci sequence is defined as F(n) = F(n-1) + F(n-2) with F(0) = 1 and F(1) = 1, 
# which produces the following pattern:

# 1, 1, 2, 3, 5, 8, 13 ...

def fib(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Debug / Test
print(fib(5))  # Output: 8