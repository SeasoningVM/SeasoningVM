#!/usr/bin/env python
# -*- coding: utf-8 -*-

from opcode import OPRAND

# 5 + 10
example_add = [
    OPRAND.PUSH, 5,
    OPRAND.PUSH, 10,
    OPRAND.ADD,
    OPRAND.HALT
]

# 10 - 5
example_sub = [
    OPRAND.PUSH, 10,
    OPRAND.PUSH, 5,
    OPRAND.SUB,
    OPRAND.HALT
]

# 5 * 10
example_mul = [
    OPRAND.PUSH, 5,
    OPRAND.PUSH, 10,
    OPRAND.MUL,
    OPRAND.HALT
]

# 10 / 5
example_div = [
    OPRAND.PUSH, 10,
    OPRAND.PUSH, 5,
    OPRAND.DIV,
    OPRAND.HALT
]

example_loop = [
    OPRAND.PUSH, 1,
    OPRAND.PUSH, 1,
    OPRAND.ADD,
    OPRAND.JUMP, 2,
    OPRAND.HALT
]

example_store_load = [
    OPRAND.PUSH, 5,
    OPRAND.PUSH, 3,
    OPRAND.STORE,
    OPRAND.LOAD, 5,
    OPRAND.HALT
]

# x + y * z + u
# This should equal: 159
# It equals: 68
example_math = [
    OPRAND.PUSH, 8,  # x
    OPRAND.PUSH, 5,  # y
    OPRAND.PUSH, 12,  # z
    OPRAND.MUL,
    OPRAND.ADD,
    OPRAND.PUSH, 3,  # u
    OPRAND.HALT
]
