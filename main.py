import cProfile, pstats, StringIO
import func_utils
import data

def wrap(pre, post):
    def decorate(func):
        def call(*args, **kwargs):
            pre(func, *args, **kwargs)
            result = func(*args, **kwargs)
            post(func, *args, **kwargs)
            return result

        return call

    return decorate

def trace_in(func, *args, **kwargs):
   print "Entering function",  func.__name__

def trace_out(func, *args, **kwargs):
   print "Leaving function", func.__name__

@wrap(trace_in, trace_out)
def calc(x, y):
   return x + y

def add(x, y):
    return x + y


def main():
    #print calc(1, 2)

    #print_profiling(main.__name__)
    data.run()

def print_profiling(func):
    pr = cProfile.Profile()
    #pr.enable()
    pr.run(func)
    #pr.disable()

    s = StringIO.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print s.getvalue()

if __name__ == '__main__':
    main()
