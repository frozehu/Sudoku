import pygame, sys
from board import *
from SudokuGenerator import *
from Cell import *

pygame.init()
screen = pygame.display.set_mode((780, 880))
pygame.display.set_caption("Sudoku")

# Global variables to track difficulty selection
difficulty_selected = False
game_started = False

class RectCell(pygame.Rect):
    '''
    A class built upon the pygame Rect class used to represent individual cells in the game.
    This class has a few extra attributes not contained within the base Rect class.
    '''

    def __init__(self, left, top, row, col):
        super().__init__(left, top, 81, 81)
        self.row = row
        self.col = col

cell_size = 81
minor_grid_size = 1
major_grid_size = 3
buffer = 18

def create_cells():
    '''Creates all 81 cells with RectCell class.'''
    cells = [[] for _ in range(9)]

    row = 0
    col = 0
    left = 18
    top = 18

    while row < 9:
        while col < 9:
            cells[row].append(RectCell(left, top, row, col))

            # Update attributes for next RectCell
            left += cell_size + minor_grid_size
            if col != 0 and (col + 1) % 3 == 0:
                left = left + major_grid_size - minor_grid_size
            col += 1

        # Update attributes for next RectCell
        top += cell_size + minor_grid_size
        if row != 0 and (row + 1) % 3 == 0:
            top = top + major_grid_size - minor_grid_size
        left = buffer + major_grid_size
        col = 0
        row += 1

    return cells

cells = create_cells()



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
                        cell.draw()

                        #Draw currently isnt drawing over the boxes correctly, gotta fix dimensions
                    except:
                        pass
                if event.type == pygame.KEYDOWN:
                    # if event.key == pygame.K_1:
                    #     position = pygame.mouse.get_pos()
                    #     board = Board(780, 780, screen, selected_difficulty)
                    #     index = board.click(position[0], position[1])
                    #     value = pygame.K_1 - 48
                    #     value2 = font.render(str(value), True, (0, 0, 0))
                    #     print(value)
                    #     screen.blit(value2, index)
                    if event.type == pygame.KEYDOWN:
                        if (event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or
                                event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or
                                event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9):

                            # Determine the value pressed (from 1 to 9)
                            value = event.key - pygame.K_1 + 1

                            # Get the mouse position and convert it to board cell indices
                            position = pygame.mouse.get_pos()
                            board = Board(780, 780, screen, selected_difficulty)
                            index = board.click(position[0], position[1])

                            # Check if the clicked cell is valid
                            if index:
                                # Update the board with the pressed number (if cell is valid)
                                sudoku_board = SudokuGenerator().get_board()
                                sudoku_board[index[0]][index[1]] = value

                                # Clear the cell area to redraw the updated number
                                pygame.draw.rect(screen, White,
                                                 (index[1] * Cell_size, index[0] * Cell_size, Cell_size, Cell_size))

                                # Render and blit the updated number onto the cell
                                font = pygame.font.Font(None, 36)
                                text_surface = font.render(str(value), True, Black)
                                text_rect = text_surface.get_rect(center=(
                                index[1] * Cell_size + Cell_size // 2, index[0] * Cell_size + Cell_size // 2))
                                screen.blit(text_surface, text_rect)

                                pygame.display.flip()

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