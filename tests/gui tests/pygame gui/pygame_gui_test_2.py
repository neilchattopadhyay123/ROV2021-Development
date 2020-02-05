import pygame
import pygame_gui   
import os
from ui_utils import *
from menu_bar import *

# https://colorhunt.co/palette/114174

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

display_info = pygame.display.Info()
screen_width = display_info.current_w - SCREEN_W_ADJ
screen_height = display_info.current_h - SCREEN_H_ADJ
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('LoggerheadROV Driver Station')

ui_manager = pygame_gui.UIManager(screen.get_size(), UI_MAIN_THEME_PATH)

menubar = MenuBar(screen, ui_manager)
menubar.add_app(App("Power On", menubar, 'icon_poweron.png'))
menubar.add_app(App("Power Off", menubar, 'icon_poweroff.png'))

clock = pygame.time.Clock()
is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            
        ui_manager.process_events(event)

    time_delta = clock.tick(60) / 1000.0
    ui_manager.update(time_delta)
    
    screen.fill(UI_COLOR_4)

    menubar.draw()
    ui_manager.draw_ui(screen)
    menubar.draw_apps()

    pygame.display.update()

pygame.quit()
