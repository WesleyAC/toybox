#!/usr/bin/env python3

class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, v):
        self.stack.append(v)
        try:
            self.mins.append(min(v, self.mins[-1]))
        except IndexError:
            self.mins.append(v)

    def pop(self):
        self.mins.pop()
        return self.stack.pop()

    def min(self):
        return self.mins[-1]

if __name__ == "__main__":
    a = MinStack()
    a.push(1)
    assert a.min() == 1
    a.push(5)
    assert a.min() == 1
    a.push(2)
    assert a.min() == 1
    a.pop()
    assert a.min() == 1
    a.pop()
    assert a.min() == 1
    a.pop()
    a.push(7)
    assert a.min() == 7
    a.push(2)
    assert a.min() == 2
    print("Tests passed")

