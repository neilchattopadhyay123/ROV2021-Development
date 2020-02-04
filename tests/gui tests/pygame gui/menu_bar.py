import pygame
import pygame_gui
from ui_utils import *

class MenuBar:
    def __init__ (self, screen, ui_manager):
        self.screen = screen
        self.ui_manager = ui_manager

        x = (self.screen.get_size()[0] / 2) - (MENUBAR_WIDTH / 2)
        y = UI_PADDING
        w = MENUBAR_WIDTH
        h = MENUBAR_HEIGHT

        self.rect = pygame.Rect(x, y, w, h)
        self.bar = pygame_gui.elements.UITextBox('', self.rect, self.ui_manager)
        
        self.apps = []

    def update (self, time_delta):
        for app in self.apps:
            app.update(time_delta)

    def add_app (self, app):
        self.apps.append(app)

class App:
    def __init__ (self, menubar, icon_path, name):
        self.menubar = menubar
        self.name = name

        x = self.menubar.rect[0] + UI_PADDING + ((APP_DIMENSION + UI_PADDING) * len(self.menubar.apps))
        y = self.menubar.rect[1] + UI_PADDING
        self.rect = pygame.Rect(x, y, APP_DIMENSION, APP_DIMENSION)
        self.icon = pygame.transform.scale(pygame.image.load(icon_path), (self.rect[2], self.rect[3]))

        self.button = pygame_gui.elements.UIButton(self.rect, '', self.menubar.ui_manager, tool_tip_text=self.name)

    def update (self, time_delta):
        self.button.update(time_delta)
