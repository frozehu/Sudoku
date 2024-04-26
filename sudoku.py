import pygame, sys
from board import *
from SudokuGenerator import *
import copy
pygame.init()
screen = pygame.display.set_mode((780, 880))
pygame.display.set_caption("Sudoku")

# Global variables to track difficulty selection
difficulty_selected = False
game_started = False
selected = False



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
    global difficulty_selected, game_started, selected_difficulty, copy_of_sudoku, sudoku_board, font
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

            for i, rect in enumerate(difficulty_rects):
                difficulty_selected = True
                difficulty_levels = ["easy", "medium", "hard"]
                selected_difficulty = difficulty_levels[i]

            # Create the board instance outside the event loop
            board = Board(780, 780, screen, selected_difficulty)

            # Inside the event loop
            if game_started:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    index = board.click(position[0], position[1])

                    # Check if the index is valid before proceeding
                    if index is not None:
                        # Removes previously selected cell
                        board = Board(750, 750, screen, selected_difficulty)
                        board.draw()
                        board.select(index[0], index[1])

                        # Adjust the position of the cell based on the index
                        cell = board.cells[index[0]][index[1]]
                        if index[1] in [3, 4, 5]:
                            cell.x += 6
                        elif index[1] in [6, 7, 8]:
                            cell.x += 12

                        if index[0] in [3, 4, 5]:
                            cell.y += 6
                        elif index[0] in [6, 7, 8]:
                            cell.y += 12

                        # Set the selected flag and draw the cell
                        cell.draw()
                        print(index)
                        cell.selected = True

                # This line should be unindented to be at the same level as the if statement above
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or
                            event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or
                            event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9):

                        # Determine the value pressed (from 1 to 9)
                        value = event.key - pygame.K_1 + 1

                        # You can only type in a selected box

                        # Check if the clicked cell is valid
                        if index:
                            # Check if the cell is empty
                            if copy_of_sudoku[index[0]][index[1]] == 0:
                                # Update the board with the pressed number
                                sudoku_board[index[0]][index[1]] = value
                                print(copy_of_sudoku)
                                print(sudoku_board)

                                for i in range(Row_length):
                                    for j in range(Row_length):
                                        if sudoku_board[i][j] != 0:
                                            text = font.render(str(sudoku_board[i][j]), True, Black, White)
                                            text_rect = text.get_rect(
                                                center=(
                                                j * Cell_size + Cell_size // 2, i * Cell_size + Cell_size // 2))
                                            screen.blit(text, text_rect)

                                pygame.display.flip()
                                #Push

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
                        copy_of_sudoku = copy.deepcopy(sudoku_board)
                        print(sudoku_board)
                        

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
                        copy_of_sudoku = copy.deepcopy(sudoku_board)
                        print(sudoku_board)

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
                        copy_of_sudoku = copy.deepcopy(sudoku_board)
                        print(sudoku_board)

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