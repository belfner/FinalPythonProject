import pygame
from Board import Board
from Piece import Piece
width = 10
height = 20

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def drawBoard(screen,board,width,height):
    for y in range(height):
        for x in range(width):
            if board[y][x]:
                pygame.draw.rect(screen, board[y][x].color, (40*x, 40*y, 40, 40))


pygame.init()

size = (width*40, height*40)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tetris")

done = False

clock = pygame.time.Clock()

board = Board(width,height)

d = True
p = Piece(width,height,'T',board)
p.genBoard()
# for x in range(10):
#     p.moveDown()
board.addCellsTemp(p)
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                p.move(1)
                board.addCellsTemp(p)
            if event.key == pygame.K_RIGHT:
                p.move(0)
                board.addCellsTemp(p)
            if event.key  == pygame.K_UP:
                p.rotate()
                board.addCellsTemp(p)
            if event.key == pygame.K_DOWN:
                if not board.checkIfSet(p):
                    p.moveDown()
                    board.addCellsTemp(p)
                else:
                    print('Piece is Set')
                    board.addCells(p)
                    p = Piece(width, height, 'T',board)
                    board.addCellsTemp(p)
    # --- Game logic should go here

    screen.fill(BLACK)
    # --- Drawing code should go here
    board.checkCompleteRows()
    drawBoard(screen,board,width,height)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()