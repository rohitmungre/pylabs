#!/usr/bin/env python

def validate_positive(func):
    def inner(n):
        if n > 0:
            print(f"{n} is positive!")
        else:
            print(f"{n} is negative!")
        func(n)
    return inner


@validate_positive
def square(n):
    return n*n

print(square(4))
print(square(-2))

