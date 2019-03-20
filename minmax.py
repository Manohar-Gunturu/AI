from Util import state_conv1, get_player_choice1, card_number, check_winner_column, check_winner_row, check_winner_diag1, check_winner_diag2, whatMakesWin, get_player_choice, is_ai_1
import operator
from math import inf

en_count = 0

def calc_en1(child):
    return calc_en(child)

def get_en_count():
    return en_count

def reset_en_count():
    global en_count
    en_count = 0


pchoices = get_player_choice()

def checkWinnerUtil1(card, board_):
    x1 = check_winner_column((card[0], card[1]),  board_)
    x2 = check_winner_column((card[2], card[3]),  board_)
    x3 = check_winner_row((card[0], card[1]), board_)
    x4 = check_winner_row((card[2], card[3]), board_)
    x5 = check_winner_diag1((card[0], card[1]), board_)
    x6 = check_winner_diag1((card[2], card[3]), board_)
    x7 = check_winner_diag2((card[0], card[1]), board_)
    x8 = check_winner_diag2((card[2], card[3]), board_)
    # wins[0] for colors and wins[1] for dots
    wins = [0, 0]
    wins1 = [0, 0]
    if x1[0]:
        tmp = whatMakesWin(x1)
        wins = [(x + y) for (x, y) in zip(wins, tmp)]
    if x2[0]:
        tmp = whatMakesWin(x2)
        wins = [(x + y) for (x, y) in zip(wins, tmp)]
    if x3[0]:
        tmp = whatMakesWin(x3)
        wins = [(x + y) for (x, y) in zip(wins, tmp)]
    if x4[0]:
        tmp = whatMakesWin(x4)
        wins = [(x + y) for (x, y) in zip(wins, tmp)]
    if x5[0]:
        tmp = whatMakesWin(x5)
        wins = [(x + y) for (x, y) in zip(wins, tmp)]

    if x6[0]:
        tmp = whatMakesWin(x6)
        wins = [(x + y) for (x, y) in zip(wins, tmp)]

    if x7[0]:
        tmp = whatMakesWin(x7)
        wins = [(x + y) for (x, y) in zip(wins, tmp)]

    if x8[0]:
        tmp = whatMakesWin(x8)
        wins = [(x + y) for (x, y) in zip(wins, tmp)]

    score = wins
    if score[0] >= 1 and score[1] >= 1:  # it is draw so last player win
        return 0, None
    elif score[0] >= 1:
        return pchoices['color'], None
    elif score[1] >= 1:
        return pchoices['dot'], None

    wins1[0] = x1[1][0] + x2[1][0] + x3[1][0] + x4[1][0] + x5[1][0] + x6[1][0] + x7[1][0] + x8[1][0]
    wins1[1] = x1[1][1] + x2[1][1] + x3[1][1] + x4[1][1] + x5[1][1] + x6[1][1] + x7[1][1] + x8[1][1]
    return -1,  wins1


def calc_en(child):
    if len(child.children) != 0:
        return child.value
    global en_count
    en_count += 1
    whowon, matches = checkWinnerUtil1(child.pos, child.state)
    who_ai_first = is_ai_1()
    what_ai_select = get_player_choice1()
    ai_chose = what_ai_select[0] if who_ai_first else what_ai_select[1]
    if whowon == 1:
        if who_ai_first == 1:
            return 100000000
        else:
            return -100000000
    elif whowon == 2:
        if who_ai_first == 1:
            return -100000000
        else:
            return 100000000
    elif whowon == 0:
        return -100000000
    if ai_chose == "color":
        matches[1] = matches[1] - matches[0] - 100
    else:
        matches[0] = matches[0] - matches[1] - 100
    return max(matches[0], matches[1])


def calc_en_for_children(node, min_or_max):
    # for each child calculate
    ens = []
    for child in node.children:
        en = calc_en1(child)
        child.set_value(en)
        ens.append(en)
    if min_or_max == "min":
        (min_index, min_value) = min(enumerate(ens), key=operator.itemgetter(1))
        return min_index, min_value
    else:
        (max_index, max_value) = max(enumerate(ens), key=operator.itemgetter(1))
        return max_index, max_value


"""
   3 levels - including root as prf said, so 
     N
    / \ 
   N   N - apply max here and return
  /     \
  N      N  - apply - min here 
"""


def run_minmax(node, trace_array):

    if len(node.children[0].children) == 0:
        # calculate e(n) on each state
        min_or_max = "max" if node.level % 2 == 0 else "min"
        best_index, best_en = calc_en_for_children(node, min_or_max)
        node.set_value(best_en)
        trace_array.append(str(round(best_en, 1)))
        return best_index

    for child in node.children:
        run_minmax(child, trace_array)

    min_or_max = "max" if node.level % 2 == 0 else "min"
    # print("applied ", min_or_max)
    best_index, best_en = calc_en_for_children(node, min_or_max)
    node.set_value(best_en)
    return best_index


"""
Reference: https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
"""
def run_alphabeta(node, alpha, beta, ismaximizing, trace_array):
    if len(node.children) == 0:
        return calc_en(node), 0

    if ismaximizing:
        maxval = -inf
        maxIndex = 0
        for i in range(len(node.children)):
            result = run_alphabeta(node.children[i], alpha, beta, False, trace_array)
            value = result[0]
            if max(maxval, value) != maxval:
                maxval = value
                maxIndex = i
            alpha = max(alpha, maxval)
            if alpha >= beta:
                break
        trace_array.append(str(round(maxval, 1)))
        return maxval, maxIndex
    else:
        minval = inf
        minIndex = 0
        for i in range(len(node.children)):
            result = run_alphabeta(node.children[i], alpha, beta, True, trace_array)
            value = result[0]
            if min(minval, value) != minval:
                minval = value
                minIndex = i
            beta = min(beta, minval)
            if alpha >= beta:
                break
        trace_array.append(str(round(minval, 1)))
        return minval, minIndex