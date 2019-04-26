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
        self.score = 0

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

    def shiftBoard(self,shiftFrom):
        for row in range(len(self.board)):
            if shiftFrom == row:
                self.board.pop(shiftFrom)
                self.board.insert(0, [None for n in range(self.width)])
                return

    def checkCompleteRows(self):
        reward = 10
        row_complete = 1
        for row in range(self.height):
            for col in range(self.width):
                if self.board[row][col] == None:
                    row_complete = 0
                    break
            if row_complete:
                self.shiftBoard(row)
                reward *= 2
            else:
                row_complete = 1






    def __getitem__(self, key):
        return self.tempBoard[key]