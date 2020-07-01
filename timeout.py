from functools import wraps
import errno
import os
import signal

class TimeoutError(Exception):
    pass

# creates a decorator called @timeout which will timeout long running functions after 5 seconds
def timeout(seconds=5):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError("Operation Timeout, Try another Category")

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator