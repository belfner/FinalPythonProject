from Cell import Cell
I0 = [[None, None, None, None]
      [   1,    1,    1,    1]
      [None, None, None, None]
      [None, None, None, None]]
I1 = [[None, None,    1, None]
      [None, None,    1, None]
      [None, None,    1, None]
      [None, None,    1, None]]
I2 = [[None, None, None, None]
      [None, None, None, None]
      [   1,    1,    1,    1]
      [None, None, None, None]]
I3 = [[None,    1, None,None]
      [None,    1, None, None]
      [None,    1, None, None]
      [None,    1, None, None]]


class Piece:
    piece = [[]]
    color = (255, 255, 255)

    def __init__(self, width, height, shapeName):
        self.width = width
        self.height = height
        self.shapeName = shapeName
        if shapeName == 'I':
            self.shape = I0
            self.posX = (width/2)-2
            self.posY = 0
            for x in range(4):
                for y in range(4):
                    if self.shape[x][y]:
                        self.shape[x][y] = Cell((255,255,255))

    def genBoard(self):
        self.board = [[None for x in range(self.width)] for y in range(self.height + 3)]
        if self.shapeName == 'I':
            for x in range(self.posX,self.posX+4):
                for y in range(self.posY, self.posY + 4):
                    self.board[y][x] = self.shape[y-self.posY][x-self.posX]

    def getBoard(self):
        return self.board[3:]