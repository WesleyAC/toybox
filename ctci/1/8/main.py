#!/usr/bin/env python3

def is_rotation(s1, s2):
    return s1 in s2 + s2

if __name__ == "__main__":
    assert is_rotation("waterbottle", "erbottlewat")
    assert not is_rotation("abc", "def")
    assert is_rotation("abcdef", "defabc")
    print("Tests passed")
