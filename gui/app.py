import pygame

from gui_utils import *
from constants import *
from menubar import MenuBar

class App:
    def __init__ (self, name, menubar, idle_icon_path=ICON_UNKNOWN, open_icon_path=None, function=None, is_folder=False):
        self.name = name # Name of app
        self.menubar = menubar # The parent menubar
        self.function = function

        if is_folder:
            self.function = self.toggle_is_open
            
            idle_icon_path = ICON_FOLDER
            open_icon_path = ICON_FOLDER_OPEN

        self.idle_rect = pygame.Rect(0, 0, APP_DIMENSION, APP_DIMENSION)
        self.selected_rect = pygame.Rect(0, 0, APP_DIMENSION + UI_PADDING, APP_DIMENSION + UI_PADDING)
        self.rect = self.idle_rect
        
        self.idle_icon = pygame.transform.scale(pygame.image.load(idle_icon_path), self.idle_rect.size)
        self.selected_icon = pygame.transform.scale(self.idle_icon, self.selected_rect.size)
        self.open_icon = pygame.transform.scale(pygame.image.load(idle_icon_path if open_icon_path == None else open_icon_path), self.idle_rect.size)
        self.open_selected_icon = pygame.transform.scale(self.open_icon, self.selected_rect.size)
        self.icon = self.idle_icon

        self.sub_apps = []
        self.sub_app_menubar = MenuBar(self.menubar.screen, self.menubar.font, self.menubar.rect[1] + APP_MENUBAR_OFFSET)
        
        self.is_selected = False
        self.is_open = False

        self.resize()

    def update (self, mouse_data, key_data):
        if mouse_data[0] and self.is_selected:
            self.run()

            self.is_selected = False
        else:
            self.is_selected = in_bounds(self.rect)

        
        self.icon = (self.open_selected_icon if self.is_open else self.selected_icon) if self.is_selected else (self.open_icon if self.is_open else self.idle_icon)
        self.rect = self.selected_rect if self.is_selected else self.idle_rect

        if self.is_open:
            self.sub_app_menubar.update(mouse_data, key_data)

            for sub_app in self.sub_apps:
                sub_app.update(mouse_data, key_data)

    def draw (self, screen):
        screen.blit(self.icon, self.rect)

        if self.is_open:
            self.sub_app_menubar.draw()
            
            for sub_app in self.sub_apps:
                sub_app.draw(screen)

    def set_pos (self, pos):
        self.idle_rect = pygame.Rect(pos, (APP_DIMENSION, APP_DIMENSION))
        self.selected_rect = pygame.Rect(pos[0] - (UI_PADDING / 2.0), pos[1] - (UI_PADDING / 2.0), APP_SELECTED_DIMENSION, APP_SELECTED_DIMENSION)
        self.rect = self.idle_rect

        self.resize()

    def run (self):
        if self.function != None:
            self.function()

            self.is_selected = False

    def resize (self):
        self.sub_app_menubar.resize()

    def toggle_is_open (self):
        self.is_open = not self.is_open

    def add_app (self, app):
        self.sub_app_menubar.add_app(app)
