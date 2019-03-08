from Nodes import Node
from Printer import printBoard
from Util import *
import copy


# Note inp should be list of integers including inp[4]
def recycle_card(inp, recent_card, board_, isprint=True):
    old_left = state_conv1(inp[0], inp[1], board_)
    old_right = state_conv1(inp[2], inp[3], board_)
    if old_left == 0 or old_right == 0 or card_number(old_left) != card_number(old_right) \
            or not inp[4] in number_angle1:
        if isprint:
            print('That is an invalid card -  no card or  red and white belongs to different cards')
        return None

    angle = number_angle1[inp[4]]
    pos = getPositionByAngle(angle, inp[5], inp[6])
    if inp[0:4] == recent_card:
        if isprint:
            print("Illegal - just recent card")
        return None

    # check is destination cell is available or could be same
    # pos contains destination location of recycling move
    dleft = state_conv1(pos[0], pos[1], board_)
    dright = state_conv1(pos[2], pos[3], board_)
    card_tmp = card_number(state_conv1(inp[0], inp[1], board_))

    if inp[1] != 0:
        if state_conv1(inp[0] - 1, inp[1], board_) != 0 and card_number(state_conv1(inp[0] - 1, inp[1], board_)) != card_tmp:
            if isprint:
                print('Sorry it is an invalid recycling move - it has something on top.l')
            return None
    if inp[2] != 0:
        if state_conv1(inp[2] - 1, inp[3], board_) != 0 and card_number(state_conv1(inp[2] - 1, inp[3], board_)) != card_tmp:
            if isprint:
                print('Sorry it is an invalid recycling move - it has something on top.r')
            return None

    if (dleft != 0 and card_number(dleft) != card_number(old_left)) \
            or (dright != 0 and card_number(dright) != card_number(old_right)):
        if isprint:
            print('Sorry it is a invalid recycling move - destination is positions are occupied')
        return None

    if all(inp[k] == pos[k] for k in range(4)):
        if isprint:
            print("cannot put it back at the same position and with the same orientation ", card_tmp)
        return None

    # now do the recycling move
    # first remove the previous card
    board_[state_conv(inp[0], inp[1])] = 0
    board_[state_conv(inp[2], inp[3])] = 0

    side = (1 if inp[4] <= 4 else 2)

    # create new card

    if not isLegalMove(inp[5], inp[6], angle, board_, False):
        if isprint:
            print('Sorry not a good move')
        board_[state_conv(inp[0], inp[1])] = old_left
        board_[state_conv(inp[2], inp[3])] = old_right
        return None

    code = mapper(side)
    board_[state_conv(pos[0], pos[1])] = card_tmp + code[0]
    board_[state_conv(pos[2], pos[3])] = card_tmp + code[1]
    if isprint:
        printBoard(board_)
    return board_, pos


def place_card(row, column, config_number, count_, board_, isprint=True):
    if config_number in number_angle:
        angle = number_angle[config_number]
    else:
        if isprint:
            print("Wrong place, kindly advised to follow prof requirement")
        return None

    side = (1 if int(config_number) <= 4 else 2)
    if not isValidcell(row, column) or not isLegalMove(row, column, angle, board_, False):
        if isprint:
            print('Sorry not a good move - out of index or illegal move ', config_number)
        return None
    pos = getPositionByAngle(angle, row, column)
    code = mapper(side)
    board_[state_conv(pos[0], pos[1])] = (count_ * 100) + code[0]
    board_[state_conv(pos[2], pos[3])] = (count_ * 100) + code[1]
    if isprint:
        printBoard(board_)
    return pos, board_


"""
it seems like there is no need to hash a state
"""


def generate_states(parent: Node):
    number_of_states = 0
    # traverse column wise to check possibilities
    for column in range(8):
        row = parent.track[column]
        if row < 0:
            row = 0
        # check all 8 cards and if it is a possible to fit in pos
        for orient in range(1, 9):
            result = place_card(row, column, str(orient), parent.no_cards, copy.copy(parent.state), False)
            if result is None:
                continue
            tmp_track = copy.copy(parent.track)
            if orient % 2 == 0:
                tmp_track[column] -= 2
            else:
                tmp_track[column] -= 1
                tmp_track[column + 1] -= 1

            node = Node(copy.copy(result[1]), parent)
            node.set_move((row, column, orient))
            node.set_level(parent.level + 1)
            node.set_no_cards(parent.no_cards + 1)
            node.set_track(tmp_track)
            parent.add_children(node)
            number_of_states += 1


def try_card_recycle(parent, card_pos):
    # remove this card and try to put at different position and orientations
    # parent.state[state_conv(card_pos[0], card_pos[1])] = 0
    for column in range(8):
        row = parent.track[column]
        if row < 0:
            row = 0
        for orient in range(1, 9):
            inp = card_pos + (orient, row, column)
            result = recycle_card(inp, parent.pos, copy.copy(parent.state), False)
            tmp = parent.parent
            results = []
            while tmp != None:
                x1 = recycle_card(inp, parent.pos, copy.copy(tmp.state), False)
                results.append(True if x1 is None else False)
                tmp = tmp.parent

            if result is None or any(results):
                continue
            tmp_track = copy.copy(parent.track)
            if orient % 2 == 0:
                tmp_track[column] -= 2
            else:
                tmp_track[column] -= 1
                tmp_track[column + 1] -= 1
            #remove the orginal card too
            tmp_track[card_pos[1]] += 1
            tmp_track[card_pos[3]] += 1
            for j in tmp_track:
                if j == 13:
                    java = "for debug error"
            (board, pos) = (result[0], result[1])
            node = Node(copy.copy(board), parent)
            node.set_level(parent.level + 1)
            node.set_track(tmp_track)
            node.set_pos(pos)
            node.set_move(inp)
            parent.add_children(node)


def generate_recyc_states(parent: Node):
    for column in range(8):
        row = parent.track[column] + 1
        if row == 12:
            continue
        if row < 0:
            row = 0
        #check horizontal
        x1 = card_number(state_conv1(row, column, parent.state))
        x2 = None
        x3 = None
        if isValidcell(row, column+1):
            x2 = card_number(state_conv1(row, column + 1, parent.state))
        if isValidcell(row + 1, column):
            x3 = card_number(state_conv1(row + 1, column, parent.state))
        if x1 == x2:
            #parent.track[column] += 1
            #parent.track[column + 1] += 1
            try_card_recycle(parent, (row, column, row, column+1))
        elif x1 == x3:
            #parent.track[column] += 2
            try_card_recycle(parent, (row, column, row + 1, column))
        else:
            continue