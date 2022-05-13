"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    if position <= 0:
        return 0
    elif position == 1:
        return 1
    else:
        output = get_fib(position-1) + get_fib(position-2)
        return output
    return -1



# Test cases
print(get_fib(9))
# print(get_fib(11))
# print(get_fib(0))

def get_fac(position):
    if position <= 1:
        return 1
    else:
        output = position * get_fac(position-1)
        return output
    return -1

# Test cases
print(get_fac(5))