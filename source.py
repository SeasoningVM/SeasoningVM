from enum import Enum, auto


class OPCodes(Enum):
    HALT = auto(),  # Stops the program.
    PUSH = auto(),  # Push a value onto the stack.
    # Math:
    ADD = auto(),  # Add the values in the stack.
    SUB = auto(),  # Subtracts the values in the stack.
    MUL = auto(),  # Multiplies the values in the stack.
    DIV = auto(),  # Divides the values in the stack.
    MOD = auto(),  # Finds the remainder of a division.
    # Operations:
    LESS = auto(),  # Determines if a value is less than another.



stack_pointer = 100
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
    OPCodes.LESS,  # True
    OPCodes.HALT
]

work = True
while work:
    instruction = program[instruction_pointer]
    instruction_pointer += 1

    if instruction == OPCodes.HALT:
        work = False

    elif instruction == OPCodes.PUSH:
        stack_pointer -= 1
        stack[stack_pointer] = program[instruction_pointer]
        instruction_pointer += 1

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

    elif instruction == OPCodes.LESS:
        value = stack[stack_pointer]
        stack_pointer += 1
        stack[stack_pointer] = stack[stack_pointer] < value
print(stack[stack_pointer])
