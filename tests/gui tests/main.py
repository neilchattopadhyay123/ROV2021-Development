import pygame

from panel import *
from constants import *
from display import *

pygame.init()

def main ():
    running = True

    display = Display()
    display.add_panel(Panel(display, SCREEN_WIDTH / 4, UI_DIMEN_FILL, UI_HALIGN_RIGHT, UI_VALIGN_CENTER))
    display.add_panel(Panel(display, SCREEN_WIDTH / 4, UI_DIMEN_FILL, UI_HALIGN_LEFT, UI_VALIGN_CENTER))

    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    display.panels[0].toggle()
                elif event.key == pygame.K_1:
                    display.panels[1].toggle()

        display.draw_ui()

        clock.tick(FPS)

if __name__ == '__main__':
    main()

    pygame.quit()
