import pygame
from ui_utils import *

class MenuBar:
    def __init__ (self, screen, font, offset=0):
        self.screen = screen
        self.font = font
        
        self.rect = pygame.Rect(0, 0, MENUBAR_HEIGHT, MENUBAR_HEIGHT)
        
        self.apps = []
        self.is_hidden = False
        self.selected_app = None

        self.resize()

    def resize (self):
        w = (len(self.apps) * APP_DIMENSION) + (LIMIT(len(self.apps) - 1, 0, len(self.apps)) * UI_PADDING) + (UI_PADDING * 2)
        h = MENUBAR_HEIGHT
        x = (self.screen.get_size()[0] / 2) - (w / 2)
        y = UI_SCREEN_PADDING

        self.rect = pygame.Rect(x, y, w, h)

        for i in range(len(self.apps)):
            x = self.rect[0] + UI_PADDING + (i * (APP_DIMENSION + UI_PADDING))
            y = self.rect[1] + UI_PADDING

            self.apps[i].set_pos((x, y))
        
    def draw (self):
        if not self.is_hidden:
            draw_rect(self.screen, self.rect, UI_BORDER)

            self.selected_app = None
            for i in range(len(self.apps)):
                self.apps[i].draw(self.screen, i)

                if self.apps[i].is_selected:
                    self.selected_app = self.apps[i]

            if self.selected_app != None:
                draw_text(self.screen, self.font, self.selected_app.name, (self.rect[0] + self.rect[2] + (UI_PADDING * 2), UI_SCREEN_PADDING), False, color=UI_COLOR_3)

    def toggle_hidden (self):
        self.is_hidden = not self.is_hidden
        
    def add_app (self, app):
        if len(self.apps) < MENUBAR_APP_COUNT:
            self.apps.append(app)

            self.resize()
        else:
            print('Cannot add another app! [Limit reached]')

class App:
    def __init__ (self, name, menubar, icon_path):
        self.name = name
        self.menubar = menubar

        self.idle_rect = pygame.Rect(0, 0, APP_DIMENSION, APP_DIMENSION)
        self.selected_rect = pygame.Rect(0, 0, APP_DIMENSION + UI_PADDING, APP_DIMENSION + UI_PADDING)
        
        self.icon = pygame.transform.scale(pygame.image.load(icon_path), (self.idle_rect[2], self.idle_rect[3]))
        self.selected_icon = pygame.transform.scale(self.icon, (self.selected_rect[2], self.selected_rect[3]))

        self.rect = self.idle_rect
        self.is_selected = False

    def draw (self, screen, index):
        self.is_selected = in_bounds(self.rect)
        
        draw_icon = self.selected_icon if self.is_selected else self.icon
        self.rect = self.selected_rect if self.is_selected else self.idle_rect
        text_color = UI_COLOR_3 if self.is_selected else UI_COLOR_1
        text_pos = (self.idle_rect.centerx, self.idle_rect.bottom + (UI_PADDING * 4))
        
        screen.blit(draw_icon, self.rect)
        draw_text(self.menubar.screen, self.menubar.font, KEYBIND_MENUBAR_SHORTCUTS[index][0], text_pos, True, color=text_color)

    def set_pos (self, pos):
        self.idle_rect = pygame.Rect(pos, (APP_DIMENSION, APP_DIMENSION))
        self.selected_rect = pygame.Rect(pos[0] - (UI_PADDING / 2.0), pos[1] - (UI_PADDING / 2.0), APP_SELECTED_DIMENSION, APP_SELECTED_DIMENSION)
        
        self.rect = self.idle_rect

class Folder (App):
    def __init__ (self, name, menubar):
        super().__init__(name, menubar, FOLDER_ICON_PATH)
        
        self.folder_menubar = MenuBar(self.menubar.screen, self.menubar.font, FOLDER_MENUBAR_OFFSET)

        self.is_open = False

    def draw (self, screen, index):
        if self.is_open:
            self.folder_menubar.draw()

        super().draw(screen, index)

    def add_app (self, app):
        self.folder_menubar.add_app(app)
