from Util import state_conv1

minmax_func = {1: min, 2: max}


def calc_en(child):
    sum_w_o = 0
    sum_w_d = 0
    sum_r_o = 0
    sum_r_d = 0
    for i in range(12):
        for j in range(8):
            cellval = (12 - i) * 10 + j + 1
            val = state_conv1(i, j, child.state)
            sum_w_o += cellval if val == 1 else 0
            sum_w_d += cellval if val == 3 else 0
            sum_r_o += cellval if val == 2 else 0
            sum_w_d += cellval if val == 4 else 0
        print("\n")
    en = sum_w_o + (3 * sum_w_d) - (2 * sum_r_d) - (1.5 * sum_r_o)
    return en


def calc_en_for_children(node, min_or_max):
    # for each child calculate
    ens = []
    for child in node.children:
        en = calc_en(child)
        child.set_value(en)
        ens.append(en)
    if min_or_max == "min":
        return min(ens)
    else:
        return max(ens)


"""
   3 levels - including root as prf said, so 
     N
    / \ 
   N   N - apply max here and return
  /     \
  N      N  - apply - min here 
"""


def run_minmax(node, levels):
    if len(node.children) == 0:  # it means we reached leafs
        return None

    if len(node.children[0].children) == 0:
        # calculate e(n) on each state
        min_or_max = "max" if node.level % 2 == 0 else "min"
        best_en = calc_en_for_children(node, min_or_max)
        node.set_value(best_en)
        return None

    for child in node.children:
        run_minmax(child, levels)

    min_or_max = "max" if node.level % 2 == 0 else "min"
    best_en = calc_en_for_children(node, min_or_max)
    node.set_value(best_en)
    return None
