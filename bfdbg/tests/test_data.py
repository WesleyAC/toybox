import sys
import os

parent_dir = os.path.dirname(os.path.realpath(__file__)) + "/../"
sys.path.append(parent_dir) # a bit of a hack, but it makes the import the same
from data import BrainfuckData

class TestData:
    def test_resizable(self):
        data = BrainfuckData()
        assert len(data) == 0
        data[9] = 42
        assert len(data) == 10
        tmp = data[49]
        assert len(data) == 50

    def test_store_values(self):
        data = BrainfuckData()
        data[0] = 42
        assert data[0] == 42
        data[0] = 16
        assert data[0] == 16

    def test_overflow(self):
        data = BrainfuckData()
        data[0] = 255
        assert data[0] == 255
        data[0] += 1
        assert data[0] == 0

    def test_underflow(self):
        data = BrainfuckData()
        data[0] = -1
        assert data[0] == 255
