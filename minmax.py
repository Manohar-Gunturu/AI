from Util import state_conv1,card_number
import operator


def calc_en1(child):
    return calc_en(child)


def calc_en(child):
    sum_w_o = 0.0
    sum_w_d = 0.0
    sum_r_o = 0.0
    sum_r_d = 0.0
    for i in range(12):
        for j in range(8):
            cellval = (12 - i) * 10 + j + 1
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


def run_minmax(node):
    if len(node.children) == 0:  # it means we reached leafs
        return None

    if len(node.children[0].children) == 0:
        # calculate e(n) on each state
        min_or_max = "max" if node.level % 2 == 0 else "min"
        # print("applied ", min_or_max)
        best_index, best_en = calc_en_for_children(node, min_or_max)
        node.set_value(best_en)
        return best_index

    for child in node.children:
        run_minmax(child)

    min_or_max = "max" if node.level % 2 == 0 else "min"
    #print("applied ", min_or_max)
    best_index, best_en = calc_en_for_children(node, min_or_max)
    node.set_value(best_en)
    return best_index


def run_alphabeta(node):
    if len(node.children) == 0:  # it means we reached leafs
        return None

    if len(node.children[0].children) == 0:
        # calculate e(n) on each state
        min_or_max = "max" if node.level % 2 == 0 else "min"
        # print("applied ", min_or_max)
        best_index, best_en = calc_en_for_children(node, min_or_max)
        node.set_value(best_en)
        return best_index

    for child in node.children:
        run_minmax(child)

    min_or_max = "max" if node.level % 2 == 0 else "min"
    #print("applied ", min_or_max)
    best_index, best_en = calc_en_for_children(node, min_or_max)
    node.set_value(best_en)
    return best_index
