import pygame
import pygame_gui
from ui_utils import *

class MenuBar:
    def __init__ (self, screen, ui_manager):
        self.screen = screen
        self.ui_manager = ui_manager

        x = (self.screen.get_size()[0] / 2) - (MENUBAR_WIDTH / 2)
        y = UI_SCREEN_PADDING
        w = MENUBAR_WIDTH
        h = MENUBAR_HEIGHT
        self.rect = pygame.Rect(x, y, w, h)
        
        self.apps = []
        
    def draw (self):
        draw_rect(self.screen, self.rect, UI_BORDER)

    def draw_apps (self):
        for app in self.apps:
            app.draw(self.screen)
        
    def add_app (self, app):
        self.apps.append(app)

class App:
    def __init__ (self, name, menubar, icon_path):
        self.name = name
        self.menubar = menubar

        x = self.menubar.rect[0] + UI_PADDING + ((APP_DIMENSION + UI_PADDING) * len(self.menubar.apps))
        y = self.menubar.rect[1] + UI_PADDING
        self.rect = pygame.Rect(x, y, APP_DIMENSION, APP_DIMENSION)
        self.icon = pygame.transform.scale(pygame.image.load(icon_path), (self.rect[2], self.rect[3]))

        self.button = pygame_gui.elements.UIButton(self.rect, '', manager=self.menubar.ui_manager, tool_tip_text=self.name)

    def draw (self, screen):
        screen.blit(self.icon, self.rect)
