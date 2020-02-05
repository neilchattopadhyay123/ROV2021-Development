import pygame  
import os
from ui_utils import *
from ui_objects import *

# https://colorhunt.co/palette/114174

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

screen = pygame.display.set_mode(SCREEN_DIMENSION, pygame.RESIZABLE)
pygame.display.set_caption('LoggerheadROV Driver Station')

unispace_font = pygame.font.Font('unispace/unispace.ttf', 12)

menubar = MenuBar(screen, unispace_font)
menubar.add_app(App("Power On", menubar, 'icon_poweron.png'))
menubar.add_app(App("Power Off", menubar, 'icon_poweroff.png'))

is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

            menubar.resize()

        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[KEYBIND_DISABLE_MENUBAR[1]]:
                menubar.toggle_hidden()
        
    
    screen.fill(UI_COLOR_4)

    menubar.draw()

    pygame.display.update()

pygame.quit()
