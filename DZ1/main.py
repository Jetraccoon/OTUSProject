from functools import wraps
from itertools import repeat
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
    delim = []

    @wraps(func)
    def wrapper(*args):
        print("___" * len(delim) + '-->' + func.__name__ + "(" + str(args[0]) + ")")
        delim.append(1)
        result = func(*args)
        delim.pop()
        print("___" * len(delim) + '<--' + func.__name__ + "(" + str(args[0]) + ")" + "=" + str(result))
        return result

    return wrapper


def exponentiation(*args, power=2):
    return list(map(pow, args, repeat(power)))


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


def check_ev(num):
    return not num % 2


def check_odd(num):
    return num % 2


@timer_decorator
def check_num(*args, filt=IS_ODD):
    if filt == 'odd':
        return list(filter(check_odd, args))
    if filt == 'even':
        return list(filter(check_ev, args))
    if filt == 'prime':
        return list(filter(check_prime, args))


print("Result of checking:",
      check_num(54364364363, 1, 7, 23523, 3253, 5325, 235, 235, 235, 235, 57743, 7436, 38234, 23634, 6, filt=IS_PRIME))


@trace
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print("Result function fibonacci:", fibonacci(15))
