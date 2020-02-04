import pygame
import pygame_gui
from ui_utils import *

class MenuBar:
    def __init__ (self, screen, ui_manager):
        self.screen = screen
        self.ui_manager = ui_manager
        
        self.apps = []

        self.calc_rect()

    def draw (self):
        draw_rect(self.screen, self.rect, UI_BORDER)

        for app in self.apps:
            app.draw()

    def add_app (self, app):
        self.apps.append(app)

        for i in range(len(self.apps)):
            x = self.rect[0] + UI_PADDING + (i * (APP_DIMENSION + UI_PADDING)) - (APP_DIMENSION / 2)
            y = self.rect[1] + UI_PADDING
            
            self.apps[i].rect = (x, y, APP_DIMENSION, APP_DIMENSION)
        
        self.calc_rect()

    def calc_rect (self):
        screen_width, screen_height = self.screen.get_size()
        
        w = (len(self.apps) * (APP_DIMENSION + UI_PADDING)) + UI_PADDING
        h = MENUBAR_HEIGHT
        x = (screen_width / 2) - (w / 2)
        y = UI_SCREEN_PADDING

        self.rect = pygame.Rect(x, y, w, h)

class App:
    def __init__ (self, menubar, icon_path, name):
        self.menubar = menubar
        
        self.icon = pygame.transform.scale(pygame.image.load(icon_path), (APP_DIMENSION, APP_DIMENSION))
        self.name = name

        self.rect = pygame.Rect(0, 0, APP_DIMENSION, APP_DIMENSION)

    def draw (self):
        self.menubar.screen.blit(self.icon, (self.rect[0], self.rect[1]))
