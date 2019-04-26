from Cell import Cell
import pprint
I0 = [[None, None, None, None],
      [   1,    1,    1,    1],
      [None, None, None, None],
      [None, None, None, None]]
I1 = [[None, None,    1, None],
      [None, None,    1, None],
      [None, None,    1, None],
      [None, None,    1, None]]
I2 = [[None, None, None, None],
      [None, None, None, None],
      [   1,    1,    1,    1],
      [None, None, None, None]]
I3 = [[None,    1, None, None],
      [None,    1, None, None],
      [None,    1, None, None],
      [None,    1, None, None]]
I = [ I1, I2, I3,I0]

L0 = [[None, None,    1, None],
      [   1,    1,    1, None],
      [None, None, None, None],
      [None, None, None, None]]
L1 = [[None,    1, None, None],
      [None,    1, None, None],
      [None,    1,    1, None],
      [None, None, None, None]]
L2 = [[None, None, None, None],
      [   1,    1,    1, None],
      [   1, None, None, None],
      [None, None, None, None]]
L3 = [[   1,    1, None, None],
      [None,    1, None, None],
      [None,    1, None, None],
      [None, None, None, None]]
L = [L0, L1, L2, L3]

J0 = [[   1, None, None, None],
      [   1,    1,    1, None],
      [None, None, None, None],
      [None, None, None, None]]
J1 = [[None,    1,    1, None],
      [None,    1, None, None],
      [None,    1, None, None],
      [None, None, None, None]]
J2 = [[None, None, None, None],
      [   1,    1,    1, None],
      [None, None,    1, None],
      [None, None, None, None]]
J3 = [[None,    1, None, None],
      [None,    1, None, None],
      [   1,    1, None, None],
      [None, None, None, None]]
J = [J0, J1, J2, J3]

O0 = [[None,    1,    1, None],
      [None,    1,    1, None],
      [None, None, None, None],
      [None, None, None, None]]
O = [O0, O0, O0, O0]

S0 = [[None,    1,    1, None],
      [   1,    1, None, None],
      [None, None, None, None],
      [None, None, None, None]]
S1 = [[None,    1, None, None],
      [None,    1,    1, None],
      [None, None,    1, None],
      [None, None, None, None]]
S2 = [[None, None, None, None],
      [None,    1,    1, None],
      [   1,    1, None, None],
      [None, None, None, None]]
S3 = [[   1, None, None, None],
      [   1,    1, None, None],
      [None,    1, None, None],
      [None, None, None, None]]
S = [S0, S1, S2, S3]

T0 = [[None,    1, None, None],
      [   1,    1,    1, None],
      [None, None, None, None],
      [None, None, None, None]]
T1 = [[None,    1, None, None],
      [None,    1,    1, None],
      [None,    1, None, None],
      [None, None, None, None]]
T2 = [[None, None, None, None],
      [   1,    1,    1, None],
      [None,    1, None, None],
      [None, None, None, None]]
T3 = [[None,    1, None, None],
      [   1,    1, None, None],
      [None,    1, None, None],
      [None, None, None, None]]
T = [T0, T1, T2, T3]

Z0 = [[   1,    1, None, None],
      [None,    1,    1, None],
      [None, None, None, None],
      [None, None, None, None]]
Z1 = [[None, None,    1, None],
      [None,    1,    1, None],
      [None,    1, None, None],
      [None, None, None, None]]
Z2 = [[None, None, None, None],
      [   1,    1, None, None],
      [None,    1,    1, None],
      [None, None, None, None]]
Z3 = [[None,    1, None, None],
      [   1,    1, None, None],
      [   1, None, None, None],
      [None, None, None, None]]
Z = [Z0, Z1, Z2, Z3]

class Piece:
    piece = [[]]
    color = (255, 255, 255)
    board = None
    def __init__(self, width, height, shapeName,board):
        self.board = board
        self.width = width
        self.height = height
        self.shapeName = shapeName
        self.piece = [[None for x in range(width)] for y in range(height)]
        if shapeName == 'I':
            self.positionSet = T
            self.rotation = 0
            self.shape = self.positionSet[self.rotation]
            self.posX = int(width/2)-2
            self.posY = -3
            for x in range(4):
                for y in range(4):
                    if self.shape[y][x]:
                        self.shape[y][x] = Cell((255,255,255))
            for y in range(4):
                for x in range(4):
                    if y+self.posY>0:
                        self.piece[y+self.posY][x+self.posX] =self.shape[y][x]

    def genBoard(self):
        self.piece = [[None for x in range(self.width)] for y in range(self.height)]
        for x in range(self.posX,self.posX+4):
            for y in range(self.posY, self.posY + 4):
                if x>=0 and x<self.width and y< self.height and y>=0:

                    self.piece[y][x] = self.shape[y-self.posY][x-self.posX]

    def getBoard(self):
        return self.board

    def __getitem__(self, key):
        return self.piece[key]

    def moveDown(self):
        self.posY+=1
        self.genBoard()

    def checkIfOutOfBoundsRight(self):
        for x in range(4):
            for y in range(4):
                if y >= 0:
                    if x+self.posX>=self.width and self.shape[y][x]:
                        return True
        return False

    def checkIfOutOfBoundsLeft(self):
        for x in range(4):
            for y in range(4):
                if y>=0:
                    if x+self.posX<0 and self.shape[y][x]:
                        return True
        return False

    def checkIfColisionAnywhere(self):
        for y in range(4):
            for x in range(0,4):
                if x+self.posX >= 0 and x+self.posX < self.width and y+self.posY < self.height and  y>=0:
                    if self.board.board[self.posY+y][x+self.posX] and self.shape[y][x]:
                        return True
        return False

    def checkIfColisionRight(self):
        for y in range(4):
            for x in range(3,4):
                if x+self.posX >= 0 and x+self.posX < self.width and y+self.posY < self.height and  y>=0:
                    if self.board.board[self.posY+y][x+self.posX] and self.shape[y][x]:
                        return True
        return False

    def checkIfColisionLeft(self):
        for y in range(4):
            for x in range(0,2):
                if x + self.posX >= 0 and x + self.posX < self.width and y + self.posY < self.height and  y>=0:
                    if self.board.board[self.posY+y][x+self.posX] and self.shape[y][x]:
                        return True
        return False

    def rotate(self):
        self.rotation = (self.rotation+1)%4
        self.shape = self.positionSet[self.rotation]
        for x in range(4):
            for y in range(4):
                if self.shape[y][x]:
                    self.shape[y][x] = Cell((255, 255, 255))
        if not self.checkIfRotateLegal():
            self.rotation = (self.rotation - 1) % 4
            self.shape = self.positionSet[self.rotation]
            for x in range(4):
                for y in range(4):
                    if self.shape[y][x]:
                        self.shape[y][x] = Cell((255, 255, 255))
            self.genBoard()
    #
    def checkIfRotateLegal(self):
        x = self.posX
        longI = self.shapeName == 'I' and (self.rotation == 1 or self.rotation == 3)
        self.genBoard()
        # Checks if Rotations moves blocks out of bounds then sees if it is posible to shift right or left to fix
        if self.checkIfOutOfBoundsRight():
            self.posX -= 1
            self.genBoard()
            if self.checkIfColisionLeft():
                self.posX = x
                return False
            if longI and self.checkIfOutOfBoundsRight():
                self.posX -= 1
                self.genBoard()
                if self.checkIfColisionLeft():
                    self.posX = x
                    return False
            if self.checkIfColisionAnywhere():
                return False
            else:
                return True

        if self.checkIfOutOfBoundsLeft():
            self.posX += 1
            self.genBoard()
            if self.checkIfColisionRight():
                self.posX = x
                return False
            if longI and self.checkIfOutOfBoundsLeft():
                self.posX += 1
                self.genBoard()
                if self.checkIfColisionRight():
                    self.posX = x
                    return False
            if self.checkIfColisionAnywhere():
                return False
            else:
                return True

        # Checks if Rotations moves blocks to overlap others then sees if it is posible to shift right or left to fix
        if self.checkIfColisionRight():
            self.posX -= 1
            self.genBoard()
            if self.checkIfColisionLeft():
                self.posX = x
                return False
            if longI and self.checkIfColisionRight():
                self.posX -= 1
                self.genBoard()
                if self.checkIfColisionLeft():
                    self.posX = x
                    return False
            if self.checkIfColisionAnywhere():
                self.posX = x
                return False
            else:
                return True

        if self.checkIfColisionLeft():
            self.posX += 1
            self.genBoard()
            if self.checkIfColisionRight():
                self.posX = x
                return False
            if longI and self.checkIfColisionLeft():
                self.posX += 1
                self.genBoard()
                if self.checkIfColisionRight():
                    self.posX = x
                    return False
            if self.checkIfColisionAnywhere():
                self.posX = x
                return False
            else:
                return True
        return True
    #     if self.checkIfOutOfBoundsRight():
    #         return 0
    #
    #     if self.checkIfOutOfBoundsLeft():
    #         return 1
    #
    #     right = self.checkIfColisionRight()
    #     left = self.checkIfColisionLeft()
    #     if not (not right or not left):
    #         return 2
    #     self.posX += 1
    #     self.genBoard()
    #     right = self.checkIfColisionRight()
    #     left = self.checkIfColisionLeft()
    #     self.posX -= 1
    #     if not (not right or not left):
    #         return 3
    #
    #     self.posX -= 1
    #     self.genBoard()
    #     right = self.checkIfColisionRight()
    #     left = self.checkIfColisionLeft()
    #     self.posX += 1
    #     if not (not right or not left):
    #         return 4
    #
    #     if self.shapeName == 'I' and (self.rotation == 0 or self.rotation == 2):
    #         self.posX += 2
    #         self.genBoard()
    #         right = self.checkIfColisionRight()
    #         left = self.checkIfColisionLeft()
    #         self.posX -= 2
    #         if not (not right or not left):
    #             return 5
    #
    #         self.posX -= 2
    #         self.genBoard()
    #         right = self.checkIfColisionRight()
    #         left = self.checkIfColisionLeft()
    #         self.posX += 2
    #         if not (not right or not left):
    #             return 6
    #
    #     return 7

    def move(self,dir):
        if dir == 0:
            self.posX+=1
            if self.checkIfOutOfBoundsRight() or self.checkIfColisionAnywhere():
                self.posX -= 1
        else:
            self.posX-=1
            if self.checkIfOutOfBoundsLeft()or self.checkIfColisionAnywhere():
                self.posX += 1
        self.genBoard()