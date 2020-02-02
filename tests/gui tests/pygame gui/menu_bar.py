import pygame
import pygame_gui
from ui_utils import *

class MenuBar:
    def __init__ (self, screen):
        self.screen = screen
        
        self.apps = []

        self.calc_rect()

    def draw (self):
        draw_rect(self.screen, self.rect, UI_BORDER)

        for i in range(len(self.apps)):
            x = self.rect[0] + UI_PADDING + (i * (APP_DIMENSION + UI_PADDING))
            y = self.rect[1] + UI_PADDING
            
            self.apps[i].draw((x, y))

    def add_app (self, app):
        self.apps.append(app)
        
        self.calc_rect()

    def calc_rect (self):
        screen_width, screen_height = self.screen.get_size()
        
        w = (len(self.apps) * (APP_DIMENSION + UI_PADDING)) + UI_PADDING
        h = MENUBAR_HEIGHT
        x = (screen_width / 2) - (w / 2)
        y = UI_SCREEN_PADDING

        self.rect = pygame.Rect(x, y, w, h)

class App:
    def __init__ (self, menubar, icon):
        self.menubar = menubar
        self.icon = pygame.transform.scale(icon, (APP_DIMENSION, APP_DIMENSION))

    def draw (self, pos):
        self.menubar.screen.blit(self.icon, pos)
