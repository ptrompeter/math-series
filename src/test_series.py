#_*_ coding: utf-8 _*_

import pytest


def test_fib_1():
    from series import fib
    assert fib(1) == 0


def test_fib_3():
    from series import fib
    assert fib(3) == 1


def test_fib_6():
    from series import fib
    assert fib(6) == 5


def test_fib_20():
    from series import fib
    assert fib(20) == 4181
