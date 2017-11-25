from enum import Enum, auto


# OPCODE
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
    # TODO: OR = auto()
    # TODO: NOT = auto()


stack_pointer = 32
stack = [None] * stack_pointer
instruction_pointer = 0

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
    OPRAND.PUSH, 5,
    OPRAND.HALT
]

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
