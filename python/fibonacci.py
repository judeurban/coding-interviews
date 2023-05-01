'''
Task
Write a function that accepts an index and returns its computed value from the fibonacci sequence.

[1 2 3 5 8 13 21 ...]

'''

def fib(n) -> int:

    if n <= 1:
        return n
    
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(7)) # prints 13