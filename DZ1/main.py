from functools import wraps
from operator import pow
from time import time


def timer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print("Calculated for:", time() - start)
        return result

    return wrapper


def trace(func):
    tracing = 0

    @wraps(func)
    def wrapper(*args):
        nonlocal tracing
        tracing += 1
        print("Вхождение в функцию №", tracing)
        print("-"*args[0],">","f(",args[0],")")
        result = func(*args)
        return result

    return wrapper


def exponentiation(*args, power=2):
    return list(map(pow, args, [power] * len(args)))


print("Result of exponentiation:", exponentiation(7, 2, 3, 6, 4, 7, 8, power=4))

IS_ODD = 'odd'
IS_EV = 'even'
IS_PRIME = 'prime'


def check_prime(num):
    if num == 1:
        return True
    if num <= 0:
        return False
    x = 2
    while num % x != 0:
        x += 1
    return x == num


@timer_decorator
def check_num(*args, filt='odd'):
    if filt == 'odd':
        return list(filter(lambda x: x % 2, args))
    if filt == 'even':
        return list(filter(lambda x: not x % 2, args))
    if filt == 'prime':
        return list(filter(lambda x: check_prime(x), args))


print("Result of checking:",
      check_num(54364364363, 1, 7, 23523, 3253, 5325, 235, 235, 235, 235, 57743, 7436, 38234, 23634, 6, filt=IS_PRIME))


@trace
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print("Result function fibonacci:", fibonacci(15))
