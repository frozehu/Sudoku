import pygame
import random

# Constants
Width = 540
Height = 540
Row_length = 9
Removed_cells = 30
Cell_size = Width // Row_length
White = (255, 255, 255)
Black = (0, 0, 0)
Gray = (200, 200, 200)
Fps = 60

class SudokuGenerator:
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
        cells_to_remove = Removed_cells
        while cells_to_remove > 0:
            row = random.randint(0, Row_length - 1)
            col = random.randint(0, Row_length - 1)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                cells_to_remove -= 1

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Sudoku")

# Create Sudoku Generator
sudoku_generator = SudokuGenerator()
sudoku_generator.fill_values()
sudoku_generator.remove_cells()
sudoku_board = sudoku_generator.get_board()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the Sudoku board
    screen.fill(White)
    for i in range(Row_length + 1):
        if i % 3 == 0:
            pygame.draw.line(screen, Black, (0, i * Cell_size), (Width, i * Cell_size), 4)
            pygame.draw.line(screen, Black, (i * Cell_size, 0), (i * Cell_size, Height), 4)
        else:
            pygame.draw.line(screen, Black, (0, i * Cell_size), (Width, i * Cell_size), 2)
            pygame.draw.line(screen, Black, (i * Cell_size, 0), (i * Cell_size, Height), 2)

    # Draw numbers on the board
    font = pygame.font.Font(None, 36)
    for i in range(Row_length):
        for j in range(Row_length):
            if sudoku_board[i][j] != 0:
                text = font.render(str(sudoku_board[i][j]), True, Black)
                text_rect = text.get_rect(center=(j * Cell_size + Cell_size // 2, i * Cell_size + Cell_size // 2))
                screen.blit(text, text_rect)

    pygame.display.flip()
    pygame.time.Clock().tick(Fps)

pygame.quit()