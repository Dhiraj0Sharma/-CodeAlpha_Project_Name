#Task-1
# FIBONACCI GENERATOR
#  The Fibonacci series is a sequence where each number is
#  the sum of the two preceding numbers, defined by a
#  mathematical recurrence relationship.

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_generator()
for _ in range(10):  
    print(next(fib_gen))
