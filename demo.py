# coding:utf-8

import functools

def login_required(func):
    # 回复本身的特性
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func()
    return wrapper

@login_required
def itcast():
    """itcast python"""
    pass

# itcast --> wrapper

print(itcast.__name__) # wrapper.__name__
print(itcast.__doc__)  # wrapper.__doc__