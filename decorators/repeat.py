#!/usr/bin/env python

def repeat(n):
    def decorator(func):
        def inner(*args, **kwargs):
            for _ in range(n): 
                func(*args, **kwargs)
        return inner
    return decorator 


@repeat(5) 
def greet(text):
    print(text)

greet("Yoooooo!")
