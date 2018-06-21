import inspect
import random
import sys
import cProfile

def run(func):
    execute(func)

def execute(func):
    args = get_arguments(func)
    params = [generate_param() for arg in args]

    res = wrapper(func, params)
    return params, res

def get_arguments(func):
    args = inspect.getargspec(func)
    return args[0]

def print_source_code(func):
    source = inspect.getsource(func)
    print source

def is_function(func):
    return inspect.isfunction(func)

def generate_param():
    #return random.randint(-sys.maxint - 1, sys.maxint)
    return random.randint(-10, 10)

def wrapper(func, args):
    return func(*args)