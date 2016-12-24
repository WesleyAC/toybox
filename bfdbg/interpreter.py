#!/usr/bin/env python3
import sys

from data import BrainfuckData

class BrainfuckProgram(object):
    """
    This class represents a brainfuck program.

    This takes a brainfuck program as a string in it's initializer.

    It provides a .step() method to step through execution.
    """
    def __init__(self, program, print_output=False):
        self.data = BrainfuckData()
        self.prog = self._strip(program)
        self.print_output = print_output

        self.dptr = 0
        self.pptr = 0
        self.output = []
        self.depth = 0
        self.done = False

    def step(self):
        self.done = self.pptr > len(self.prog) - 1
        if not self.done:
            self._commands[self.prog[self.pptr]](self)

    def _strip(self, prog):
        return [c for c in prog if c in self._commands]

    def _plus(self):
        self.data[self.dptr] += 1
        self.pptr += 1

    def _minus(self):
        self.data[self.dptr] -= 1
        self.pptr += 1

    def _left(self):
        self.dptr -= 1
        if (self.dptr < 0):
            raise IndexError()
        self.pptr += 1

    def _right(self):
        self.dptr += 1
        self.pptr += 1

    def _dot(self):
        self.output.append(self.data[self.dptr])
        if self.print_output:
            print(chr(self.output[-1]), end="")
        self.pptr += 1

    def _comma(self):
        # TODO(Wesley) input
        self.pptr += 1

    def _open_bracket(self):
        lastdepth = self.depth
        self.depth += 1
        if self.data[self.dptr] == 0:
            while (self.depth != lastdepth):
                self.pptr += 1
                if self.prog[self.pptr] == "[":
                    self.depth += 1
                elif self.prog[self.pptr] == "]":
                    self.depth -= 1;
        self.pptr += 1

    def _close_bracket(self):
        lastdepth = self.depth
        self.depth -= 1
        if self.data[self.dptr] != 0:
            while (self.depth != lastdepth):
                self.pptr -= 1
                if self.prog[self.pptr] == "[":
                    self.depth += 1
                elif self.prog[self.pptr] == "]":
                    self.depth -= 1;
        self.pptr += 1


    _commands = {
        "+": _plus,
        "-": _minus,
        "<": _left,
        ">": _right,
        ".": _dot,
        ",": _comma,
        "[": _open_bracket,
        "]": _close_bracket
    }

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Wrong number of parameters!\n"
              "Usage: {} filename.bf".format(sys.argv[0]))
        sys.exit(1)
    prog = open(sys.argv[1]).read()
    bf = BrainfuckProgram(prog, print_output=True)
    while (not bf.done):
        bf.step()
