#!/usr/bin/env python3

def rle(s):
    new_s = ""
    current_c = s[0]
    count = 0
    for c in s:
        if c != current_c:
            new_s = "{}{}{}".format(new_s, current_c, count)
            count = 0
            current_c = c
        count += 1
    new_s = "{}{}{}".format(new_s, current_c, count)
    if len(new_s) < len(s):
        return new_s
    else:
        return s

if __name__ == "__main__":
    assert rle("aabcccccaaa") == "a2b1c5a3"
    assert rle("abc") == "abc"
    assert rle("aaaaaa") == "a6"
    print("Tests passed")
