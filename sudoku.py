import pygame, sys
from board import *

pygame.init()
screen = pygame.display.set_mode((750, 750))
pygame.display.set_caption("Sudoku")

def background():
    screen.fill(pygame.Color("white"))
    pygame.draw.rect(screen, pygame.Color("black"), pygame.Rect(15, 15, 720, 720), 10)
    board = Board(750, 750, screen, "easy")
    board.draw()
def game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    background()
    pygame.display.flip()

while True:
    game()