from __future__ import print_function

class Boomer(object):
    def __init__(self):
        self.level = 0
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        if self.level > 0:
            print(*args, **kwargs)

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, *exc):
        self.level -= 1
        if self.level == 0:
            print("boom was called %d times!" % self.calls)

boom = Boomer()