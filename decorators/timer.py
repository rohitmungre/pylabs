#!//usr/bin/env python

import time 

def timer_decorator(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end-start}")
    return inner

@timer_decorator
def slow_function():
    print("Start func")
    time.sleep(2)
    print("Finished func!")

slow_function()

