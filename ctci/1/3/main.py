#!/usr/bin/env python3

def urlify(s):
    return s.replace(" ", "%20")

if __name__ == "__main__":
    assert urlify("a b c") == "a%20b%20c"
    assert urlify("   ") == "%20%20%20"
    assert urlify("what") == "what"
    print("Tests passed")
