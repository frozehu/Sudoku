import pygame, sys
from board import *
from SudokuGenerator import *

pygame.init()
#made a bit bigger, original board was getting cut off
screen = pygame.display.set_mode((780, 780))
pygame.display.set_caption("Sudoku")


#def starting_screen():
    # put starting screen things in here? Ran into accessing button collide points outside of definition
    # Ref lines 67, 70, 73

def game():
    mouse = pygame.mouse.get_pos()
    running = True
    screen.fill(White)
    while running:


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
        

        #Main Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if easyrect.collidepoint(event.pos):
                    # Insert change screen and filling of sudoku board at this difficulty
                    running = False
                if medrect.collidepoint(event.pos):
                    # Insert change screen and filling of sudoku board at this difficulty
                    running = False
                if hardrect.collidepoint(event.pos):
                    # Insert change screen and filling of sudoku board at this difficulty
                    running = False

        pygame.display.flip()
        
    pygame.quit


if __name__ == "__main__":
    game()