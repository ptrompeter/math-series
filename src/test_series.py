#_*_ coding: utf-8 _*_

import pytest


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
