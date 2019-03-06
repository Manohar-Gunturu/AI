"""
Track keeps row position
default track of root node is 12,12,12,12,12,12,12,12
so we can efficiently generates different states

_Note_: number of levels = number of moves, so maximum levels = 60
"""


class Node:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
        self.children = []
        self.value = 0
        if parent is not None:
            self.track = []
            self.level = parent.level + 1

    def update_track(self, column_pos):
        self.track[column_pos] = self.track[column_pos] - 1

    def set_track(self, track):
        self.track = track

    def set_level(self, level):
        self.level = level

    def set_value(self, value):
        self.value = value

    def add_children(self, child_node):
        self.children.append(child_node)
