import pygame, sys
from board import *
from SudokuGenerator import *

pygame.init()
screen = pygame.display.set_mode((780, 780))
pygame.display.set_caption("Sudoku")

#def starting_screen():
    # put starting screen things in here? Ran into accessing button collide points outside of definition
    # Ref lines 24 - 59

def background():
    screen.fill(White)
    board = Board(750, 750, screen, "easy")
    board.draw()

def start_screen():
    # background image
    bg = pygame.image.load("sudoimage.jpg")
    bg = pygame.transform.scale(bg, (780, 780))
    screen.blit(bg, (0, 0))

    # Welcome message
    welcomefont = pygame.font.Font(None, 50)
    welcome = welcomefont.render("Welcome to Sudoku", True, Black, None)
    screen.blit(welcome, (235,100))

    # Select game mode message
    sgmfont = pygame.font.Font(None, 50)
    sgm = sgmfont.render("Select Game Mode:", True, Black, None)
    screen.blit(sgm, (235, 400))

    # Game mode buttons(Easy)
    easyfont = pygame.font.Font(None, 36)
    easy = easyfont.render("Easy", True, White, None)
    easyrect = easy.get_rect(topleft = (230, 490))
    pygame.draw.rect(screen, (255, 102, 0), easyrect)
    screen.blit(easy, easyrect)


    # Game mode button(Medium)
    medfont = pygame.font.Font(None, 36)
    med = medfont.render("Medium", True, White, None)
    medrect = med.get_rect(topleft = (350, 490))
    pygame.draw.rect(screen, (255, 102, 0), medrect)
    screen.blit(med, medrect)


    # Game mode button(Hard)
    hardfont = pygame.font.Font(None, 36)
    hard = hardfont.render("Hard", True, White, None)
    hardrect = hard.get_rect(topleft = (500, 490))
    pygame.draw.rect(screen, (255, 102, 0), hardrect)
    screen.blit(hard, hardrect)

    return [easyrect, medrect, hardrect]

def main():
    mouse = pygame.mouse.get_pos()
    running = True
    screen.fill(White)
    start_screen()
    easyrect = start_screen()[0]
    medrect = start_screen()[1]
    hardrect = start_screen()[2]


    

    while running:
        #Main Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


            #Mouse Button event for Easy Medium and Hard Modes
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easyrect.collidepoint(event.pos):
                    sudoku_generator = SudokuGenerator()
                    sudoku_generator.Removed_cells = 30
                    sudoku_generator.fill_values()
                    sudoku_generator.remove_cells()
                    sudoku_board = sudoku_generator.get_board()

                    background()
                    font = pygame.font.Font(None, 36)
                    for i in range(Row_length):
                        for j in range(Row_length):
                            if sudoku_board[i][j] != 0:
                                text = font.render(str(sudoku_board[i][j]), True, Black)
                                text_rect = text.get_rect(center=(j * Cell_size + Cell_size // 2, i * Cell_size + Cell_size // 2))
                                screen.blit(text, text_rect)


                    pygame.display.flip()
                    pygame.time.Clock().tick(60)

                if medrect.collidepoint(event.pos):
                    sudoku_generator = SudokuGenerator()
                    sudoku_generator.Removed_cells = 40
                    sudoku_generator.fill_values()
                    sudoku_generator.remove_cells()
                    sudoku_board = sudoku_generator.get_board()

                    background()

                    font = pygame.font.Font(None, 36)
                    for i in range(Row_length):
                        for j in range(Row_length):
                            if sudoku_board[i][j] != 0:
                                text = font.render(str(sudoku_board[i][j]), True, Black)
                                text_rect = text.get_rect(center=(j * Cell_size + Cell_size // 2, i * Cell_size + Cell_size // 2))
                                screen.blit(text, text_rect)

                    pygame.display.flip()
                    pygame.time.Clock().tick(60)
                if hardrect.collidepoint(event.pos):
                    sudoku_generator = SudokuGenerator()
                    sudoku_generator.Removed_cells = 50
                    sudoku_generator.fill_values()
                    sudoku_generator.remove_cells()
                    sudoku_board = sudoku_generator.get_board()
                    
                    background()

                    font = pygame.font.Font(None, 36)
                    for i in range(Row_length):
                        for j in range(Row_length):
                            if sudoku_board[i][j] != 0:
                                text = font.render(str(sudoku_board[i][j]), True, Black)
                                text_rect = text.get_rect(center=(j * Cell_size + Cell_size // 2, i * Cell_size + Cell_size // 2))
                                screen.blit(text, text_rect)

                    pygame.display.flip()
                    pygame.time.Clock().tick(60)


        pygame.display.flip()
        
    pygame.quit


if __name__ == "__main__":
    main()