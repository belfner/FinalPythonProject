from Cell import Cell
from copy import deepcopy
import pprint
import pygame
class Board:
    board = [[]]
    tempBoard = [[]]
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.board = [[None for x in range(width)] for y in range(height)]
        self.tempBoard = [[None for x in range(width)] for y in range(height)]
        self.score = 0
        self.level = 1
        self.lineclears = 10

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
    def checkIfGameOver(self):
        for col in range(self.width):
            if self.board[0][col] != None:
                row_complete = 0
                return True
        return False
    def checkCompleteRows(self):
        reward = 0
        row_complete = 1
        for row in range(self.height):
            for col in range(self.width):
                if self.board[row][col] == None:
                    row_complete = 0
                    break
            if row_complete:
                self.shiftBoard(row)
                reward += 1
            else:
                row_complete = 1
        if reward:

            if reward == 1:
                self.score += (100*(self.level+1))
            elif reward == 2:
                self.score += (300*(self.level+1))
            elif reward == 3:
                self.score += (500*(self.level+1))
            else:
                self.score += (800*(self.level+1))
            self.lineclears += reward
            self.level = int(self.lineclears/10)

    def drawGUI(self,screen):
        basicfont = pygame.font.SysFont(None, 48)
        gameName = basicfont.render('TETRIS', True, (255, 255, 255), (66, 179, 180))
        scoreText = basicfont.render('Score:', True, (255, 255, 255), (66, 179, 180))
        levelText = basicfont.render('Level:', True, (255, 255, 255), (66, 179, 180))
        score = basicfont.render(str(self.score), True, (255, 255, 255), (66, 179, 180))
        level = basicfont.render(str(self.level), True, (255, 255, 255), (66, 179, 180))
        screen.blit(gameName, (440, 50))
        screen.blit(levelText, (410, 160))
        screen.blit(level, (520, 160))
        screen.blit(scoreText, (410, 200))
        screen.blit(score, (520, 200))

        basicfont = pygame.font.SysFont(None, 24)
        text = basicfont.render('Made By:', True, (255, 255, 255), (66, 179, 180))
        screen.blit(text, (410, 250))
        text = basicfont.render('Jack, Ben, and Nate', True, (255, 255, 255), (66, 179, 180))
        screen.blit(text, (410, 270))

    def drawPause(selfself,screen):
        basicfont = pygame.font.SysFont(None, 64)
        paused = basicfont.render('PAUSED', True, (255, 255, 255), (66, 179, 180))
        screen.blit(paused, (110, 200))
        basicfont = pygame.font.SysFont(None, 48)
        instructions = basicfont.render('Press P to resume', True, (255, 255, 255), (66, 179, 180))
        screen.blit(instructions, (57, 250))

    def drawGameover(selfself,screen):
        basicfont = pygame.font.SysFont(None, 64)
        paused = basicfont.render('GAME OVER', True, (255, 255, 255), (66, 179, 180))
        screen.blit(paused, (110, 200))
        basicfont = pygame.font.SysFont(None, 48)
        instructions = basicfont.render('Press R to restart', True, (255, 255, 255), (66, 179, 180))
        screen.blit(instructions, (57, 250))





    def __getitem__(self, key):
        return self.tempBoard[key]

        # reward = 0
        # row_complete = True
        # for row in range(self.height):
        #     for col in range(self.width):
        #         if self.board[row][col] == None:
        #             row_complete = False
        #             break
        #     if row_complete:
        #         self.shiftBoard(row)
        #         reward+=1
        #     else:
        #         row_comwplete = True
        #