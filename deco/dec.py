import functools


def call_and_save(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
            ar = 2*args[0]
            return func(ar, **kwargs)
    return inner


def initialize_settings(ar):
    print(ar)
    return 'Hello, World!'


print(call_and_save(initialize_settings)(2))
print(initialize_settings(2))



