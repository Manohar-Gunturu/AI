#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from sys import exit
from GameEngine import *
from minmax import run_minmax, run_alphabeta, inf, get_en_count, reset_en_count
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


def take_human_input():
    #inp = input('Enter card details ').strip().split(' ')
    inp = names_list[count - 1].split(' ')
    if inp[0] != '0':
        print("Don't you know the input format for a move")
        return None
    row, column = getCellPosition([inp[2], inp[3]])

    return row, column, inp[1]


global_track = [11, 11, 11, 11, 11, 11, 11, 11]


def take_ai_input():
    root = Node(copy.copy(Board), None)
    root.set_track(copy.copy(global_track))
    root.set_level(0)
    root.set_no_cards(count)
    generate_states(root)
    for child in root.children:
        generate_states(child)
    # run min max
    if not isalphabeta:
        bestmove = run_minmax(root)
        print("e(n) brought up to root is ", root.value, " number of time e(n) applied", get_en_count())
    else:
        bestmove1 = run_alphabeta(root, -inf, inf, True)
        bestmove = bestmove1[1]
        print("e(n) brought up to root is ", bestmove1, " number of time e(n) applied", get_en_count())
    move = root.children[bestmove].move
    return move


while count <= 24:
    print('Player ', whose_turn, ' turn')
    """
    if whose_turn % 2 == aifirst:
        reset_en_count()
        (row, column, card_number) = take_ai_input()
    else:
    """
    (row, column, card_number) = take_human_input()

    result = place_card(row, column, str(card_number), count, Board)
    if result is None:
        continue
    if int(card_number) % 2 == 0:
        global_track[column] -= 2
    else:
        global_track[column] -= 1
        global_track[column + 1] -= 1
    pos = result[0]
    if checkWinner(pos, player_choices, whose_turn):
        exit()
    recent_card = pos
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
            return lpos + rpos + (int(inp[4]),) + npos
    except (ValueError, IndexError):
        return ()

print("-------- Started recycling phase ------")

# sample test
root = Node(copy.copy(Board), None)
root.set_track(copy.copy(global_track))
root.set_level(0)
root.set_pos(recent_card)
root.set_no_cards(count)
generate_recyc_states(root)
exit()




def take_ai_rec_input():
    pass


for i in range(36):
    print('Player ', whose_turn, ' turn')
    if whose_turn % 2 == aifirst:
        reset_en_count()
        inp = take_ai_rec_input()
    else:
        inp = process_input()
    if len(inp) == 0:
        print('Recycling move input error')
        continue

    result = recycle_card(inp, recent_card, Board)
    pos = result[1]
    recent_card = pos
    if checkWinner(pos, player_choices, whose_turn):
        exit()
    count = count + 1
    whose_turn = calc_turn(whose_turn)

print('Match is a draw, ;)')
