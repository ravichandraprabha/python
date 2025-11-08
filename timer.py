from time import time, sleep
from functools import wraps


def timeit(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"{func.__name__} took {(end_time - start_time):.3f} seconds")
        return result

    return wrapped


@timeit
def sleep_function(sleep_seconds: int) -> None:
    sleep(sleep_seconds)
    return


@timeit
def hello_world():
    print(f"No action taken . Just hello world.")
    return


ret1 = sleep_function(2)
ret2 = hello_world()