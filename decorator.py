#!/usr/bin/python
import datetime
from functools import wraps
def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        print("--- Start time: %s ---" % start)
        ret = func(*args, **kwargs)
        end = datetime.datetime.now()
        print("--- End time: %s ---" % end)
        print("--- Function spend time: %s ---" % (end - start))
        return ret
    return wrapper

