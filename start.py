#!/usr/bin/python
# -*- coding: utf-8 -*-


from sys import exit
from GameEngine import *

tmpinput = """0 1 A 1
            0 1 C 1
            0 1 E 1
            0 1 G 1
            0 5 A 2
            0 5 C 2
            0 5 E 2
            0 5 G 2
            0 3 A 3
            0 3 C 3
            0 3 E 3
            0 3 G 3
            0 7 A 4
            0 7 C 4
            0 7 E 4
            0 7 G 4
            0 1 A 5
            0 1 C 5
            0 1 E 5
            0 1 G 5
            0 5 A 6
            0 5 C 6
            0 5 E 6
            0 5 G 6"""

names_list = [y for y in (x.strip() for x in tmpinput.splitlines()) if y]
count = 1
recent_card = []
"""
root: Node = Node(Board, None)
root.set_track(copy.copy(default_track))
root.set_level(0)
generate_states(root)
for child in root.children:
    generate_states(child)
exit()
"""
while count <= 24:
    print('Player ', whose_turn, ' turn')
    inp = input('Enter card details ').strip().split(' ')
    #inp = names_list[count - 1].split(' ')
    if inp[0] != '0':
        print("Don't you know the input format for a move")
        continue
    (row, column) = getCellPosition([inp[2], inp[3]])
    result = place_card(row, column, inp[1], count, Board)
    if result is None:
        continue
    pos = result[0]
    if checkWinner(pos, player_choices, whose_turn):
        exit()
    recent_card = pos
    count = count + 1
    print("count, ", count)
    whose_turn = calc_turn(whose_turn)


def card_number(num):
    return num - (num % 100)


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
            return lpos + rpos + (inp[4],) + npos
    except (ValueError, IndexError):
        return ()


print("-------- Started recycling phase ------")

for i in range(36):
    print('Player ', whose_turn, ' turn')
    inp = process_input()
    if len(inp) == 0:
        print('Recycling move input error')
        continue

    old_left = state_conv1(inp[0], inp[1])
    old_right = state_conv1(inp[2], inp[3])
    if old_left == 0 or old_right == 0 or card_number(old_left) != card_number(old_right) \
            or not inp[4] in number_angle:
        print('That is an invalid card -  no card or  red and white belongs to different cards')
        continue

    angle = number_angle[inp[4]]
    pos = getPositionByAngle(angle, inp[5], inp[6])
    if inp[0:4] == recent_card:
        print("Illegal - just recent card")
        continue

    # check is destination cell is available or could be same
    # pos contains destination location of recycling move
    dleft = state_conv1(pos[0], pos[1])
    dright = state_conv1(pos[2], pos[3])
    card_tmp = card_number(state_conv1(inp[0], inp[1]))

    if inp[1] != 0:
        if state_conv1(inp[0] - 1, inp[1]) != 0 and card_number(state_conv1(inp[0] - 1, inp[1])) != card_tmp:
            print('Sorry it is an invalid recycling move - it has something on top.l')
            continue
    if inp[2] != 0:
        if state_conv1(inp[2] - 1, inp[3]) != 0 and card_number(state_conv1(inp[2] - 1, inp[3])) != card_tmp:
            print('Sorry it is an invalid recycling move - it has something on top.r')
            continue

    if (dleft != 0 and card_number(dleft) != card_number(old_left)) \
            or (dright != 0 and card_number(dright) != card_number(old_right)):
        print('Sorry it is a invalid recycling move - destination is positions are occupied')
        continue

    if all(inp[k] == pos[k] for k in range(4)):
        print("cannot put it back at the same position and with the same orientation ", card_tmp)
        continue

    # now do the recycling move
    # first remove the previous card
    Board[state_conv(inp[0], inp[1])] = 0
    Board[state_conv(inp[2], inp[3])] = 0

    side = (1 if int(inp[4]) <= 4 else 2)

    # create new card

    if not isLegalMove(inp[5], inp[6], angle):
        print('Sorry not a good move')
        Board[state_conv(inp[0], inp[1])] = old_left
        Board[state_conv(inp[2], inp[3])] = old_right
        continue

    code = mapper(side)
    Board[state_conv(pos[0], pos[1])] = card_tmp + code[0]
    Board[state_conv(pos[2], pos[3])] = card_tmp + code[1]
    printBoard(Board)
    recent_card = pos
    if checkWinner(pos, player_choices, whose_turn):
        exit()
    count = count + 1
    whose_turn = calc_turn(whose_turn)

print('Match is a draw, ;)')
