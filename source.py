#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from examples import *
from opcode import OPRAND


def seasoning(source):
    stack_pointer = 32
    stack = [None] * stack_pointer
    instruction_pointer = 0

    while True:
        working = program

        instruction = working[instruction_pointer]  # The current instruction is at the instruction pointer.
        instruction_pointer += 1  # Increase the instruction pointer (move down the list).

        if instruction in [OPRAND.HALT, "HALT"]:
            break

        # Stack Modifications:

        elif instruction in [OPRAND.PUSH, "PUSH"]:
            stack_pointer -= 1
            stack[stack_pointer] = int(working[instruction_pointer])
            instruction_pointer += 1

        elif instruction in [OPRAND.LOAD, "LOAD"]:
            stack_index = stack[stack_pointer]
            stack[stack_pointer] = stack[stack_index]

        elif instruction in [OPRAND.STORE, "STORE"]:
            stack_index = stack[stack_pointer]
            stack_pointer += 1
            stack[stack_index] = stack[stack_pointer]
            stack_pointer += 1

        # Stack Movement:

        elif instruction in [OPRAND.JUMP, "JUMP"]:
            instruction_pointer = working[instruction_pointer]

        # Arithmetic Operators:

        elif instruction in [OPRAND.ADD, "ADD"]:
            value = stack[stack_pointer]
            stack_pointer += 1
            stack[stack_pointer] += value

        elif instruction in [OPRAND.SUB, "SUB"]:
            value = stack[stack_pointer]
            stack_pointer += 1
            stack[stack_pointer] -= value

        elif instruction in [OPRAND.MUL, "MUL"]:
            value = stack[stack_pointer]
            stack_pointer += 1
            stack[stack_pointer] *= value

        elif instruction in [OPRAND.DIV, "DIV"]:
            value = stack[stack_pointer]
            stack_pointer += 1
            stack[stack_pointer] //= value

        elif instruction in [OPRAND.MOD, "MOD"]:
            value = stack[stack_pointer]
            stack_pointer += 1
            stack[stack_pointer] %= value

        # Comparison Operations:

        elif instruction in [OPRAND.LESS, "LESS"]:
            value = stack[stack_pointer]
            stack_pointer += 1
            stack[stack_pointer] = int(stack[stack_pointer] < value)

        elif instruction in [OPRAND.MORE, "MORE"]:
            value = stack[stack_pointer]
            stack_pointer += 1
            stack[stack_pointer] = int(stack[stack_pointer] > value)

        elif instruction in [OPRAND.EQUAL, "EQUAL"]:
            value = stack[stack_pointer]
            stack_pointer += 1
            stack[stack_pointer] = int(stack[stack_pointer] == value)

        print(stack)
        print(stack[stack_pointer])


if __name__ == "__main__":
    program = example_add
    type_ = "python"

    # program = "example.sasm"
    # type_ = "file"
    
    try:
        program = sys.argv[1]
        type_ = sys.argv[2]

    except IndexError:
        pass

    if type_ != "python":
        if type_ == "file":
            program = open(program).readlines()

        list_ = []

        for line in program:
            if not line.startswith(";"):
                list_.append(line)

        program = "".join(list_)

        list_ = []
        program_split = program.split(",")

        for code in program_split:
            list_.append("".join(code.split()))

        program = list_

    seasoning(program)
