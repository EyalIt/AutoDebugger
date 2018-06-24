import psutil
import os

def run():
    pid = current_pid()
    print "cpu usage for this process: %.2f" % (cpu_usage_per_pid(pid))
    #print cpu_usage()

def cpu_usage():
    print psutil.cpu_percent()

def cpu_stats():
    print psutil.cpu_stats()

def current_pid():
    return os.getpid()

def cpu_usage_per_pid(pid):
    p = psutil.Process(pid)
    return p.cpu_percent() / psutil.cpu_count()