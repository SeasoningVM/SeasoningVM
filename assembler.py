#!/usr/bin/env python
# -*- coding: utf-8 -*-

from opcode import OPRAND


def prepare_file(file, memory_size):
    file.write(0xCAFE.to_bytes(2, byteorder='little'))
    file.write(memory_size.to_bytes(4, byteorder='little'))


if __name__ == "__main__":
    with open("example.sasm", "r") as asm:
        with open("example.sbc", "wb+") as bytecode:
            # prepare_file(bytecode, 64)
            for line in asm:
                # bytecode.write(bytes())

                if ";" not in line:
                    lines = line.split()

                    new_lines = []
                    for item in lines:
                        new_lines.append(item.replace(",", ""))
                    lines = new_lines

                    bytecode.write(bytes([OPRAND.__getitem__(lines[0])]))

                    for rest in lines[1:]:
                        bytecode.write(bytes([int(rest)]))

                    print(lines)
