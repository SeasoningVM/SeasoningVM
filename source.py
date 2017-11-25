from enum import Enum


class OPCodes(Enum):
    HALT = 0,
    PUSH = 1,  # Push a value onto the stack.
    # Math:
    ADD = 2,  # Add the values in the stack.
    SUB = 3,  # Subtracts the values in the stack.
    MUL = 4,  # Multiplies the values in the stack.
    DIV = 5,  # Divides the values in the stack.
    MOD = 6,  # Finds the remainder of a division.



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
    OPCodes.MOD,
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

print(stack[stack_pointer])
