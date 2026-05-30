import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from main import add, subtract, multiply


def test_add():
    assert add(3, 4) == 7


def test_subtract():
    assert subtract(10, 3) == 7

def test_multiply():
    assert multiply(2, 3) == 6

def test_add_negative():
    assert add(-1, 1) == 0
