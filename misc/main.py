#!/usr/bin/python3

import random
import string
import copy

def make_board(size=4, letters=None):
    if letters is None:
        letters = string.ascii_uppercase

    board = []

    for row in range(0,size):
        row_array = []
        for col in range(0,size):
            row_array.append(random.choice(letters))
        board.append(row_array)

    return board

def print_board(board):
    for row in board:
        print(" ".join(row))

words = []
with open("words") as wordfile:
    words = [x.upper() for x in wordfile.read().split("\n")[:-1]]

def check_path(board, path):
    word = [board[x[0]][x[1]] for x in path]
    return "".join(word) in words

def get_word_from_path(board, path):
    word = [board[x[0]][x[1]] for x in path]
    return word

def filter_word_list(prefix, wordlist):
    new_wordlist = []
    for word in wordlist:
        if word[0:len(prefix)] == prefix:
            new_wordlist.append(word)
    return new_wordlist

def find_word(board, wordlist=None, path=None):
    if wordlist is None:
        wordlist = words
    if path is None:
        for row in range(0,len(board)):
            for col in range(0,len(board)):
                find_word(board, wordlist=wordlist, path=[(row, col)])
    else:
        if len(path) > len(board)**2:
            return

        if check_path(board, path):
            print("{}\t{}".format(get_word_from_path(board, path), path))
        for row in range(path[-1][0]-1, path[-1][0]+2):
            for col in range(path[-1][1]-1, path[-1][1]+2):
                if (row, col) not in path:
                    if row >= 0 and row < len(board) and col >= 0 and col < len(board):
                        new_path = copy.copy(path)
                        new_path.append((row, col))

                        new_word_list = filter_word_list("".join(get_word_from_path(board, new_path)), wordlist)
                        if len(new_word_list) > 0:
                            find_word(board, wordlist=new_word_list, path=new_path)

if __name__ == "__main__":
    print(make_board())
    print(words)
