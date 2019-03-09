from sys import exit
from GameEngine import *
import time
from asycwrite import open_trace,write_trace, close_trace
from minmax import run_minmax, run_alphabeta, inf, get_en_count, reset_en_count, calc_en

global_track = [10, 10, 11, 11, 11, 11, 11, 11]
Board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 104, 101, 0, 0, 0, 0, 0, 0]
root = Node(copy.copy(Board), None)
root.set_track(copy.copy(global_track))
root.set_level(0)
root.set_no_cards(1)
generate_states(root)
trace_content = []
bestmove = run_minmax(root, trace_content)
for child in root.children:
    printBoard(child.state)
    print(child.value)

print("best move", bestmove,root.children[bestmove].value)


"""
b = [0, 0, 0, 0, 0, 2304, 0, 0, 0, 1004, 0, 0, 0, 2301, 0, 0, 0, 1001, 0, 0, 0, 1804, 0, 0, 0, 804, 0, 0, 0, 1801, 0, 0, 0, 801, 0, 0, 0, 1604, 0, 2404, 0, 604, 0, 0, 0, 1601, 0, 2401, 0, 601, 0, 0, 0, 1404, 0, 2204, 0, 404, 2002, 2003, 0, 1401, 0, 2201, 0, 401, 1903, 1902, 0, 1204, 2103, 2102, 0, 204, 1501, 1504, 0, 1201, 1701, 1704, 0, 201, 902, 903, 1102, 1103, 1302, 1303, 104, 101, 304, 301, 504, 501, 704, 701]
t = [10, 0, 5, 7, 9, -1, 7, 3]
printBoard(b)
start_time = time.time()
root = Node(copy.copy(b), None)
root.set_track(copy.copy(t))
root.set_level(0)
root.set_pos((7, 2, 7, 3))
root.set_no_cards(25)
generate_recyc_states(root)
for child in root.children:
    generate_recyc_states(child)
trace_content = []
bestmove = run_minmax(root, trace_content)
trace_content.append(" ")
trace_content = [str(get_en_count()), str(round(root.value, 1)), ' '] + trace_content
write_trace(trace_content)
"""