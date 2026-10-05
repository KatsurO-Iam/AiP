from practica.practica_1 import vector
from pytest import *


def test_uninit_len():
    z = vector()
    with raises(RuntimeError):
        z.len_vector()

def test_init():
    z = vector(3,4)
    assert(z.x == 3)
    assert(z.y == 4)

def test_len():
    z = vector(3,4)
    assert(z.len_vector() == 5)

