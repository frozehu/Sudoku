import pygame
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.cell_size = 81
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value
        #pass???

    def draw(self):
        x = self.col * self.cell_size
        y = self.row * self.cell_size
        rect = pygame.Rect(x +15, y+15, 82, 82)
        # if user selects a cell, outline in red
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), rect, 3)
        else:
            return None
        #draw cell and value inside it
        if self.value != 0:
            text = self.font.render(str(self.value), True, (0, 0, 0))
            text_rect = text.get_rect(center = (x + self.cell_size/2, y + self.cell_size))
            self.screen.blit(text, text_rect)
        else:
            return None