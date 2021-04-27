import functools


class Example:

    def wrapper(func):
        @functools.wraps(func)
        def wrap(self, *args, **kwargs):
            print("inside wrap")
            return func(self, *args, **kwargs)
        return wrap

    @wrapper
    def method(self):
        print("METHOD")

    wrapper = staticmethod(wrapper)


e = Example()
e.method()