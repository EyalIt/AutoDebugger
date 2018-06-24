import inspect
import random
import param_int

def run(func):
    #print "execution data: " + str(execute(func))
    print "the number of lines of code: %d" % (get_lines_of_code(func))

def execute(func, argsGenerator, tracer = None):
    params = [gen.generateParam() for gen in argsGenerator]

    res = wrapper(func, params, tracer)
    return params, res

def getArgsGenerator(func):
    args = get_arguments(func)
    generator = argsGeneration(args)

    return generator

def get_arguments(func):
    args = inspect.getargspec(func)
    return args[0]

def argsGeneration(args):
    generators = []

    for arg in args:
        generators.append(param_int.IntParam(arg))

    return generators

def print_source_code(func):
    source = inspect.getsource(func)
    print source

def is_function(func):
    return inspect.isfunction(func)

def generate_param(minValue, maxValue):
    #return random.randint(-sys.maxint - 1, sys.maxint)
    return random.randint(minValue, maxValue)

def wrapper(func, args, tracer):
    if (tracer is not None):
        return tracer.runfunc(func, *args)

    return func(*args)

def get_lines_of_code(func):
    lines, first = get_source_lines(func)

    # starting from -1 since we also have the declaration of the function
    count = -1
    for line in lines:
        if (line != '\n'):
            count += 1

    return count

def get_source_lines(func):
    lines = inspect.getsourcelines(func)
    return lines