import pygame
from Board import Board
from Piece import Piece
import random

class Game:
    width = 10
    height = 20
    pause = False

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
        self.pieceSelect = ['T', 'L', 'I', 'J', 'O', 'S', 'Z']
        self.p = Piece(self.width,self.height,random.choice(self.pieceSelect),self.board)
        self.p.genBoard()
        # for x in range(10):
        #     p.moveDown()
        self.board.addCellsTemp(self.p)

        self.mainLoop()

    def moveDown(self):
        if not self.board.checkIfSet(self.p):
            self.p.moveDown()
            self.board.addCellsTemp(self.p)
        else:
            print('Piece is Set')
            self.board.addCells(self.p)
            self.board.checkCompleteRows()
            self.p = Piece(self.width, self.height, random.choice(self.pieceSelect), self.board)
            self.board.addCellsTemp(self.p)
    def mainLoop(self):
        while not self.done:


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                elif event.type == pygame.KEYDOWN:
                    if not self.pause:
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
                    if event.key == pygame.K_ESCAPE:
                        self.pause = not self.pause
            # --- Game logic should go here
            if not self.pause:
                self.moveDown()
            # --- Drawing code should go here
                self.screen.fill(self.BLACK)
            else:
                self.screen.fill(self.WHITE)
                self.board.drawPause(self.screen)
            self.drawBoard(self.screen,self.board,self.width,self.height)
            self.board.drawGUI(self.screen)
            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            self.clock.tick(4)

        # Close the window and quit.
        pygame.quit()


if __name__ == '__main__':
    g = Game()
    g.mainLoop()