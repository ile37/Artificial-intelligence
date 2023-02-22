import drawUtils
import pygame
from drawUtils import *
import numpy as np

from Network_model import *


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draw a roman numeral")

def init_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)

    return grid

def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

def draw(win, grid, buttons, label):
    win.fill(BG_COLOR)
    draw_grid(win, grid)

    for button in buttons:
        button.draw(win)
    
    WIN.blit(label, (150, -10 + HEIGHT-TOOLBAR_HEIGHT/2))

    pygame.display.update()

def get_row_col_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError

    return row, col



def main():

    run = True
    clock = pygame.time.Clock()
    grid = init_grid(ROWS, COLS, BG_COLOR)
    drawing_color = BLACK

    font = pygame.font.Font(None, 36)
    text = "Current gess: ??"
    label = font.render(text, True, (0,0,0))
    
    # neural network setup
    model = Net()
    model.load_state_dict(torch.load('save\model_params.pth'))

    buttons = [
        Button(10, HEIGHT-TOOLBAR_HEIGHT/2 -25, 50, 50, WHITE, "Clear", BLACK),
        Button(70, HEIGHT-TOOLBAR_HEIGHT/2 -25, 50, 50, WHITE, "Gess", BLACK)
    ]

    while run:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()

                try:
                    row, col = get_row_col_from_pos(pos)
                    grid[row][col] = drawing_color
                except IndexError:
                    for button in buttons:
                        if not button.clicked(pos):
                            continue
                        
                        if button.text == "Clear":
                            grid = init_grid(ROWS, COLS, BG_COLOR)
                            drawing_color = BLACK

                        if button.text == "Gess":

                            out = model(torch.tensor(grid)[:,:,0].resize(1,1,32,32).float())
                            index = torch.argmax(out)
                            text = f"Current gess: {index + 1}"
                            label = font.render(text, True, (0,0,0))


        draw(WIN, grid, buttons, label)
    pygame.quit()

main()

