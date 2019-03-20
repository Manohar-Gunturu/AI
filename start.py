#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from sys import exit
import time
from GameEngine import *
from asycwrite import open_trace,write_trace, close_trace
from minmax import run_minmax, run_alphabeta, inf, get_en_count, reset_en_count
tmpinput = """
0 1 a 1
0 1 e 1
0 6 e 2
0 6 f 2
0 5 e 4
0 1 e 5
0 2 e 6
0 2 e 8
0 2 e 10
0 2 d 1
0 2 d 5
0 6 d 9"""


names_list = [y for y in (x.strip() for x in tmpinput.splitlines()) if y]
count = 1
recent_card = []
def take_human_input():
    try:
        inp = input('Enter card details ').strip().split(' ')
        #inp = names_list[trc].split(' ')
        if inp[0] != '0':
            print("Don't you know the input format for a move")
            return take_human_input()
        row, column = getCellPosition([inp[2], inp[3]])
        return row, column, inp[1]
    except (ValueError, IndexError, TypeError):
        return take_human_input()


global_track = [11, 11, 11, 11, 11, 11, 11, 11]


if istrace:
    open_trace(isalphabeta)
player_choicesai = get_player_choice();
def take_ai_input():
    start_time = time.time()
    root = Node(copy.copy(Board), None)
    root.set_track(copy.copy(global_track))
    root.set_level(0)
    root.set_no_cards(count)
    generate_states(root)
    for child in root.children:
        generate_states(child)
    # run min max

    for child in root.children:
        if checkWinner_AI(child.pos, player_choicesai, whose_turn, child.state):
            return child.move

    trace_content = []
    if not isalphabeta:
        bestmove = run_minmax(root, trace_content)
        trace_content.append("\n")
        if istrace: trace_content = [str(get_en_count()), str(round(root.value, 1)), ''] + trace_content
        if istrace: write_trace(trace_content)
        print("e(n) brought up to root is ", root.value, " number of time e(n) applied", get_en_count()," time", (time.time() - start_time))
    else:
        bestmove1 = run_alphabeta(root, -inf, inf, True, trace_content)
        bestmove = bestmove1[1]
        trace_content.append("\n")
        if istrace: trace_content = [ str(get_en_count()), str(round(bestmove1[0], 1)), ''] + trace_content
        write_trace(trace_content)
        print("e(n) brought up to root is ", bestmove1, " number of time e(n) applied", get_en_count(), " time", (time.time() - start_time))
    move = root.children[bestmove].move
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
    except (ValueError, IndexError, TypeError):
        return ()


print("-------- Started recycling phase ------")


# sample test
def take_ai_rec_input():
    start_time = time.time()
    root = Node(copy.copy(Board), None)
    root.set_track(copy.copy(global_track))
    root.set_level(0)
    root.set_pos(recent_card)
    root.set_no_cards(count)
    generate_recyc_states(root)
    for child in root.children:
        generate_recyc_states(child)
    # run min max
    trace_content = []
    if not isalphabeta:
        bestmove = run_minmax(root, trace_content)
        trace_content.append("\n")
        if istrace: trace_content = [str(get_en_count()), str(round(root.value, 1)), ''] + trace_content
        if istrace: write_trace(trace_content)
        print("e(n) brought up to root is ", root.value, " number of time e(n) applied", get_en_count()," time", (time.time() - start_time))
    else:
        bestmove1 = run_alphabeta(root, -inf, inf, True, trace_content)
        bestmove = bestmove1[1]
        trace_content.append("\n")
        if istrace: trace_content = [str(get_en_count()), str(round(bestmove1[0], 1)), ''] + trace_content
        if istrace: write_trace(trace_content)
        print("e(n) brought up to root is ", bestmove1, " number of time e(n) applied", get_en_count(), " time", (time.time() - start_time))
    move = root.children[bestmove].move
    return move


while count <= 40:
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
        if inp[6]+ 1 <= 7: global_track[inp[6]+ 1] -= 1
    # remove the orginal card too
    global_track[inp[1]] += 1
    global_track[inp[3]] += 1
    if checkWinner(pos, player_choices, whose_turn):
        exit()
    count = count + 1
    whose_turn = calc_turn(whose_turn)

print('Match is a draw, ;)')

import atexit
atexit.register(close_trace)
