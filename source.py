from enum import Enum

class Actions(Enum):
    HALT = 0,
    PUSH = 1,
    ADD = 2,

stack_pointer = 100
stack = [0] * stack_pointer
instruction_pointer = 0

program = [
    Actions.PUSH, 10,
    Actions.PUSH, 20,
    Actions.ADD,
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

    elif instruction == Actions.ADD:
        stack[stack_pointer] += stack[stack_pointer+1]

print(stack[stack_pointer])