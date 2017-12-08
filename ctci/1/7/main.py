#!/usr/bin/env python3

def rotate(arr):
    new_arr = []
    for i in range(len(arr)-1, -1, -1):
        new_arr.append([arr[x][i] for x in range(len(arr))])
    return new_arr

#TODO(Wesley) inplace version

if __name__ == "__main__":
    i = [[1,2,3],
         [4,5,6],
         [7,8,9]]
    assert rotate(i) == [[3,6,9],[2,5,8],[1,4,7]]
    print("Tests passed")
