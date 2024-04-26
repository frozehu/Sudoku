import pygame
import random

# Constants
Width = 780
Height = 780
Row_length = 9
Cell_size = Width // Row_length
White = (255, 255, 255)
Black = (0, 0, 0)
Gray = (200, 200, 200)
Fps = 60
class SudokuGenerator:
    Removed_cells = 30
    def __init__(self):
        self.board = [[0] * Row_length for _ in range(Row_length)]

    def get_board(self):
        return self.board

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        for row in self.board:
            if row[col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        for i in range(3):
            for j in range(3):
                if self.board[row_start + i][col_start + j] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        return (self.valid_in_row(row, num) and
                self.valid_in_col(col, num) and
                self.valid_in_box(row - row % 3, col - col % 3, num))

    def fill_box(self, row_start, col_start):
        nums = [i for i in range(1, 10)]
        random.shuffle(nums)
        for i in range(3):
            for j in range(3):
                self.board[row_start + i][col_start + j] = nums.pop()

    def fill_diagonal(self):
        for i in range(0, Row_length, 3):
            self.fill_box(i, i)

    def fill_remaining(self, row, col):
        if col >= Row_length and row < Row_length - 1:
            row += 1
            col = 0
        if row >= Row_length and col >= Row_length:
            return True
        if row < 3:
            if col < 3:
                col = 3
        elif row < Row_length - 3:
            if col == int(row / 3) * 3:
                col += 3
        else:
            if col == Row_length - 3:
                row += 1
                col = 0
                if row >= Row_length:
                    return True
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, 3)

    def remove_cells(self):
        cells_to_remove = self.Removed_cells
        while cells_to_remove > 0:
            row = random.randint(0, Row_length - 1)
            col = random.randint(0, Row_length - 1)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                cells_to_remove -= 1
