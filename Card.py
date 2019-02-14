#!/usr/bin/python
# -*- coding: utf-8 -*-


class Red:

    def __init__(self, card, isdot):
        self.card = card
        self.color = 'red'
        self.dot = isdot

    def position(self, row, column):
        self.row = row
        self.column = column
        return self

    def getposition(self):
        return self.row, self.column


class White:

    def __init__(self, card, isdot):
        self.card = card
        self.color = 'white'
        self.dot = isdot

    def position(self,row, column):
        self.row = row
        self.column = column
        return self

    def getposition(self):
        return self.row, self.column


class Card:

    def __init__(self, row, column, player):
        self.row = row
        self.column = column
        self.player = player

    def config(self, face, rotation, row, column):
        self.face = face
        if face == 1:
            self.left = Red(self, 1)
            self.right = White(self, 0)
        else:
            self.left = Red(self, 0)
            self.right = White(self, 1)

        self.rotation = rotation
        self.row = row
        self.column = column
