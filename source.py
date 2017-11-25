from enum import Enum


class Actions(Enum):
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
    Actions.PUSH, 10,
    Actions.PUSH, 20,
    Actions.ADD,  # 30
    Actions.PUSH, 5,
    Actions.SUB,  # 25
    Actions.PUSH, 2,
    Actions.MUL,  # 50
    Actions.PUSH, 2,
    Actions.DIV,  # 25
    Actions.PUSH, 3,
    Actions.MOD,
    Actions.HALT
]

work = True
while work:
    instruction = program[instruction_pointer]
    instruction_pointer += 1

    if instruction == Actions.HALT:
        work = False

    elif instruction == Actions.PUSH:
        stack_pointer -= 1
        stack[stack_pointer] = program[instruction_pointer]
        instruction_pointer += 1

    elif instruction == Actions.ADD:
        value = stack[stack_pointer]
        stack_pointer += 1
        stack[stack_pointer] += value

    elif instruction == Actions.SUB:
        value = stack[stack_pointer]
        stack_pointer += 1
        stack[stack_pointer] -= value

    elif instruction == Actions.MUL:
        value = stack[stack_pointer]
        stack_pointer += 1
        stack[stack_pointer] *= value

    elif instruction == Actions.DIV:
        value = stack[stack_pointer]
        stack_pointer += 1
        stack[stack_pointer] //= value

    elif instruction == Actions.MOD:
        value = stack[stack_pointer]
        stack_pointer += 1
        stack[stack_pointer] %= value

print(stack[stack_pointer])
