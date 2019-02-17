#!/usr/bin/python
# -*- coding: utf-8 -*-


class Red:

    def __init__(self, card, isdot, player):
        self.card = card
        self.color = 'red'
        self.dot = isdot
        self.player = player

    def position(self, row, column):
        self.row = row
        self.column = column
        return self

    def getposition(self):
        return self.row, self.column


class White:

    def __init__(self, card, isdot, player):
        self.card = card
        self.color = 'white'
        self.dot = isdot
        self.player = player

    def position(self,row, column):
        self.row = row
        self.column = column
        return self

    def getposition(self):
        return self.row, self.column


class Card:

    def __init__(self, row, column, player, o):
        self.row = row
        self.column = column
        self.player = player
        self.o = o

    def config(self, face, rotation, row, column):
        self.face = face
        if face == 1:
            self.left = Red(self, 1, self.player)
            self.right = White(self, 0, self.player)
        else:
            self.left = Red(self, 0, self.player)
            self.right = White(self, 1, self.player)

        self.rotation = rotation
        self.row = row
        self.column = column
