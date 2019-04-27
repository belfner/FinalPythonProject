import pygame
from Board import Board
from Piece import Piece

class Game:
    width = 10
    height = 20

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    def drawBoard(self,screen,board,width,height):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x]:
                    pygame.draw.rect(self.screen, self.board[y][x].color, (40*x, 40*y, 40, 40))
                    pygame.draw.rect(self.screen, (66, 79, 159), (self.width*40, 0, self.width*40+200, self.height*40))


    def __init__(self):
        pygame.init()

        self.size = (self.width*40+200, self.height*40)

        self.screen = pygame.display.set_mode(self.size)

        pygame.display.set_caption("Tetris")

        self.done = False

        self.clock = pygame.time.Clock()

        self.board = Board(self.width,self.height)

        d = True
        self.p = Piece(self.width,self.height,'T',self.board)
        self.p.genBoard()
        # for x in range(10):
        #     p.moveDown()
        self.board.addCellsTemp(self.p)

        self.mainLoop()

    def moveDown(self):
        self.p.moveDown()
        if not self.board.checkIfSet(self.p):
            self.board.addCellsTemp(self.p)
        else:
            print('Piece is Set')
            self.board.addCells(self.p)
            self.board.checkCompleteRows()
            self.p = Piece(self.width, self.height, 'T', self.board)
            self.board.addCellsTemp(self.p)
    def mainLoop(self):
        while not self.done:


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.p.move(1)
                        self.board.addCellsTemp(self.p)
                    if event.key == pygame.K_RIGHT:
                        self.p.move(0)
                        self.board.addCellsTemp(self.p)
                    if event.key  == pygame.K_UP:
                        self.p.rotate()
                        self.board.addCellsTemp(self.p)
                    if event.key == pygame.K_DOWN:
                        self.moveDown()
            # --- Game logic should go here
            self.moveDown()
            # --- Drawing code should go here
            self.screen.fill(self.BLACK)
            self.drawBoard(self.screen,self.board,self.width,self.height)
            self.board.drawGUI(self.screen)
            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            self.clock.tick(5)

        # Close the window and quit.
        pygame.quit()


if __name__ == '__main__':
    g = Game()
    g.mainLoop()