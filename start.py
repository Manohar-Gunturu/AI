#!/usr/bin/python
# -*- coding: utf-8 -*-

from Card import Card
from Printer import printBoard

Board = [[None for x in range(8)] for y in range(12)]


# position must be A4 or C5 like that

def getCellPosition(position):
    column = ord(position[0].upper())
    column = column - 65
    row = 12 - int(position[1])
    return (row, column)


def isValidcell(row, column):
    if (row <= 11 and row >= 0) and (column >= 0 and row <= 7):
        return True
    else:
        return False


def check_winner_diag(_card, _choice):
    (_row, _column) = _card.getposition()
    tmprow, tmpcolumn = _row, _column
    match = 0
    compare = getattr(_card, _choice)
    while isValidcell(tmprow, tmpcolumn) and Board[tmprow][tmpcolumn] is not None and \
            getattr(Board[tmprow][tmpcolumn], _choice) == compare:
        match += 1
        tmprow += 1
        tmpcolumn += 1

    tmprow, tmpcolumn = _row - 1, _column - 1
    while isValidcell(tmprow, tmpcolumn) and Board[tmprow][tmpcolumn] is not None and \
            getattr(Board[tmprow][tmpcolumn], _choice) == compare:
        match += 1
        tmprow -= 1
        tmpcolumn -= 1
    if match >= 4:
        return True
    else:
        return False


def check_winner_row(_card, _choice):
    (_row, _column) = _card.getposition()
    compare1, compare = '', ''
    match = 1
    row_tmp = 12
    while row_tmp >= 0 and match < 4:
        row_tmp = row_tmp - 1
        if Board[row_tmp][_column] is None:
            match = 0
            continue
        compare1 = getattr(Board[row_tmp][_column], _choice)
        if compare != compare1:
            compare = compare1
            match = 1
        else:
            match = match + 1

    if match >= 4:
        return True
    else:
        return False


def check_winner_column(_card, _choice):
    (_row, _column) = _card.getposition()
    compare, compare1 = '', ''
    match = 1
    column_tmp = 8
    while column_tmp >= 0 and match < 4:
        column_tmp = column_tmp - 1
        if Board[_row][column_tmp] is None:
            break
        compare1 = getattr(Board[_row][column_tmp], _choice)
        if compare != compare1:
            compare = compare1
            match = 1
        else:
            match = match + 1

    if match >= 4:
        return True
    else:
        return False


def checkWinner(card, hisChoice):
    if check_winner_column(card.left, hisChoice) or check_winner_column(card.right, hisChoice):
        return True
    elif check_winner_row(card.left, hisChoice) or check_winner_row(card.right, hisChoice):
        return True
    elif check_winner_diag(card.left, hisChoice) or check_winner_diag(card.right, hisChoice):
        return True
    else:
        return False


def isLegalMoveUtil(row, column, angle):
    if Board[row][column] is not None:
        return False
    else:
        pass

    if row == 11:
        return True

    if angle == 90 or angle == 270:
        if Board[row + 1][column] is not None:
            return True
        else:
            return False

    if angle == 0 or angle == 180:
        if Board[row + 1][column] is not None:
            return True
        else:
            return False


def isLegalMove(row, column, angle):
    isgood = isLegalMoveUtil(row, column, angle)
    if not isgood:
        print('Sorry, Illegal place')
    return isgood


def calc_turn(turn):
    if turn == 1:
        return 2
    else:
        return 1


player1_choice = input("Enter your Player 1 choice either dot or color ")
player2_choice = "dot" if player1_choice == "color" else "color"
player_choices = (player1_choice, player2_choice)
count = 0
whose_turn = 1
number_angle = {"1": 0, "2": 90, "3": 180, "4": 270, "5": 0, "6": 90, "7": 180, "8": 270}
while count <= 24:
    print('Player ', whose_turn, ' turn')
    inp = input("Enter card details ").split(" ")
    if inp[0] == "0":
        angle = number_angle[inp[1]]

    side = 1 if int(inp[1]) <= 4 else 2
    (row, column) = getCellPosition([inp[2], inp[3]])
    card = Card(row, column)
    card.config(side, angle, row, column)

    if not isLegalMove(row, column, angle):
        continue

    if angle == 0:
        Board[row][column] = card.left.position(row, column)
        if not isLegalMove(row, column + 1, angle):
            continue
        Board[row][column + 1] = card.right.position(row, column + 1)
    elif angle == 90:
        Board[row][column] = card.right.position(row, column)
        if not isLegalMove(row - 1, column, angle):
            continue
        Board[row - 1][column] = card.left.position(row - 1, column)
    elif angle == 180:
        Board[row][column] = card.right.position(row, column)
        if not isLegalMove(row, column + 1, angle):
            continue
        Board[row][column + 1] = card.left.position(row, column + 1)
    elif angle == 270:
        Board[row][column] = card.left.position(row, column)
        if not isLegalMove(row - 1, column, angle):
            continue
        Board[row - 1][column] = card.right.position(row - 1, column)
    printBoard(Board)
    if checkWinner(card, player_choices[whose_turn - 1]):
        print('Winner is ', whose_turn)
        break
    count = count + 1
    whose_turn = calc_turn(whose_turn)

# if while loop exited then it means placing 24 cards is done so entering into recycling phase

