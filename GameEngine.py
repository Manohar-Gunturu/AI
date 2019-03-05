from Nodes import Node
from Printer import printBoard
from Util import *
import copy


def place_card(row, column, config_number, count, board_):
    if row == 10 and column == 0:
        xc = 9
    if config_number in number_angle:
        angle = number_angle[config_number]
    else:
        print("Wrong place, kindly advised to follow prof requirement")
        return None

    side = (1 if int(config_number) <= 4 else 2)
    if not isValidcell(row, column) or not isLegalMove(row, column, angle, board_):
        #print('Sorry not a good move - out of index or illegal move ', config_number)
        return None
    pos = getPositionByAngle(angle, row, column)
    code = mapper(side)
    board_[state_conv(pos[0], pos[1])] = (count * 100) + code[0]
    board_[state_conv(pos[2], pos[3])] = (count * 100) + code[1]
    #printBoard(board_)
    return pos, board_

"""
it seems like there is no need to hash a state
"""
possible_moves = {}
def generate_states(parent : Node):
    number_of_states = 0
    # traverse column wise to check possibilities
    for column in range(8):
        row = parent.track[column]
        # check all 8 cards and if it is a possible to fit in pos
        for card_number in range(1, 9):
            result = place_card(row, column, str(card_number), parent.level + 1, copy.copy(parent.state))
            if result is None:
                print(row, column, card_number, " is wrong")
                continue
            print(row, column, card_number, "is right")
            tmp_track = copy.copy(parent.track)
            if card_number % 2 == 0:
                tmp_track[column] -= 2
            else:
                tmp_track[column] -= 1
                tmp_track[column + 1] -= 1

            node = Node(copy.copy(result[1]), parent)
            node.set_track(tmp_track)
            parent.add_children(node)
            number_of_states += 1
    print("Number of possible states are ", number_of_states)