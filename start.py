#!/usr/bin/python
# -*- coding: utf-8 -*-

from Card import Card
from Printer import printBoard
from sys import exit

Board = [[None for x in range(8)] for y in range(12)]


# position must be A4 or C5 like that

def getCellPosition(position):
    column = ord(position[0].upper())
    column = column - 65
    row = 12 - int(position[1])
    return (row, column)


def isValidcell(row, column):
    if 11 >= row >= 0 and 7 >= column >= 0:
        return True
    else:
        return False


def check_winner_diag(_card):
    (_row, _column) = _card.getposition()
    (tmprow, tmpcolumn) = (_row, _column)
    match = [0, 0]
    compare = [_card.color, _card.dot]

    # checking for color match

    while isValidcell(tmprow, tmpcolumn) and Board[tmprow][tmpcolumn] \
        is not None and Board[tmprow][tmpcolumn].color == compare[0]:
        match[0] += 1
        tmprow -= 1
        tmpcolumn += 1

    # checking for dot match

    (tmprow, tmpcolumn) = (_row, _column)
    while isValidcell(tmprow, tmpcolumn) and Board[tmprow][tmpcolumn] \
        is not None and Board[tmprow][tmpcolumn].dot == compare[1]:
        match[1] += 1
        tmprow -= 1
        tmpcolumn += 1

    # checking for color match

    (tmprow, tmpcolumn) = (_row + 1, _column - 1)
    while isValidcell(tmprow, tmpcolumn) and Board[tmprow][tmpcolumn] \
        is not None and Board[tmprow][tmpcolumn].color == compare[0]:
        match[0] += 1
        tmprow += 1
        tmpcolumn -= 1

    # checking for dot match

    (tmprow, tmpcolumn) = (_row + 1, _column - 1)
    while isValidcell(tmprow, tmpcolumn) and Board[tmprow][tmpcolumn] \
            is not None and Board[tmprow][tmpcolumn].dot == compare[1]:
        match[1] += 1
        tmprow += 1
        tmpcolumn -= 1

    if match[0] >= 4 or match[1] >= 4:
        return True, match
    else:
        return False, match


def check_winner_row(_card):
    (_row, _column) = _card.getposition()
    (compare1, compare) = (['', ''], ['', ''])
    match = [1, 1]
    row_tmp = 12
    while row_tmp >= 0 and match[0] < 4 and match[1] < 4:
        row_tmp = row_tmp - 1
        if Board[row_tmp][_column] is None:
            break
        compare1[0] = Board[row_tmp][_column].color
        compare1[1] = Board[row_tmp][_column].dot
        if compare[0] != compare1[0]:
            compare[0] = compare1[0]
            match[0] = 1
        else:
            match[0] = match[0] + 1
        if compare[1] != compare1[1]:
            compare[1] = compare1[1]
            match[1] = 1
        else:
            match[1] = match[1] + 1

    if match[0] >= 4 or match[1] >= 4:
        return True, match
    else:
        return False, match


def check_winner_column(_card):
    (_row, _column) = _card.getposition()
    (compare, compare1) = (['', ''], ['', ''])
    match = [1, 1]
    column_tmp = 8
    while column_tmp >= 0 and match[0] < 4 and match[1] < 4:
        column_tmp = column_tmp - 1
        if Board[_row][column_tmp] is None:
            (compare, compare1) = (['', ''], ['', ''])
            match = [1, 1]
            continue

        compare1[0] = Board[_row][column_tmp].color
        compare1[1] = Board[_row][column_tmp].dot
        if compare[0] != compare1[0]:
            compare[0] = compare1[0]
            match[0] = 1
        else:
            match[0] = match[0] + 1

        if compare[1] != compare1[1]:
            compare[1] = compare1[1]
            match[1] = 1
        else:
            match[1] = match[1] + 1

    if match[0] >= 4 or match[1] >= 4:
        return True, match
    else:
        return False, match


def checkWinnerUtil(card):

    x = check_winner_column(card.left)
    if x[0]:
        return x
    x = check_winner_column(card.right)
    if x[0]:
        return x
    x = check_winner_row(card.left)
    if x[0]:
        return x
    x = check_winner_row(card.right)
    if x[0]:
        return x
    x = check_winner_diag(card.left)
    if x[0]:
        return x
    x = check_winner_diag(card.right)
    if x[0]:
        return x
    else:
        return ()


def checkWinner(card, _choice, player):
    how_he_won = checkWinnerUtil(card)
    if len(how_he_won) == 0:
        return False

    score = how_he_won[1]
    if how_he_won[0]:
        if score[0] >= 4 and score[1] >= 4:  # it is draw so last player win
            print(player, ' won,- it is draw so last player win')
            return True
        elif score[0] >= 4:
            print(_choice['color'],' has won the game as he choosen color')
            return True
        elif score[1] >= 4:
            print(_choice['dot'], ' has won the game as he choosen dot')
            return True
        else:
            return False


def isLegalMoveUtil(row, column, angle):

    if isValidcell(row, column) and Board[row][column] is not None:
        return False
    else:
        pass

    if row == 11:
        return True

    if angle == 90 or angle == 270:
        if Board[row - 1][column] is None and Board[row + 1][column] \
                is not None:
            return True
        else:
            return False

    if angle == 0 or angle == 180:
        if Board[row][column + 1] is None and Board[row + 1][column + 1] \
                is not None and Board[row + 1][column] is not None:
            return True
        else:
            return False


def isLegalMove(row, column, angle):
    isgood = isLegalMoveUtil(row, column, angle)
    if not isgood:
        print ('Sorry, Illegal place')
    return isgood


def calc_turn(turn):
    if turn == 1:
        return 2
    else:
        return 1


player1_choice = input('Enter your Player 1 choice either dot or color ').lower()
player2_choice = ('dot' if player1_choice == 'color' else 'color')
player_choices = {player1_choice: '1', player2_choice: '2'}
count = 0
whose_turn = 1
number_angle = {
    '1': 0,
    '2': 90,
    '3': 180,
    '4': 270,
    '5': 0,
    '6': 90,
    '7': 180,
    '8': 270,
    }


def getPositionByAngle(angle, row, column):
    if angle == 0:
        return(row, column, row, column + 1)
    elif angle == 90:
        return(row - 1, column, row, column)
    elif angle == 180:
        return(row, column + 1, row, column)
    elif angle == 270:
        return(row, column, row - 1, column)


while count <= 24:
    print('Player ', whose_turn, ' turn')
    inp = input('Enter card details ').strip().split(' ')
    if inp[0] == '0':
        angle = number_angle[inp[1]]
    else:
        print("I hope u're doing Recycling Moves, but have to complete placing 24 cards")
        continue

    side = (1 if int(inp[1]) <= 4 else 2)
    (row, column) = getCellPosition([inp[2], inp[3]])
    card = Card(row, column, whose_turn)
    card.config(side, angle, row, column)

    if not isLegalMove(row, column, angle):
        print("Sorry not a good move")
        continue

    pos = getPositionByAngle(angle, row, column)
    Board[pos[0]][pos[1]] = card.left.position(pos[0], pos[1])
    Board[pos[2]][pos[3]] = card.right.position(pos[2], pos[3])
    printBoard(Board)
    if checkWinner(card, player_choices, whose_turn):
        exit()
    count = count + 1
    whose_turn = calc_turn(whose_turn)

# if while loop exited then it means placing 24 cards is done so entering into recycling phase


def process_input():
    try:
        inp = input('Enter card details ').strip().split(' ')
        if inp[0].isdigit():
            print("Sorry invalid input")
            return ()
        lpos = getCellPosition([inp[0], inp[1]])
        rpos = getCellPosition([inp[2], inp[3]])
        npos = getCellPosition([inp[5], inp[6]])
        if isValidcell(lpos) and isValidcell(rpos) and isValidcell(npos):
            return lpos + rpos + (inp[4]) + npos
    except ValueError:
        return ()


for i in range(56):
    print('Player ', whose_turn, ' turn')
    inp = process_input()
    if len(inp) == 0:
        print("Recycling move input error")
        continue

    left = Board[inp[0]][inp[1]]
    right = Board[inp[2]][inp[3]]
    if left is None or right is None or left.card != right.card or left.card.player != whose_turn:
        print("That is an invalid card")
        continue
    # check is destination cell is available or could be same
    angle = number_angle[inp[4]]
    pos = getPositionByAngle(angle, inp[5], inp[6])
    dleft = Board[pos[0]][pos[1]]
    dright = Board[pos[2]][pos[3]]
    if not ((dleft is None and dright is None) or
            ((dleft is None or (dleft.card == left.card)) and
            ((dright is None or (dright.card == right.card))))):
        print("Sorry it is a invalid recycling view")
        continue

    # now do the recycling move
    # first remove the previous card
    Board[inp[0]][inp[1]] = None
    Board[inp[2]][inp[3]] = None
    side = (1 if int(inp[4]) <= 4 else 2)
    # create new card

    card = Card(pos[0], pos[1], whose_turn)
    card.config(side, angle, pos[0], pos[1])

    if not isLegalMove(pos[0], pos[1], angle):
        print("Sorry not a good move")
        continue
    Board[pos[0]][pos[1]] = card.left.position(pos[0], pos[1])
    Board[pos[2]][pos[3]] = card.right.position(pos[2], pos[3])
    printBoard(Board)
    if checkWinner(card, player_choices, whose_turn):
        break
    count = count + 1
    whose_turn = calc_turn(whose_turn)


print("Match is a draw, ;) ")
