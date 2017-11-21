#!/usr/bin/env python3

def one_away(s, target):
    if len(s) == len(target):
        # Replace
        diffs = 0
        for i in range(len(s)):
            if s[i] != target[i]:
                diffs += 1
        return diffs <= 1
    elif len(s)-1 == len(target):
        # Delete
        deleted = 0
        for i in range(len(target)):
            if s[i] != target[i]:
                s = s[:i] + s[i+1:]
                deleted += 1
            return deleted <= 1
    elif len(s)+1 == len(target):
        # Insert
        inserted = 0
        for i in range(len(target)):
            if s[i] != target[i]:
                s = s[:i] + target[i] + s[i:]
                inserted += 1
            return inserted <= 1
    else:
        return False

if __name__ == "__main__":
    assert one_away("pale", "ple")
    assert one_away("pales", "pale")
    assert one_away("pale", "pales")
    assert one_away("pale", "bale")
    assert not one_away("pale", "bake")
    print("Tests passed")
