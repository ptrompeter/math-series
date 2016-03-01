#_*_ coding: utf-8 _*_


def fib(a):
    """Return value of ath number in fib sequence."""
    if a <= 0:
        return 0
    elif a == 1:
        return 1
    else:
        return fib(a - 1) + fib(a - 2)


def lucas(a):
    """Return value of ath number in lucas sequence."""
    if a <= 0:
        return 2
    elif a == 1:
        return 1
    else:
        return lucas(a - 1) + lucas(a - 2)


def sum(a, b=0, c=1):
    """Return value of ath number in lucas sequence."""
    if a <= 0:
        return b
    elif a == 1:
        return c
    else:
        return sum(a - 1, b, c) + sum(a - 2, b, c)


if __name__ == "__main__":
    print(u"Our fibonacci sequence:")
    print(u"fib(0) = ", fib(0))
    print(u"fib(10) = ", fib(10))
    print(u"Our Lucas series:")
    print(u"lucas(0) = ", lucas(0))
    print(u"lucas(10) = ", lucas(10))
    print(u"Our sum series:")
    print(u"sum(0) = ", sum(0))
    print(u"sum(10) = ", sum(10))
    print(u"sum(0, 2, 1) = ", sum(0, 2, 1))
    print(u"sum(10, 2 ,1) = ", sum(10, 2, 1))
