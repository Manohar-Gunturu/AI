Board = []

for i1 in range(96):
    Board.append(0)

default_track = [11, 11, 11, 11, 11, 11, 11, 11]

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


def c_color(row, column, board_=Board):
    pos = state_conv(row, column)
    if board_[pos] == 0:
        return -1
    if board_[pos] % 100 == 2 or board_[pos] % 100 == 4:
        return "red"
    else:
        return "white"


def c_dot(row, column,  board_=Board):
    pos = state_conv(row, column)
    if board_[pos] == 0:
        return -1
    if board_[pos] % 100 == 3 or board_[pos] % 100 == 4:
        return 1
    else:
        return 0


def check_winner_diag1(_card, board_=Board):
    (_row, _column) = _card
    (tmprow, tmpcolumn) = (_row, _column)
    match = [0, 0]
    compare = [c_color(tmprow, tmpcolumn, board_), c_dot(tmprow, tmpcolumn, board_)]

    # checking for color match
    while isValidcell(tmprow, tmpcolumn) and state_conv1(tmprow, tmpcolumn, board_) != 0 \
            and c_color(tmprow, tmpcolumn, board_) == compare[0]:
        match[0] += 1
        tmprow -= 1
        tmpcolumn += 1

    # checking for dot match

    (tmprow, tmpcolumn) = (_row, _column)
    while isValidcell(tmprow, tmpcolumn) and state_conv1(tmprow, tmpcolumn, board_) != 0 \
            and c_dot(tmprow, tmpcolumn, board_) == compare[1]:
        match[1] += 1
        tmprow -= 1
        tmpcolumn += 1

    # checking for color match

    (tmprow, tmpcolumn) = (_row + 1, _column - 1)
    while isValidcell(tmprow, tmpcolumn) and state_conv1(tmprow, tmpcolumn) != 0 \
            and c_color(tmprow, tmpcolumn) == compare[0]:
        match[0] += 1
        tmprow += 1
        tmpcolumn -= 1

    # checking for dot match

    (tmprow, tmpcolumn) = (_row + 1, _column - 1)
    while isValidcell(tmprow, tmpcolumn) and state_conv1(tmprow, tmpcolumn, board_) != 0 \
            and c_dot(tmprow, tmpcolumn, board_) == compare[1]:
        match[1] += 1
        tmprow += 1
        tmpcolumn -= 1

    if match[0] >= 4 or match[1] >= 4:
        return (True, match)
    else:
        return (False, match)


def check_winner_diag2(_card, board_=Board):
    (_row, _column) = _card
    (tmprow, tmpcolumn) = (_row, _column)
    match = [0, 0]
    compare = [c_color(tmprow, tmpcolumn,board_ ), c_dot(tmprow, tmpcolumn, board_)]

    # checking for color match
    while isValidcell(tmprow, tmpcolumn) and state_conv1(tmprow, tmpcolumn, board_) != 0 \
            and c_color(tmprow, tmpcolumn, board_) == compare[0]:
        match[0] += 1
        tmprow -= 1
        tmpcolumn -= 1

    # checking for dot match
    (tmprow, tmpcolumn) = (_row, _column)
    while isValidcell(tmprow, tmpcolumn) and state_conv1(tmprow, tmpcolumn, board_) != 0 \
            and c_dot(tmprow, tmpcolumn, board_) == compare[1]:
        match[1] += 1
        tmprow -= 1
        tmpcolumn -= 1

    # checking for color match
    (tmprow, tmpcolumn) = (_row + 1, _column + 1)
    while isValidcell(tmprow, tmpcolumn) and state_conv1(tmprow, tmpcolumn, board_) != 0 \
            and c_color(tmprow, tmpcolumn, board_) == compare[0]:
        match[0] += 1
        tmprow += 1
        tmpcolumn += 1

    # checking for dot match
    (tmprow, tmpcolumn) = (_row + 1, _column + 1)
    while isValidcell(tmprow, tmpcolumn) and state_conv1(tmprow, tmpcolumn, board_) != 0 \
            and c_dot(tmprow, tmpcolumn, board_) == compare[1]:
        match[1] += 1
        tmprow += 1
        tmpcolumn += 1

    if match[0] >= 4 or match[1] >= 4:
        return (True, match)
    else:
        return (False, match)


def check_winner_row(_card, board_=Board):
    (_row, _column) = _card
    (compare1, compare) = (['', ''], ['', ''])
    match = [1, 1]
    row_tmp = 12
    iswin = [1, 1]
    while (row_tmp - 1) >= 0 and (match[0] < 4 or match[1] < 4):
        row_tmp = row_tmp - 1
        if state_conv1(row_tmp, _column, board_) == 0:
            break
        compare1[0] = c_color(row_tmp, _column, board_)
        compare1[1] = c_dot(row_tmp, _column, board_)
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

    iswin = [max(iswin[0], match[0]), max(iswin[1], match[1])]
    if iswin[0] >= 4 or iswin[1] >= 4:
        return (True, iswin)
    else:
        return (False, iswin)


def check_winner_column(_card, board_=Board):
    (_row, _column) = _card
    (compare, compare1) = (['', ''], ['', ''])
    match = [1, 1]
    column_tmp = 8
    iswin = [1, 1]
    while (column_tmp - 1) >= 0 and (match[0] < 4 or match[1] < 4):
        column_tmp = column_tmp - 1
        if state_conv1(_row, column_tmp, board_) == 0:
            iswin = [max(iswin[0], match[0]), max(iswin[1], match[1])]
            (compare, compare1) = (['', ''], ['', ''])
            match = [1, 1]
            continue
        compare1[0] = c_color(_row, column_tmp, board_)
        compare1[1] = c_dot(_row, column_tmp, board_)
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
    iswin = [max(iswin[0], match[0]), max(iswin[1], match[1])]
    if iswin[0] >= 4 or iswin[1] >= 4:
        return (True, iswin)
    else:
        return (False, iswin)


def whatMakesWin(stat):
    winby = stat[1]
    if not stat[0]:
        return [0, 0]
    if winby[0] >= 4 and winby[1] >= 4:
        return [1, 1]
    elif winby[0] >= 4:
        return [1, 0]
    elif winby[1] >= 4:
        return [0, 1]
    else:
        return [0, 0]


def checkWinnerUtil(card, board_=Board):
    x1 = check_winner_column((card[0], card[1]), board_)
    x2 = check_winner_column((card[2], card[3]), board_)
    x3 = check_winner_row((card[0], card[1]), board_)
    x4 = check_winner_row((card[2], card[3]), board_)
    x5 = check_winner_diag1((card[0], card[1]), board_)
    x6 = check_winner_diag1((card[2], card[3]), board_)
    x7 = check_winner_diag2((card[0], card[1]), board_)
    x8 = check_winner_diag2((card[2], card[3]), board_)
    # wins[0] for colors and wins[1] for dots
    wins = [0, 0]
    if x1[0]:
        print("c.left")
        tmp = whatMakesWin(x1)
        wins = [(x + y) for (x, y) in zip(wins, tmp)]
    if x2[0]:
        print("c.right")
        tmp = whatMakesWin(x2)
        wins = [(x + y) for (x, y) in zip(wins, tmp)]
    if x3[0]:
        print("r.left")
        tmp = whatMakesWin(x3)
        wins = [(x + y) for (x, y) in zip(wins, tmp)]
    if x4[0]:
        print("r.right")
        tmp = whatMakesWin(x4)
        wins = [(x + y) for (x, y) in zip(wins, tmp)]
    if x5[0]:
        print("d.left")
        tmp = whatMakesWin(x5)
        wins = [(x + y) for (x, y) in zip(wins, tmp)]

    if x6[0]:
        print("d.right")
        tmp = whatMakesWin(x6)
        wins = [(x + y) for (x, y) in zip(wins, tmp)]

    if x7[0]:
        print("d.left")
        tmp = whatMakesWin(x7)
        wins = [(x + y) for (x, y) in zip(wins, tmp)]

    if x8[0]:
        print("d.right")
        tmp = whatMakesWin(x8)
        wins = [(x + y) for (x, y) in zip(wins, tmp)]

    return wins


def checkWinner(card, _choice, player, board_=Board):
    score = checkWinnerUtil(card, board_)

    if all(v == 0 for v in score):
        return False

    if score[0] >= 1 and score[1] >= 1:  # it is draw so last player win
        print(player, ' won,- it is draw so last player win')
        return True
    elif score[0] >= 1:
        print('Player ', _choice['color'], ' has won the game as he choosen color')
        return True
    elif score[1] >= 1:
        print('Player ', _choice['dot'], ' has won the game as he choosen dot')
        return True
    else:
        return False

def checkWinner_AI(card, _choice, player, board):
    score = checkWinnerUtil(card, board)

    if all(v == 0 for v in score):
        return False
    wonby = -1
    if score[0] >= 1 and score[1] >= 1:
        return True
    elif score[0] >= 1:
        wonby = _choice['color']
    elif score[1] >= 1:
        wonby = _choice['dot']
    else:
        return False

    if wonby == ai_player_num:
        return True
    else:
        return False


def isLegalMoveUtil(row, column, angle, board_):

    if state_conv1(row, column,board_) != 0:
        return False
    else:
        pass

    if row == 11:
        if angle == 0 or angle == 180:
            return isValidcell(row, column + 1) and state_conv1(row, column + 1, board_) == 0
        elif angle == 90 or angle == 270:
            return isValidcell(row - 1, column) and state_conv1(row - 1, column, board_) == 0
        else:
            return True

    if angle == 90 or angle == 270:
        if (isValidcell(row - 1, column) and state_conv1(row - 1, column,board_) == 0) and \
                (isValidcell(row + 1, column) and state_conv1(row + 1, column, board_) != 0):
            return True
        else:
            return False

    if angle == 0 or angle == 180:
        if ( isValidcell(row,column + 1) and state_conv1(row, column + 1,board_) == 0 ) and \
                (state_conv1(row + 1, column + 1,board_) != 0 and state_conv1(row + 1, column,board_) != 0):
            return True
        else:
            return False


def isLegalMove(row, column, angle, board_, isprint=True):
    isgood = isLegalMoveUtil(row, column, angle, board_)
    if not isgood:
        if isprint:
            print('Sorry, Illegal place')
    return isgood


# to see if any card is hanging on an empty cell
def isLegalMove1(pos, angle):
    if state_conv1(pos[0], pos[1]) == 0 and state_conv1(pos[0] - 1, pos[1]) != 0:
        return False
    if state_conv1(pos[2], pos[3]) == 0 and state_conv1(pos[2] - 1, pos[3]) != 0:
        return False
    return True


def calc_turn(turn):
    if turn == 1:
        return 2
    else:
        return 1


isalphabeta_1 = input("alpha-beta should be yes or no")
isalphabeta = True if isalphabeta_1 == "yes" else False
istrace_1 = input("trace should be yes or no")
ai_player_num = 0
istrace = True if istrace_1 == "yes" else False
aifirst_1 = input("is AI plays first -  yes or no")
aifirst = 1 if aifirst_1 == "yes" else 0
ai_player_num = 1 if aifirst_1 == "yes" else 2
if aifirst == 1:
    player1_choice = 'dot'
else:
    player1_choice = input('Enter your Player 1 choice either dot or color ').lower()
player2_choice = ('dot' if player1_choice == 'color' else 'color')
player_choices = {player1_choice: '1', player2_choice: '2'}
count = 1

def get_player_choice():
    return {player1_choice: 1, player2_choice: 2}

def get_player_choice1():
    return ( player1_choice, player2_choice )

def is_ai_1():
    return aifirst

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

number_angle1 = {
    1: 0,
    2: 90,
    3: 180,
    4: 270,
    5: 0,
    6: 90,
    7: 180,
    8: 270
}



def state_conv(row, column):
    # assume index start at 0 0
    row = row + 1
    column = column + 1
    pos = row * 8
    pos = pos - (8 - column) - 1
    return pos


def mapper(card_side):
    if card_side == 1:
        return [4, 1]
    else:
        return [2, 3]


def card_number(num):
    return num - (num % 100)

def state_conv1(row1, column1, board_=Board):
    # assume index start at 0 0
    row1 = row1 + 1
    column1 = column1 + 1
    pos1 = row1 * 8
    pos1 = pos1 - (8 - column1) - 1
    return board_[pos1]


def getPositionByAngle(angle, row, column):
    if angle == 0:
        return (row, column, row, column + 1)
    elif angle == 90:
        return (row - 1, column, row, column)
    elif angle == 180:
        return (row, column + 1, row, column)
    elif angle == 270:
        return (row, column, row - 1, column)
