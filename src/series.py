#_*_ coding: utf-8 _*_


def fib(num):
    """Return value of ath number in fib sequence."""
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


def lucas(num):
    """Return value of ath number in lucas sequence."""
    if num <= 0:
        return 2
    elif num == 1:
        return 1
    else:
        return lucas(num - 1) + lucas(num - 2)


def sum(num, first=0, second=1):
    """Return value of ath number in lucas sequence."""
    if num <= 0:
        return first
    elif num == 1:
        return second
    else:
        return sum(num - 1, first, second) + sum(num - 2, first, second)


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
