#!/usr/bin/env python3

def is_permutation(s1, s2):
    if len(s1) != len(s2): return False
    chars1 = {}
    chars2 = {}
    for i in range(len(s1)):
        if s1[i] in chars1:
            chars1[s1[i]] += 1
        else:
            chars1[s1[i]] = 1
        if s2[i] in chars2:
            chars2[s2[i]] += 1
        else:
            chars2[s2[i]] = 1
    return chars1 == chars2

if __name__ == "__main__":
    assert is_permutation("abc", "cab")
    assert is_permutation("test", "test")
    assert is_permutation("qwerty", "eytwqr")
    assert not is_permutation("abc", "zba")
    assert not is_permutation("abc", "acab")
    print("Tests passed")
