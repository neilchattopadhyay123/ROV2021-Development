import pygame
import pygame_gui
from ui_utils import *
from menu_bar import MenuBar

# https://colorhunt.co/palette/114174

pygame.init()

pygame.display.set_caption('LoggerheadROV Driver Station')
screen = pygame.display.set_mode(DEF_DIMENSION, flags=pygame.RESIZABLE)

manager = pygame_gui.UIManager(DEF_DIMENSION, 'loggerhead-theme.json')

menu_bar = MenuBar(screen)

clock = pygame.time.Clock()
is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            manager = pygame_gui.UIManager((event.w, event.h), 'loggerhead-theme.json')

        manager.process_events(event)
        
    screen.fill(UI_COLOR_4)

    menu_bar.draw()
    manager.draw_ui(screen)

    pygame.display.update()
    manager.update(clock.tick(60) / 1000.0)

pygame.quit()
