#!/usr/bin/env python
# -*- coding: utf-8 -*-

from examples import *
from opcode import OPRAND

stack_pointer = 32
stack = [None] * stack_pointer
instruction_pointer = 0

while True:
    working = example_add

    instruction = working[instruction_pointer]  # The current instruction is at the instruction pointer.
    instruction_pointer += 1  # Increase the instruction pointer (move down the list).

    if instruction == OPRAND.HALT:
        break

    # Stack Modifications:

    elif instruction == OPRAND.PUSH:
        stack_pointer -= 1
        stack[stack_pointer] = working[instruction_pointer]
        instruction_pointer += 1

    elif instruction == OPRAND.LOAD:
        stack_index = stack[stack_pointer]
        stack_pointer += 1
        stack[stack_index] = stack[stack_pointer]
        stack_pointer += 1

    elif instruction == OPRAND.STORE:
        stack_index = stack[stack_pointer]
        stack[stack_pointer] = stack[stack_index]

    # Stack Movement:

    elif instruction == OPRAND.JUMP:
        instruction_pointer = working[instruction_pointer]

    # Arithmetic Operators:

    elif instruction == OPRAND.ADD:
        value = stack[stack_pointer]
        stack_pointer += 1
        stack[stack_pointer] += value

    elif instruction == OPRAND.SUB:
        value = stack[stack_pointer]
        stack_pointer += 1
        stack[stack_pointer] -= value

    elif instruction == OPRAND.MUL:
        value = stack[stack_pointer]
        stack_pointer += 1
        stack[stack_pointer] *= value

    elif instruction == OPRAND.DIV:
        value = stack[stack_pointer]
        stack_pointer += 1
        stack[stack_pointer] //= value

    elif instruction == OPRAND.MOD:
        value = stack[stack_pointer]
        stack_pointer += 1
        stack[stack_pointer] %= value

    # Comparison Operations:

    elif instruction == OPRAND.LESS:
        value = stack[stack_pointer]
        stack_pointer += 1
        stack[stack_pointer] = int(stack[stack_pointer] < value)

    elif instruction == OPRAND.MORE:
        value = stack[stack_pointer]
        stack_pointer += 1
        stack[stack_pointer] = int(stack[stack_pointer] > value)

    elif instruction == OPRAND.EQUAL:
        value = stack[stack_pointer]
        stack_pointer += 1
        stack[stack_pointer] = int(stack[stack_pointer] == value)

    print(stack)
    print(stack[stack_pointer])
