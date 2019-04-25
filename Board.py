from Cell import Cell
from copy import deepcopy
import pprint
class Board:
    board = [[]]
    tempBoard = [[]]
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.board = [[None for x in range(width)] for y in range(height)]
        self.tempBoard = [[None for x in range(width)] for y in range(height)]

    def checkIfMoveLegal(self,piece):
        for y in range(self.height):
            for x in range(self.width):
                if piece[y][x] and self.board[y][x]:
                    return False
        return True

    def addCells(self,piece):
        for y in range(self.height):
            for x in range(self.width):
                if piece[y][x]:
                    self.board[y][x] = piece[y][x]

    def addCellsTemp(self,piece):
        self.tempBoard = deepcopy(self.board)
        for y in range(self.height):
            for x in range(self.width):
                if piece[y][x]:
                    self.tempBoard[y][x] = piece[y][x]

    def checkIfSet(self,piece):
        for y in range(self.height):
            for x in range(self.width):
                if piece[y][x]:
                    if y == self.height-1:
                        return True
                    elif self.board[y+1][x]:
                        return True
        return False

    def __getitem__(self, key):
        return self.tempBoard[key]