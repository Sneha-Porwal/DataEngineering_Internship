import time
def time_logger(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Execution Time:", end - start)
    return wrapper


@time_logger
def func():
    x = 5
    if x > 0:
        print("Positive")
    else:
        print("Non-positive")


func()
