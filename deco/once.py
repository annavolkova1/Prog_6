import functools


def once(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if not inner.called:
            inner.value = func(*args, **kwargs)
            inner.called = True

    inner.called = False
    return inner


@once
def initialize_settings():
    print("Settings initialized")
    k = 0
    k += 1
    return k


print(initialize_settings())
print('')
print(initialize_settings())