from Cell import Cell
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

L = [L0, L1, L2, L3]
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

J = [J0, J1, J2, J3]
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

O = [O0, O0, O0, O0]
O0 = [[None,    1,    1, None],
      [None,    1,    1, None],
      [None, None, None, None],
      [None, None, None, None]]

S = [S0, S1, S2, S3]
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

T = [T0, T1, T2, T3]
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

Z = [Z0, Z1, Z2, Z3]
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


class Piece:
    piece = [[]]
    color = (255, 255, 255)

    def __init__(self, width, height, shapeName):
        self.width = width
        self.height = height
        self.shapeName = shapeName
        self.piece = [[None for x in range(width)] for y in range(height+3)]
        if shapeName == 'I':
            self.shape = I1
            self.posX = int(width/2)-2
            self.posY = 0
            for x in range(4):
                for y in range(4):
                    if self.shape[y][x]:
                        self.shape[y][x] = Cell((255,255,255))
            for y in range(4):
                for x in range(4):
                    self.piece[y+self.posY][x+self.posX] =self.shape[y][x]

    def genBoard(self):
        self.piece = [[None for x in range(self.width)] for y in range(self.height + 3)]
        if self.shapeName == 'I':
            for x in range(self.posX,self.posX+4):
                for y in range(self.posY, self.posY + 4):
                    self.piece[y][x] = self.shape[y-self.posY][x-self.posX]

    def getBoard(self):
        return self.board[3:]

    def __getitem__(self, key):
        return self.piece[key+3]

    def moveDown(self):
        self.posY+=1
        self.genBoard()

    def move(self,dir):
        if dir == 0:
            if self.posX<self.width-4:
                self.posX+=1
        else:
            if self.posX>0:
                self.posX-=1
        self.genBoard()