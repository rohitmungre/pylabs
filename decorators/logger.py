#!/usr/bin/env python

def log_decorator(func):
    def inner(*args, **kwargs):
        print("logging before the function call")
        func(*args, **kwargs)
        print("logging after the function call")
    return inner

@log_decorator
def say_hello():
    print("Hello!")

say_hello()
