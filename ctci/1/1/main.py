#!/usr/bin/env python3

def is_unique(s):
    return len(s) == len(set(s))

if __name__ == "__main__":
    assert is_unique("abcdef")
    assert not is_unique("deadbeef")
    print("Tests passed")
