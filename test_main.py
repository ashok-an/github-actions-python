#!/usr/bin/env python

import pytest
import main

def test_add():
    main.main(oper='add', a=5, b=10)

def test_sub():
    main.main(oper='sub', a=5, b=10)

def test_mul():
    main.main(oper='mul', a=5, b=10)

def test_div():
    main.main(oper='div', a=5, b=10)

@pytest.mark.skip(reason="need to mock")
def test_div_zero():
    main.main(oper='div', a=5, b=0)

def test_get_args():
    main.main(oper='something', a=4, b=8)

