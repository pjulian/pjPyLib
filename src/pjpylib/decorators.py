"""pjPyLib Decorators."""

from datetime import datetime
from functools import wraps


def timeit(func):
    """Capture & log the runtime of a method."""
    @wraps(func)
    def timed(*args, **kwargs):
        startTime = datetime.now()
        return_data = func(*args, **kwargs)
        endTime = datetime.now()
        runTime = endTime - startTime
        print(f"{func.__name__} took {runTime.seconds}s to complete.")
        return return_data
    return timed
