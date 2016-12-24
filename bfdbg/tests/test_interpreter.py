import sys
import os

parent_dir = os.path.dirname(os.path.realpath(__file__)) + "/../"
sys.path.append(parent_dir) # a bit of a hack, but it makes the import the same
from interpreter import BrainfuckProgram

class TestInterpreter:
    def test_programs(self):
        test_progs = {
                    "":              [],
                    ".":             [0],
                    "+.":            [1],
                    "++.":           [2],
                    "+++[-].":       [0],
                    "+++[+].":       [0],
                    "+++.>.":        [3,0],
                    "+[.+]":         [n for n in range(1, 256)],
                    "+>++>+++.<.<.": [3,2,1]
                }
        for test_prog in test_progs:
            prog = BrainfuckProgram(test_prog)
            while (not prog.done):
                prog.step()
            assert prog.output == test_progs[test_prog]
