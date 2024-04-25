import pygame, sys
from board import *
from SudokuGenerator import *

pygame.init()
screen = pygame.display.set_mode((780, 880))
pygame.display.set_caption("Sudoku")
SCREEN_SIZE = 600
GRID_SIZE = 9
GRID_BOX_SIZE = SCREEN_SIZE // GRID_SIZE
pygame.init()
pygame.font.init()
GAME_FONT = pygame.font.Font(None, 36)

grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Global variables to track difficulty selection
difficulty_selected = False
game_started = False


def background(difficulty):
    screen.fill(White)
    board = Board(750, 750, screen, difficulty)
    board.draw()

    # Reset button
    resetfont = pygame.font.Font(None, 36)
    reset = resetfont.render("Reset", True, White, None)
    resetrect = reset.get_rect(topleft=(230, 800))
    pygame.draw.rect(screen, (255, 102, 0), resetrect)
    screen.blit(reset, resetrect)

    # Restart button
    restartfont = pygame.font.Font(None, 36)
    restart = restartfont.render("Restart", True, White, None)
    restartrect = restart.get_rect(topleft=(355, 800))
    pygame.draw.rect(screen, (255, 102, 0), restartrect)
    screen.blit(restart, restartrect)

    # Exit button
    exitfont = pygame.font.Font(None, 36)
    exit_ = exitfont.render("Exit", True, White, None)
    exitrect = exit_.get_rect(topleft=(505, 800))
    pygame.draw.rect(screen, (255, 102, 0), exitrect)
    screen.blit(exit_, exitrect)

    pygame.display.flip()



def start_screen():
    # background image
    bg = pygame.image.load("sudoimage.jpg")
    bg = pygame.transform.scale(bg, (780, 880))
    screen.blit(bg, (0, 0))

    # Welcome message
    welcomefont = pygame.font.Font(None, 50)
    welcome = welcomefont.render("Welcome to Sudoku", True, Black, None)
    screen.blit(welcome, (235, 100))

    # Select game mode message
    sgmfont = pygame.font.Font(None, 50)
    sgm = sgmfont.render("Select Game Mode:", True, Black, White)
    screen.blit(sgm, (235, 400))

    # Game mode buttons(Easy)
    easyfont = pygame.font.Font(None, 36)
    easy = easyfont.render("Easy", True, White, None)
    easyrect = easy.get_rect(topleft=(230, 490))
    pygame.draw.rect(screen, (255, 102, 0), easyrect)
    screen.blit(easy, easyrect)

    # Game mode button(Medium)
    medfont = pygame.font.Font(None, 36)
    med = medfont.render("Medium", True, White, None)
    medrect = med.get_rect(topleft=(350, 490))
    pygame.draw.rect(screen, (255, 102, 0), medrect)
    screen.blit(med, medrect)

    # Game mode button(Hard)
    hardfont = pygame.font.Font(None, 36)
    hard = hardfont.render("Hard", True, White, None)
    hardrect = hard.get_rect(topleft=(500, 490))
    pygame.draw.rect(screen, (255, 102, 0), hardrect)
    screen.blit(hard, hardrect)

    # Only show additional buttons if a difficulty has been selected

    return [easyrect, medrect, hardrect]

def select_cell(pos):
    global selected_cell
    x, y = pos
    row = y // GRID_BOX_SIZE
    col = x // GRID_BOX_SIZE
    selected_cell = (row, col) if grid[row][col] == 0 else None

def place_number(key):
    if selected_cell and 49 <= key <= 57:  # Key codes for 1-9
        num = key - 48  
        row, col = selected_cell
        if valid_move(row, col, num):
            grid[row][col] = num
            check_game_over()

def valid_move(row, col, number):
    # Check row
    if number in grid[row]:
        return False
    # Check column
    for r in range(GRID_SIZE):
        if grid[r][col] == number:
            return False
    # Check 3x3 square
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c] == number:
                return False
    return True

def check_game_over():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == 0 or not valid_move(row, col, grid[row][col]):
                return False


def main():
    global difficulty_selected, game_started  # Accessing the global flag
    running = True
    screen.fill(White)
    start_screen()
    difficulty_rects = start_screen()
    easyrect = start_screen()[0]
    medrect = start_screen()[1]
    hardrect = start_screen()[2]

    resetfont = pygame.font.Font(None, 36)
    reset = resetfont.render("Reset", True, White, None)
    resetrect = reset.get_rect(topleft=(230, 800))

    restartfont = pygame.font.Font(None, 36)
    restart = restartfont.render("Restart", True, White, None)
    restartrect = restart.get_rect(topleft=(355, 800))

    exitfont = pygame.font.Font(None, 36)
    exit_ = exitfont.render("Exit", True, White, None)
    exitrect = exit_.get_rect(topleft=(505, 800))

    while running:
        # Main Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


            if game_started:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    board = Board(780, 780, screen, selected_difficulty)
                    index = board.click(position[0], position[1])

                    #try function checking if click is in the parameters of the board, if not passes
                    try:
                        board.select(index[0], index[1])
                        cell = Cell(0, index[0], index[1], screen)
                        cell.selected = True
                        cell.draw() #Draw currently isnt drawing over the boxes correctly, gotta fix dimensions
                    except:
                        pass
                            

            # Mouse Button event for Easy Medium and Hard Modes
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not game_started:
                    if easyrect.collidepoint(event.pos):
                        for i, rect in enumerate(difficulty_rects):
                            difficulty_selected = True
                            difficulty_levels = ["easy", "medium", "hard"]
                            selected_difficulty = difficulty_levels[i]
                        game_started = True

                        sudoku_generator = SudokuGenerator()
                        sudoku_generator.Removed_cells = 30
                        sudoku_generator.fill_values()
                        sudoku_generator.remove_cells()
                        sudoku_board = sudoku_generator.get_board()

                        background(selected_difficulty)

                        font = pygame.font.Font(None, 36)
                        for i in range(Row_length):
                            for j in range(Row_length):
                                if sudoku_board[i][j] != 0:
                                    text = font.render(str(sudoku_board[i][j]), True, Black)
                                    text_rect = text.get_rect(
                                        center=(j * Cell_size + Cell_size // 2, i * Cell_size + Cell_size // 2))
                                    screen.blit(text, text_rect)

                        pygame.display.flip()
                        pygame.time.Clock().tick(60)

                        

                if not game_started:
                    if medrect.collidepoint(event.pos):
                        for i, rect in enumerate(difficulty_rects):
                            difficulty_selected = True
                            difficulty_levels = ["easy", "medium", "hard"]
                            selected_difficulty = difficulty_levels[i]
                        game_started = True

                        sudoku_generator = SudokuGenerator()
                        sudoku_generator.Removed_cells = 40
                        sudoku_generator.fill_values()
                        sudoku_generator.remove_cells()
                        sudoku_board = sudoku_generator.get_board()

                        background(selected_difficulty)

                        font = pygame.font.Font(None, 36)
                        for i in range(Row_length):
                            for j in range(Row_length):
                                if sudoku_board[i][j] != 0:
                                    text = font.render(str(sudoku_board[i][j]), True, Black)
                                    text_rect = text.get_rect(
                                        center=(j * Cell_size + Cell_size // 2, i * Cell_size + Cell_size // 2))
                                    screen.blit(text, text_rect)

                        pygame.display.flip()
                        pygame.time.Clock().tick(60)
                        


                        position = pygame.mouse.get_pos()
                        board = Board(780, 780, screen, selected_difficulty)
                        index = board.click(position[0], position[1])
                        board.select(index[0], index[1]) # <-- encounters error currently where if click is not in any of the cells
                        #TypeError: 'NoneType' object is not subscriptable for index[0] returns **Fix later
                        cell = Cell(0, index[0], index[1], screen)
                        cell.selected = True
                        cell.draw()

                if not game_started:
                    if hardrect.collidepoint(event.pos):
                        for i, rect in enumerate(difficulty_rects):
                            difficulty_selected = True
                            difficulty_levels = ["easy", "medium", "hard"]
                            selected_difficulty = difficulty_levels[i]
                        game_started = True

                        sudoku_generator = SudokuGenerator()
                        sudoku_generator.Removed_cells = 50
                        sudoku_generator.fill_values()
                        sudoku_generator.remove_cells()
                        sudoku_board = sudoku_generator.get_board()

                        background(selected_difficulty)

                        font = pygame.font.Font(None, 36)
                        for i in range(Row_length):
                            for j in range(Row_length):
                                if sudoku_board[i][j] != 0:
                                    text = font.render(str(sudoku_board[i][j]), True, Black)
                                    text_rect = text.get_rect(
                                        center=(j * Cell_size + Cell_size // 2, i * Cell_size + Cell_size // 2))
                                    screen.blit(text, text_rect)

                        pygame.display.flip()
                        pygame.time.Clock().tick(60)
                        
                
                            


                #Implementation of Reset, Return, Exit functionality

                else:
                    if resetrect.collidepoint(event.pos):
                        pass
                            # Reset button clicked
                        # Implement code to reset the board
                        # ...

                    elif restartrect.collidepoint(event.pos):
                        # Restart button clicked
                        # Reset game_started flag and any other necessary variables
                        game_started = False
                        # Return to the home screen
                        screen.fill(White)
                        start_screen()

                    elif exitrect.collidepoint(event.pos):
                        # Exit button clicked
                        pygame.quit()
                        sys.exit()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()