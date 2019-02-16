#!/usr/bin/python
# -*- coding: utf-8 -*-

CREDBG  = '\33[41m'
CEND = '\033[0m'
CWHITEBG  = '\33[47m'

def printCard(flip):
    if flip == None:
        return '\33[60m' + " \u25CF " + CEND

    CBG = ''
    if(flip.color == "red"):
       CBG = CREDBG
    else:
       CBG = CWHITEBG

    if flip.player == 1:
        PL = ' '
    else:
        PL = '\u0060'

    if not flip.dot:
      return CBG + " \u25CB" + PL + CEND
    else:
      return CBG + " \u25CF" + PL + CEND



def printBoard(board):
    print("\n")
    for i in range(12):
        tmp = ''
        for j in range(8):
          tmp += printCard(board[i][j])
        print(tmp)
