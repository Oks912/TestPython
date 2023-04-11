def print_fname(func):
    def func_2(*args, **kwargs):
        print(f"Function name: {func.__name__}")
        return func(*args, **kwargs)

    return func_2


@print_fname
def add(x, y):
    return x / y


result = add(64,20)
print(result)


@print_fname
def stepin(x):
    return x **3


result = stepin(6)
print(result)

