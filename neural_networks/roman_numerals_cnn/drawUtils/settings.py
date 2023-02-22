import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60

WIDTH, HEIGHT = 600, 700

ROWS = COLS = 32

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = WHITE

def get_font(size):
    return pygame.font.SysFont("Comicsans", size)