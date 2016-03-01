#_*_ coding: utf-8 _*_

import pytest


def test_fib_0():
    from series import fib
    assert fib(0) == 1
