#_*_ coding: utf-8 _*_


def test_fib_0():
    from series import fib
    assert fib(0) == 0


def test_fib_3():
    from series import fib
    assert fib(3) == 2


def test_fib_6():
    from series import fib
    assert fib(6) == 8


def test_fib_20():
    from series import fib
    assert fib(20) == 6765


def test_lucas_0():
    from series import lucas
    assert lucas(0) == 2


def test_lucas_1():
    from series import lucas
    assert lucas(1) == 1


def test_lucas_5():
    from series import lucas
    assert lucas(5) == 11


def test_lucas_10():
    from series import lucas
    assert lucas(10) == 123


def test_sum_10a():
    from series import sum
    assert sum(10) == 55


def test_sum_10b():
    from series import sum
    assert sum(10, 2, 1) == 123