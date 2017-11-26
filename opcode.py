#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum, auto

class OPRAND(Enum):
    HALT = auto()  # Stops the program.
    # Stack Modifications:
    PUSH = auto()  # Pushes a value onto the stack.
    # TODO: POP = auto()  # Pops a value from the stack.
    # TODO: MOVE = auto()  # Moves a value to the stack.
    LOAD = auto()  # Loads a value from the stack.
    STORE = ()  # Stores a value in the stack.
    # Stack Movement:
    JUMP = auto()  # Jumps to an instruction.
    # Arithmetic Operators:
    ADD = auto()  # Add the values in the stack.
    SUB = auto()  # Subtracts the values in the stack.
    MUL = auto()  # Multiplies the values in the stack.
    DIV = auto()  # Divides the values in the stack.
    MOD = auto()  # Finds the remainder of a division.
    # Comparison Operators:
    LESS = auto()  # Determines if a value is less than another.
    MORE = auto()  # Determines if a value is more than another.
    EQUAL = auto()  # Determines if a value equals another.
    # Logical Operators:
    # TODO: AND = auto()
    # TODO: NAND = auto()
    # TODO: OR = auto()
    # TODO: XOR = auto()
    # TODO: NOT = auto()
