#!/usr/bin/env python3

class StackSet:
    def __init__(self, max_height):
        self.stacks = [[]]
        self.max_height = max_height

    def push(self, v):
        if len(self.stacks[-1]) < self.max_height:
            self.stacks[-1].append(v)
        else:
            self.stacks.append([v])

    def pop(self):
        out = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return out

if __name__ == "__main__":
    a = StackSet(3)
    a.push(1)
    a.push(2)
    a.push(5)
    a.push(7)
    a.push(9)
    assert a.pop() == 9
    assert a.pop() == 7
    assert a.pop() == 5
    assert a.pop() == 2
    assert a.pop() == 1
    print("Tests passed")
