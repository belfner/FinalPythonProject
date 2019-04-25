from Cell import Cell
class Board:
    board = [[]]
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.board = [[None for x in range(width)] for y in range(height)]

    def checkIfMoveLegal(self,piece):
        for x in range(self.width):
            for y in range(self.height):
                if piece[y][x] and self.board[y][x]:
                    return False
        return True

    def addCells(self,piece):
        for x in range(self.width):
            for y in range(self.height):
                if piece[y][x]:
                    self.board[y][x] = piece[y][x]

    def checkIfSet(self,piece):
        for x in range(self.width):
            for y in range(self.height):
                if piece[y][x]:
                    self.board[y][x] = piece[y][x]