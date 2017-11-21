#!/usr/bin/env python3

def is_palindrome_permutation(s):
    chars = {}
    for char in s:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    num_odds = 0
    for n in chars.values():
        if n%2 != 0:
            num_odds += 1
    return num_odds <= 1

if __name__ == "__main__":
    assert is_palindrome_permutation("tactcoa")
    assert is_palindrome_permutation("aabb")
    assert is_palindrome_permutation("qwerqwtyerty")
    assert not is_palindrome_permutation("abcdef")
    print("Tests passed")
