#_*_ coding: utf-8 _*_


def fib(a):
    """Return value of ath number in fib sequence."""
    if a <= 0:
        return 0
    elif a == 1:
        return 1
    else:
        return fib(a-1) + fib(a-2)

