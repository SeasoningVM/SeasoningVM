from enum import Enum, auto


class OPCodes(Enum):
    HALT = auto()  # Stops the program.
    # Stack Modifications:
    PUSH = auto()  # Pushes a value onto the stack.
    POP = auto()  # Pops a value from the stack.
    # Stack Movement:
    MOVE = auto()  # Moves a value to the stack.
    JUMP = auto()  # Jumps to an instruction.
    # Math:
    ADD = auto()  # Add the values in the stack.
    SUB = auto()  # Subtracts the values in the stack.
    MUL = auto()  # Multiplies the values in the stack.
    DIV = auto()  # Divides the values in the stack.
    MOD = auto()  # Finds the remainder of a division.
    # Operations:
    LESS = auto()  # Determines if a value is less than another.
    MORE = auto()  # Determines if a value is more than another.
    EQUAL = auto()  # Determines if a value equals another.
    #
    AND = auto()
    OR = auto()
    NOT = auto()



stack_pointer = 32
stack = [0] * stack_pointer
instruction_pointer = 0

program = [
    OPCodes.PUSH, 10,
    OPCodes.PUSH, 20,
    OPCodes.ADD,  # 30
    OPCodes.PUSH, 5,
    OPCodes.SUB,  # 25
    OPCodes.PUSH, 2,
    OPCodes.MUL,  # 50
    OPCodes.PUSH, 2,
    OPCodes.DIV,  # 25
    OPCodes.PUSH, 3,
    OPCodes.MOD,  # 1
    OPCodes.PUSH, 7,
    OPCodes.LESS,  # True/1
    OPCodes.PUSH, 5,
    OPCodes.MORE,  # False/0
    OPCodes.PUSH, 0,
    OPCodes.EQUAL,  # True/1
    # OPCodes.JUMP, 1,  # Infinite loop.
    # OPCodes.JUMP, 28,  # Jumps to the end.
    OPCodes.HALT
]

while True:
    instruction = program[instruction_pointer]  # The current instruction is at the instruction pointer.
    instruction_pointer += 1  # Increase the instruction pointer (move down the list).

    if instruction == OPCodes.HALT:
        break

    # Stack Modifications:

    elif instruction == OPCodes.PUSH:
        stack_pointer -= 1
        stack[stack_pointer] = program[instruction_pointer]
        instruction_pointer += 1

    # Stack Movement:

    elif instruction == OPCodes.JUMP:
        instruction_pointer = program[instruction_pointer]

    # Math:

    elif instruction == OPCodes.ADD:
        value = stack[stack_pointer]
        stack_pointer += 1
        stack[stack_pointer] += value

    elif instruction == OPCodes.SUB:
        value = stack[stack_pointer]
        stack_pointer += 1
        stack[stack_pointer] -= value

    elif instruction == OPCodes.MUL:
        value = stack[stack_pointer]
        stack_pointer += 1
        stack[stack_pointer] *= value

    elif instruction == OPCodes.DIV:
        value = stack[stack_pointer]
        stack_pointer += 1
        stack[stack_pointer] //= value

    elif instruction == OPCodes.MOD:
        value = stack[stack_pointer]
        stack_pointer += 1
        stack[stack_pointer] %= value

    # Operations:

    elif instruction == OPCodes.LESS:
        value = stack[stack_pointer]
        stack_pointer += 1
        stack[stack_pointer] = int(stack[stack_pointer] < value)

    elif instruction == OPCodes.MORE:
        value = stack[stack_pointer]
        stack_pointer += 1
        stack[stack_pointer] = int(stack[stack_pointer] > value)

    elif instruction == OPCodes.EQUAL:
        value = stack[stack_pointer]
        stack_pointer += 1
        stack[stack_pointer] = int(stack[stack_pointer] == value)

print(stack)
print(stack[stack_pointer])
