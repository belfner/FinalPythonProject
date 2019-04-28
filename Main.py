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



    def __init__(self):
        pygame.init()

        self.size = (self.width*40+400, self.height*40)

        self.screen = pygame.display.set_mode(self.size)

        pygame.display.set_caption("Tetris")

        self.clock = pygame.time.Clock()

        self.continueGame = True

    def setUpBoard(self):
        self.gameover = False
        self.board = Board(self.width, self.height)

        d = True
        self.pieceSelect = ['T', 'L', 'I', 'J', 'O', 'S', 'Z']
        self.p = Piece(self.width, self.height, random.choice(self.pieceSelect), self.board)
        self.p.genBoard()
        # for x in range(10):
        #     p.moveDown()
        self.board.addCellsTemp(self.p)
        self.done = False

    def shouldGameTick(self,step):
        level = self.board.level
        if level == 0 or level == 1:
            if step%48 == 0 and step != 0:
                return True
        elif level == 1:
            if step%43 == 0 and step != 0:
                return True
        elif level == 2:
            if step%38 == 0 and step != 0:
                return True
        elif level == 3:
            if step%33 == 0 and step != 0:
                return True
        elif level == 4:
            if step%28 == 0 and step != 0:
                return True
        elif level == 5:
            if step%23 == 0 and step != 0:
                return True
        elif level == 6:
            if step%18 == 0 and step != 0:
                return True
        elif level == 7:
            if step%13 == 0 and step != 0:
                return True
        elif level == 8:
            if step%8 == 0 and step != 0:
                return True
        elif level == 9:
            if step%6 == 0 and step != 0:
                return True
        elif level <=12:
            if step%5 == 0 and step != 0:
                return True
        elif level <=15:
            if step%4 == 0 and step != 0:
                return True
        elif level <=18:
            if step%3 == 0 and step  != 0:
                return True
        elif level <=28:
            if step%2 == 0 and step != 0:
                return True
        else:
            return True
    def moveDown(self):
        if not self.board.checkIfSet(self.p):
            self.p.moveDown()
            self.board.addCellsTemp(self.p)
        else:
            print('Piece is Set')
            self.board.addCells(self.p)
            self.done = self.board.checkIfGameOver()
            self.board.checkCompleteRows()
            self.p = Piece(self.width, self.height, random.choice(self.pieceSelect), self.board)
            self.board.addCellsTemp(self.p)
    def hardDrop(self):
        while not self.board.checkIfSet(self.p):
            self.p.moveDown()
            self.board.addCellsTemp(self.p)
        print('Piece is Set')
        self.board.addCells(self.p)
        self.gameover = self.board.checkIfGameOver()
        if self.gameover:
            x = 1
        self.board.checkCompleteRows()
        self.p = Piece(self.width, self.height, random.choice(self.pieceSelect), self.board)
        self.board.addCellsTemp(self.p)


    def mainLoop(self):
        while self.continueGame:
            self.setUpBoard()
            self.gameLoop()
        # Close the window and quit.
        pygame.quit()
    def gameLoop(self):
        steps = 0

        while not self.done:
            hardDrop = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                    self.continueGame = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.done = True
                        self.continueGame = False
                    if event.key == pygame.K_r:
                        self.done = True
                    if not self.pause and not self.gameover:
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
                        if event.key == pygame.K_SPACE:
                            self.hardDrop()
                            hardDrop = True
                    if event.key == pygame.K_p:
                        self.pause = not self.pause
            # --- Game logic should go here
            if not self.pause and not self.gameover:
                if self.shouldGameTick(steps) and not hardDrop:
                    self.moveDown()
            # --- Drawing code should go here
            if not self.pause:
                self.screen.fill(self.BLACK)
            else:
                self.screen.fill(self.WHITE)



            pygame.draw.rect(self.screen, (66, 79, 159),
(self.width * 40, 0, self.width * 40 + 200, self.height * 40))
            self.drawBoard(self.screen,self.board,self.width,self.height)
            self.board.drawGUI(self.screen)
            if self.pause:
                self.board.drawPause(self.screen)
            elif self.gameover:
                self.board.drawGameover(self.screen)
            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            self.clock.tick(60)
            steps+=1




if __name__ == '__main__':
    g = Game()
    g.mainLoop()