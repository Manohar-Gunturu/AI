#!/usr/bin/python
# -*- coding: utf-8 -*-

CREDBG = '\33[41m'
CEND = '\033[0m'
CWHITEBG = '\33[47m'


def printCard(flip_):
    if flip_ == 0:
        return '\33[60m' + " \u25CF " + CEND
    CBG = ''
    if flip_ % 100 == 2 or flip_ % 100 == 4:
       CBG = CREDBG
    else:
       CBG = CWHITEBG

    if flip_ % 100 == 2 or flip_ % 100 == 1:
        return CBG + " \u25CB " + CEND
    else:
        return CBG + " \u25CF " + CEND


def printBoard(board):
    print("\n")
    tmp = ''
    for p in range(96):
        if p % 8 == 0:
            print(tmp)
            tmp = ''
        tmp += printCard(board[p])
    print(tmp)

