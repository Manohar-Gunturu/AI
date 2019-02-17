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


def check_winner_diag1(_card):
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
        return (True, match)
    else:
        return (False, match)


def check_winner_diag2(_card):
    (_row, _column) = _card.getposition()
    (tmprow, tmpcolumn) = (_row, _column)
    match = [0, 0]
    compare = [_card.color, _card.dot]
    # checking for color match
    while isValidcell(tmprow, tmpcolumn) and Board[tmprow][tmpcolumn] \
        is not None and Board[tmprow][tmpcolumn].color == compare[0]:
        match[0] += 1
        tmprow -= 1
        tmpcolumn -= 1

    # checking for dot match
    (tmprow, tmpcolumn) = (_row, _column)
    while isValidcell(tmprow, tmpcolumn) and Board[tmprow][tmpcolumn] \
        is not None and Board[tmprow][tmpcolumn].dot == compare[1]:
        match[1] += 1
        tmprow -= 1
        tmpcolumn -= 1

    # checking for color match
    (tmprow, tmpcolumn) = (_row + 1, _column + 1)
    while isValidcell(tmprow, tmpcolumn) and Board[tmprow][tmpcolumn] \
        is not None and Board[tmprow][tmpcolumn].color == compare[0]:
        match[0] += 1
        tmprow += 1
        tmpcolumn += 1

    # checking for dot match
    (tmprow, tmpcolumn) = (_row + 1, _column + 1)
    while isValidcell(tmprow, tmpcolumn) and Board[tmprow][tmpcolumn] \
        is not None and Board[tmprow][tmpcolumn].dot == compare[1]:
        match[1] += 1
        tmprow += 1
        tmpcolumn += 1

    if match[0] >= 4 or match[1] >= 4:
        return (True, match)
    else:
        return (False, match)


def check_winner_row(_card):
    (_row, _column) = _card.getposition()
    (compare1, compare) = (['', ''], ['', ''])
    match = [1, 1]
    row_tmp = 12
    iswin = [1,1]
    while (row_tmp - 1) >= 0 and (match[0] < 4 or match[1] < 4):
        row_tmp = row_tmp - 1
        if Board[row_tmp][_column] is None:
            break
        compare1[0] = Board[row_tmp][_column].color
        compare1[1] = Board[row_tmp][_column].dot
        if compare[0] != compare1[0]:
            compare[0] = compare1[0]
            iswin[0] = max(match[0], iswin[0])
            match[0] = 1
        else:
            match[0] = match[0] + 1

        if compare[1] != compare1[1]:
            compare[1] = compare1[1]
            match[1] = 1
            iswin[1] = max(match[1], iswin[1])
        else:
            match[1] = match[1] + 1

    iswin = [ max(iswin[0],match[0]), max(iswin[1],match[1])  ]
    if iswin[0] >= 4 or iswin[1] >= 4:
        return (True, iswin)
    else:
        return (False, iswin)


def check_winner_column(_card):
    (_row, _column) = _card.getposition()
    (compare, compare1) = (['', ''], ['', ''])
    match = [1, 1]
    column_tmp = 8
    iswin = [1,1]
    while (column_tmp - 1) >= 0 and (match[0] < 4 or match[1] < 4):
        column_tmp = column_tmp - 1
        if Board[_row][column_tmp] is None:
            iswin = [ max(iswin[0],match[0]), max(iswin[1],match[1])  ]
            (compare, compare1) = (['', ''], ['', ''])
            match = [1, 1]
            continue
        compare1[0] = Board[_row][column_tmp].color
        compare1[1] = Board[_row][column_tmp].dot
        if compare[0] != compare1[0]:
            compare[0] = compare1[0]
            iswin[0] = max(match[0], iswin[0])
            match[0] = 1
        else:
            match[0] = match[0] + 1

        if compare[1] != compare1[1]:
            compare[1] = compare1[1]
            iswin[1] = max(match[1], iswin[1])
            match[1] = 1
        else:
            match[1] = match[1] + 1
    iswin = [ max(iswin[0],match[0]), max(iswin[1],match[1])  ]
    if iswin[0] >= 4 or iswin[1] >= 4:
        return (True, iswin)
    else:
        return (False, iswin)

def whatMakesWin(stat):
    winby = stat[1]
    if not stat[0]:
        return [0,0]
    if winby[0] >= 4 and winby[1] >= 4:
        return [1,1]
    elif winby[0] >= 4:
        return [1,0]
    elif winby[1] >= 4:
        return [0,1]
    else:
        return [0,0]

def checkWinnerUtil(card):

    x1 = check_winner_column(card.left)
    x2 = check_winner_column(card.right)
    x3 = check_winner_row(card.left)
    x4 = check_winner_row(card.right)
    x5 = check_winner_diag1(card.left)
    x6 = check_winner_diag1(card.right)
    x7 = check_winner_diag2(card.left)
    x8 = check_winner_diag2(card.right)
    # wins[0] for colors and wins[1] for dots 
    wins = [0,0]
    if x1[0]:
        print("c.left")
        tmp = whatMakesWin(x1)
        wins = [ (x + y) for (x, y) in zip(wins,tmp)   ]
    if x2[0]:
        print("c.right")
        tmp = whatMakesWin(x2)
        wins = [ (x + y) for (x, y) in zip(wins,tmp)   ]
    if x3[0]:
        print("r.left")
        tmp = whatMakesWin(x3)
        wins = [ (x + y) for (x, y) in zip(wins,tmp)   ]
    if x4[0]:
        print("r.right")
        tmp = whatMakesWin(x4)
        wins = [ (x + y) for (x, y) in zip(wins,tmp)   ]
    if x5[0]:
        print("d.left")
        tmp = whatMakesWin(x5)
        wins = [ (x + y) for (x, y) in zip(wins,tmp)   ]

    if x6[0]:
        print("d.right")
        tmp = whatMakesWin(x6)
        wins = [ (x + y) for (x, y) in zip(wins,tmp)   ]

    if x7[0]:
        print("d.left")
        tmp = whatMakesWin(x7)
        wins = [ (x + y) for (x, y) in zip(wins,tmp)   ]

    if x8[0]:
        print("d.right")
        tmp = whatMakesWin(x8)
        wins = [ (x + y) for (x, y) in zip(wins,tmp)   ]
    
    return wins


def checkWinner(card, _choice, player):
    score = checkWinnerUtil(card)
   
    if all(v == 0 for v in score):
        return False

    if score[0] >= 1 and score[1] >= 1:  # it is draw so last player win
        print (player, ' won,- it is draw so last player win')
        return True
    elif score[0] >= 1:
        print ('Player ' , _choice['color'],' has won the game as he choosen color')
        return True
    elif score[1] >= 1:
        print ('Player ', _choice['dot'], ' has won the game as he choosen dot')
        return True
    else:
        return False


def isLegalMoveUtil(row, column, angle):
    if isValidcell(row, column) and Board[row][column] is not None:
        return False
    else:
        pass

    if row == 11:
        if angle == 0 or angle == 180:
            return Board[row][column + 1] is None
        elif angle == 90 or angle == 270:
            return Board[row - 1][column] is None
        else:
            return True

    if angle == 90 or angle == 270:
        if Board[row - 1][column] is None and Board[row + 1][column] \
            is not None:
            return True
        else:
            return False

    if angle == 0 or angle == 180:
        if Board[row][column + 1] is None and Board[row + 1][column
                + 1] is not None and Board[row + 1][column] is not None:
            return True
        else:
            return False


def isLegalMove(row, column, angle):
    isgood = isLegalMoveUtil(row, column, angle)
    if not isgood:
        print ('Sorry, Illegal place')
    return isgood

# to see if any card is hanging on an empty cell
def isLegalMove1(pos, angle):
    if Board[pos[0]][pos[1]]  == None and Board[pos[0] - 1][pos[1]] is not None:
        return False
    if Board[pos[2]][pos[3]]  == None and Board[pos[2] - 1][pos[3]] is not None:
        return False
    return True


def calc_turn(turn):
    if turn == 1:
        return 2
    else:
        return 1


player1_choice = input('Enter your Player 1(\u0060) choice either dot or color ').lower()
player2_choice = ('dot' if player1_choice == 'color' else 'color')
player_choices = {player1_choice: '1', player2_choice: '2'}
count = 1
recent_card = None;
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
        return (row, column, row, column + 1)
    elif angle == 90:
        return (row - 1, column, row, column)
    elif angle == 180:
        return (row, column + 1, row, column)
    elif angle == 270:
        return (row, column, row - 1, column)


while count <= 24:
    print ('Player ', whose_turn, ' turn')
    inp = input('Enter card details ').strip().split(' ')
    if inp[0] == '0' and inp[1] in number_angle:
        angle = number_angle[inp[1]]
    else:
        print ("Wrong place, kindly adviced to follow prof requirement")
        continue

    side = (1 if int(inp[1]) <= 4 else 2)
    (row, column) = getCellPosition([inp[2], inp[3]])
    card = Card(row, column, whose_turn, inp[1])
    card.config(side, angle, row, column)

    if not isLegalMove(row, column, angle):
        print ('Sorry not a good move')
        card = None
        continue
    pos = getPositionByAngle(angle, row, column)
    Board[pos[0]][pos[1]] = card.left.position(pos[0], pos[1])
    Board[pos[2]][pos[3]] = card.right.position(pos[2], pos[3])
    printBoard(Board)
    if checkWinner(card, player_choices, whose_turn):
        exit()
    recent_card = card
    count = count + 1
    print("count, ", count)
    whose_turn = calc_turn(whose_turn)


# if while loop exited then it means placing 24 cards is done so entering into recycling phase

def process_input():
    try:
        inp = input('Enter card details ').strip().split(' ')
        if inp[0].isdigit():
            print('Sorry invalid input')
            return ()
        lpos = getCellPosition([inp[0], inp[1]])
        rpos = getCellPosition([inp[2], inp[3]])
        npos = getCellPosition([inp[5], inp[6]])
        if isValidcell(*lpos) and isValidcell(*rpos) \
            and isValidcell(*npos):
            return lpos + rpos + (inp[4], ) + npos
    except (ValueError, IndexError):
        return ()

print("-------- Started recycling phase ------")

for i in range(36):
    print ('Player ', whose_turn, ' turn')
    inp = process_input()
    if len(inp) == 0:
        print('Recycling move input error')
        continue

    left = Board[inp[0]][inp[1]]
    right = Board[inp[2]][inp[3]]
    if left is None or right is None or left.card != right.card \
        or left.card == recent_card or not inp[4] in number_angle:
        print('That is an invalid card - or just recent card, or this red and black belongs to different cards')
        continue

    # check is destination cell is available or could be same

    angle = number_angle[inp[4]]

    # pos contains destination location of recycling move

    pos = getPositionByAngle(angle, inp[5], inp[6])
    dleft = Board[pos[0]][pos[1]]
    dright = Board[pos[2]][pos[3]]
    card_tmp = Board[inp[0]][inp[1]].card

    if inp[0] != 0:
        if(Board[inp[0] - 1][inp[1]] is not None and Board[inp[0] - 1][inp[1]].card != card_tmp ):
            print('Sorry it is an invalid recycling move - it has someting on top.l')            
            continue
    if inp[2] != 0:
        if(Board[inp[2] - 1][inp[3]] is not None and Board[inp[2] - 1][inp[3]].card != card_tmp ):
            print('Sorry it is an invalid recycling move - it has someting on top.r')   
            continue

    if not (dleft is None and dright is None or (dleft is None
            or dleft.card == left.card) and (dright is None
            or dright.card == right.card)):
        print('Sorry it is a invalid recycling move')
        continue

    if card_tmp.row != inp[5] or card_tmp.column != inp[6]:
        if card_tmp.o != inp[4]:
            print("you can put it back at a *different* position with the same orientation", card_tmp.o)
            continue

    if card_tmp.row == inp[5] and card_tmp.column == inp[6] and card_tmp.o == inp[4]:
        print("cannot put it back at the same position and with the same orientation ", card_tmp.o)
        continue

    # now do the recycling move
    # first remove the previous card
    Board[inp[0]][inp[1]] = None
    Board[inp[2]][inp[3]] = None

    side = (1 if int(inp[4]) <= 4 else 2)

    # create new card

    card = Card(pos[0], pos[1], whose_turn, inp[4])
    card.config(side, angle, pos[0], pos[1])
    if not isLegalMove(inp[5], inp[6], angle):
        print('Sorry not a good move')
        card = None
        Board[inp[0]][inp[1]] = card_tmp.left
        Board[inp[2]][inp[3]] = card_tmp.right
        continue

    Board[pos[0]][pos[1]] = card.left.position(pos[0], pos[1])
    Board[pos[2]][pos[3]] = card.right.position(pos[2], pos[3])

    """
    # check if removing card leave borad in illegal state, just check if the card above cells valid else revoke the move
    if not isLegalMove1(inp, card_tmp.rotation):
        print('This move leaves board in illegal state, so reverting back!! :)')
        Board[pos[0]][pos[1]] = None
        Board[pos[2]][pos[3]] = None
        Board[inp[0]][inp[1]] = card_tmp.left
        Board[inp[2]][inp[3]] = card_tmp.right
        continue
    """ 
    printBoard(Board)
    recent_card = card
    if checkWinner(card, player_choices, whose_turn):
        exit()
    count = count + 1
    whose_turn = calc_turn(whose_turn)

print('Match is a draw, ;)')
