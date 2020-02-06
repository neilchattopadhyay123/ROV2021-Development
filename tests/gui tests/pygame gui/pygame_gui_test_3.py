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

server_folder = App("Server Functions", menubar, is_folder=True)
server_folder.add_app(App("Power Off", server_folder.sub_app_menubar, 'icon_poweroff.png'))
menubar.add_app(server_folder)

sub_server_folder = App("ANOTHER FOLDER???", server_folder.sub_app_menubar, is_folder=True)
sub_server_folder.add_app(App("Power On", sub_server_folder.sub_app_menubar, 'icon_poweron.png'))
server_folder.add_app(sub_server_folder)

is_running = True

while is_running:
    mouse_data = (False, False, False)
    key_data = [False] * len(pygame.key.get_pressed())
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

            menubar.resize()

        if event.type == pygame.KEYDOWN:
            key_data = pygame.key.get_pressed()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_data = pygame.mouse.get_pressed()

    menubar.update(mouse_data, key_data)

    screen.fill(UI_COLOR_4)

    menubar.draw()
    
    draw_text(screen, unispace_font, str(round(clock.get_fps(), 3)) + ' FPS', (UI_SCREEN_PADDING, UI_SCREEN_PADDING), False)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
