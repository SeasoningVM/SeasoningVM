#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import IntEnum
from enum import unique


@unique
class OPCODE(IntEnum):
    HALT = 0  # Stops the program.
    # Stack Modifications:
    PUSH = 1  # Pushes a value onto the stack.
    # TODO: POP = auto()  # Pops a value from the stack.
    # Memory Modification:
    MOVE = 13  # Moves a value into a memory slot.
    LOAD = 2  # Loads a value from the stack.
    STORE = 3  # Stores a value in the stack.tack.
    # Arithmetic Operators:
    ADD = 5  # Add the values in the stack.
    SUB = 6  # Subtracts the values in the stack.
    MUL = 7  # Multiplies the values in the stack.
    DIV = 8  # Divides the values in the stack.
    MOD = 9  # Finds the remainder of a division.
    # Comparison Operators:
    COMPARE = 16  # Compares two values.
    LESS = 10  # Determines if a value is less than another.
    MORE = 11  # Determines if a value is more than another.
    EQUAL = 12  # Determines if a value equals another.
    # Logical Operators:
    # TODO: AND = auto()
    # TODO: NAND = auto()
    # TODO: OR = auto()
    # TODO: XOR = auto()
    # TODO: NOT = auto()
    # Instruction Movement:
    JUMP = 4  # Jumps to an instruction.
    JUMPLESS = 14  # Jump if less-than.
    JUMPLESSEQUAL = 23  # Jump if less-than or equal.
    JUMPMORE = 15  # Jump if more-than.
    JUMPMOREEQUAL = 24  # Jump if more-than or equal.
    JUMPREL = 19  # Jumps relatively to the current instruction.
    # IO:
    IN = 17
    OUT = 18
    # Imports:
    IMPORTFILE = 20  # Imports a file in the location specified.
    IMPORTLIB = 21  # Imports a library from the location specified.
    IMPORTSTDLIB = 22  # Importa a standard library.
