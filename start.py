#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from sys import exit
from GameEngine import *
from asycwrite import open_trace,write_trace, close_trace
from minmax import run_minmax, run_alphabeta, inf, get_en_count, reset_en_count
tmpinput = """0 8 g 1
              0 2 a 1
              0 1 b 1
              0 2 g 3
              0 8 h 11
              0 1 b 2
              0 1 b 3
              0 8 c 4
              0 2 c 6
              0 7 d 1
              0 1 d 2
              0 1 d 3"""

names_list = [y for y in (x.strip() for x in tmpinput.splitlines()) if y]
count = 1
recent_card = []

tmp_t = 0
def take_human_input():
    global tmp_t
    #inp = input('Enter card details ').strip().split(' ')
    inp = names_list[tmp_t].split(' ')
    if inp[0] != '0':
        print("Don't you know the input format for a move")
        return None
    tmp_t += 1
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
    open_trace(isalphabeta)
    trace_content = []
    if not isalphabeta:
        bestmove = run_minmax(root, trace_content)
        trace_content.append(" ")
        trace_content = [str(get_en_count()), str(round(root.value, 1)), ' '] + trace_content
        write_trace(trace_content)
        print("e(n) brought up to root is ", root.value, " number of time e(n) applied", get_en_count())
    else:
        bestmove1 = run_alphabeta(root, -inf, inf, True, trace_content)
        bestmove = bestmove1[1]
        trace_content.append(" ")
        trace_content = [ str(get_en_count()), str(round(bestmove1[0], 1)), ' '] + trace_content
        write_trace(trace_content)
        print("e(n) brought up to root is ", bestmove1, " number of time e(n) applied", get_en_count())
    move = root.children[bestmove].move
    close_trace()
    return move


while count <= 24:
    print('Player ', whose_turn, ' turn')
    if whose_turn % 2 == aifirst:
        reset_en_count()
        (row, column, card_number) = take_ai_input()
    else:
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
def take_ai_rec_input():
    root = Node(copy.copy(Board), None)
    root.set_track(copy.copy(global_track))
    root.set_level(0)
    root.set_pos(recent_card)
    root.set_no_cards(count)
    generate_recyc_states(root)
    for child in root.children:
        generate_recyc_states(child)
    # run min max
    open_trace(isalphabeta)
    trace_content = []
    if not isalphabeta:
        bestmove = run_minmax(root, trace_content)
        trace_content.append(" ")
        trace_content = [str(get_en_count()), str(round(root.value, 1)), ' '] + trace_content
        write_trace(trace_content)
        print("e(n) brought up to root is ", root.value, " number of time e(n) applied", get_en_count())
    else:
        bestmove1 = run_alphabeta(root, -inf, inf, True, trace_content)
        bestmove = bestmove1[1]
        trace_content.append(" ")
        trace_content = [str(get_en_count()), str(round(bestmove1[0], 1)), ' '] + trace_content
        write_trace(trace_content)
        print("e(n) brought up to root is ", bestmove1, " number of time e(n) applied", get_en_count(), len(root.children))
    move = root.children[bestmove].move
    close_trace()
    return move


while count <= 60:
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
    if result is None:
        continue
    pos = result[1]
    recent_card = pos
    if inp[4] % 2 == 0:
        global_track[inp[6]] -= 2
    else:
        global_track[inp[6]] -= 1
        global_track[inp[6]] -= 1
    # remove the orginal card too
    global_track[inp[1]] += 1
    global_track[inp[3]] += 1
    if checkWinner(pos, player_choices, whose_turn):
        exit()
    count = count + 1
    whose_turn = calc_turn(whose_turn)

print('Match is a draw, ;)')
