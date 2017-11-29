#!/usr/bin/env python
# -*- coding: utf-8 -*-


def assemble(file, memory_size):
    file.write(0xCAFE.to_bytes(2, byteorder='little'))
    file.write(memory_size.to_bytes(4, byteorder='little'))


if __name__ == "__main__":
    with open("example.sbc", "wb+") as bytecode:
        assemble(bytecode, 64)
