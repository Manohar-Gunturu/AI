from Util import state_conv1, card_number
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

def calc_en(child):
    if len(child.children) != 0:
        return child.value
    global en_count
    en_count += 1
    sum_w_o = 0.0
    sum_w_d = 0.0
    sum_r_o = 0.0
    sum_r_d = 0.0
    for i in range(12):
        for j in range(8):
            cellval = (12 - i) * 10 + j + 1 - 10
            val = state_conv1(i, j, child.state)
            sum_w_o += cellval if val % 100 == 1 else 0.0
            sum_w_d += cellval if val % 100 == 3 else 0.0
            sum_r_o += cellval if val % 100 == 2 else 0.0
            sum_w_d += cellval if val % 100 == 4 else 0.0
    en = sum_w_o + (3.0 * sum_w_d) - (2.0 * sum_r_d) - (1.5 * sum_r_o)
    return en


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
        # print("applied ", min_or_max)
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
        maxEval = -inf
        maxIndex = 0
        for i in range(len(node.children)):
            result = run_alphabeta(node.children[i], alpha, beta, False, trace_array)
            value = result[0]
            if max(maxEval, value) != maxEval:
                maxEval = value
                maxIndex = i
            alpha = max(alpha, maxEval)
            if alpha >= beta:
                break
        trace_array.append(str(round(maxEval, 1)))
        return maxEval, maxIndex
    else:
        minEval = inf
        minIndex = 0
        for i in range(len(node.children)):
            result = run_alphabeta(node.children[i], alpha, beta, True, trace_array)
            value = result[0]
            if min(minEval, value) != minEval:
                minEval = value
                minIndex = i
            beta = min(beta, minEval)
            if alpha >= beta:
                break
        trace_array.append(str(round(minEval, 1)))
        return minEval, minIndex
