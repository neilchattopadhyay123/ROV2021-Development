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
clock = pygame.time.Clock()

menubar = MenuBar(screen, unispace_font)
menubar.add_app(App("Power On", menubar, 'icon_poweron.png'))
menubar.add_app(App("Power Off", menubar, 'icon_poweroff.png'))
menubar.add_app(Folder("Server Functions", menubar))

is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

            menubar.resize()

        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[KEYBIND_MENUBAR_DISABLE[1]]:
                menubar.toggle_hidden()

    screen.fill(UI_COLOR_4)

    menubar.draw()
    
    draw_text(screen, unispace_font, str(round(clock.get_fps(), 3)) + ' FPS', (UI_SCREEN_PADDING, UI_SCREEN_PADDING), False)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
