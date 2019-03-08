from sys import exit
from GameEngine import *
from asycwrite import open_trace,write_trace, close_trace
from minmax import run_minmax, run_alphabeta, inf, get_en_count, reset_en_count

b = [0, 0, 0, 0, 0, 2104, 0, 1104, 0, 0, 0, 0, 0, 2101, 0, 1101, 0, 0, 0, 0, 0, 1904, 0, 904, 0, 0, 0, 0, 0, 1901, 0, 901, 0, 0, 0, 0, 0, 1704, 0, 704, 0, 0, 0, 0, 0, 1701, 0, 701, 0, 0, 2302, 2303, 0, 1504, 0, 504, 2204, 2201, 2404, 2401, 0, 1501, 0, 501, 1803, 1802, 2003, 2002, 0, 1304, 0, 304, 1401, 1404, 1601, 1604, 0, 1301, 0, 301, 802, 803, 1002, 1003, 1202, 1203, 0, 104, 204, 201, 404, 401, 604, 601, 0, 101]
t = [6, 6, 5, 5, 9, -1, 11, -1]
printBoard(b)
root = Node(copy.copy(b), None)
root.set_track(copy.copy(t))
root.set_level(0)
root.set_pos((7, 2, 7, 3))
root.set_no_cards(25)
generate_recyc_states(root)