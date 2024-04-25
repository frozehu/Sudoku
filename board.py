import pygame, sys
from Cell import *

pygame.init()
screen = pygame.display.set_mode((750, 750))
pygame.display.set_caption("Sudoku")

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        # Initially was giving a not enough parameters error, add None and screen for it 
        #to be able to run not sure if its correct
        self.cells = [[Cell(None, row, col, screen) for col in range(9)] for row in range(9)]
        self.selected_cell = None

    def draw(self):
        box_width = self.width // 9
        box_height = self.height // 9
        for i in range(10):
            line_width = 5 if i % 3 > 0 else 10
            #changed lines to go from 730 to 760 so that boxes werent uneven
            pygame.draw.line(screen, pygame.Color("black"), pygame.Vector2((i * box_height) + 15, 15),
                             pygame.Vector2((i * box_height) + 15, 760), line_width)
            pygame.draw.line(screen, pygame.Color("black"), pygame.Vector2(15, (i * box_width) + 15),
                             pygame.Vector2(760, (i * box_width) + 15), line_width)
    def select(self, row, col):
        self.selected_cell = (row, col)
    def click(self, x, y):
        row = y // (self.height // 9)
        col = x // (self.width // 9)
        if 0 <= row < 9 and 0 <= col < 9:
            return (row, col)
        else:
            return None
    def clear(self):
        if self.selected_cell:
            self.cells[self.selected_cell[0]][self.selected_cell[1]].clear()
    def sketch(self, value):
        if self.selected_cell:
            self.cells[self.selected_cell[0]][self.selected_cell[1]].set_sketched_value(value)
    def place_number(self, value):
        self.cells[self.selected_cell[0]][self.selected_cell[1]].set_sketched_value(value)
    def reset_to_original(self):
        pass
    def is_full(self):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    return False
        return True
    def update_board(self):
        pass
    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    return (row, col)
        return False
    # def check_board(self):
    #     pass

