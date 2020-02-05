import pygame
from ui_utils import *

class MenuBar:
    def __init__ (self, screen, font):
        self.screen = screen
        self.font = font

        w = UI_PADDING * 2
        h = MENUBAR_HEIGHT
        x = (self.screen.get_size()[0] / 2) - (w / 2)
        y = UI_SCREEN_PADDING
        self.rect = pygame.Rect(x, y, w, h)
        
        self.apps = []
        self.hidden = False

    def resize (self):
        w = (len(self.apps) * MENUBAR_APP_DIMENSION) + (LIMIT(len(self.apps) - 1, 0, len(self.apps)) * UI_PADDING) + (UI_PADDING * 2)
        h = MENUBAR_HEIGHT
        x = (self.screen.get_size()[0] / 2) - (w / 2)
        y = UI_SCREEN_PADDING

        self.rect = pygame.Rect(x, y, w, h)

        for i in range(len(self.apps)):
            x = self.rect[0] + UI_PADDING + (i * (MENUBAR_APP_DIMENSION + UI_PADDING))
            y = self.rect[1] + UI_PADDING

            self.apps[i].set_pos((x, y))
        
    def draw (self):
        if not self.hidden:
            draw_rect(self.screen, self.rect, UI_BORDER)
            draw_text(self.screen, self.font, 'Press [0] to toggle', (self.rect[0] + self.rect[2] + (UI_PADDING * 2), UI_SCREEN_PADDING), False)

            for app in self.apps:
                app.draw(self.screen)

    def toggle_hidden (self):
        self.hidden = not self.hidden
        
    def add_app (self, app):
        self.apps.append(app)

        self.resize()

class App:
    def __init__ (self, name, menubar, icon_path):
        self.name = name
        self.menubar = menubar

        self.pos = (0, 0)
        self.selected_pos = (0, 0)
        self.rect = pygame.Rect(self.pos, (MENUBAR_APP_DIMENSION, MENUBAR_APP_DIMENSION))
        
        self.icon = pygame.transform.scale(pygame.image.load(icon_path), (MENUBAR_APP_DIMENSION, MENUBAR_APP_DIMENSION))
        self.selected_icon = pygame.transform.scale(self.icon, (MENUBAR_APP_DIMENSION + UI_PADDING, MENUBAR_APP_DIMENSION + UI_PADDING))

    def draw (self, screen):
        if not self.menubar.hidden:
            draw_icon = self.icon
            draw_pos = self.pos
            
            if in_bounds(self.rect):
                draw_icon = self.selected_icon
                draw_pos = self.selected_pos
            
            screen.blit(draw_icon, draw_pos)

    def set_pos (self, pos):
        self.pos = pos
        self.selected_pos = (self.pos[0] - (UI_PADDING / 2.0), self.pos[1] - (UI_PADDING / 2.0))
        self.rect = pygame.Rect(self.pos, (MENUBAR_APP_DIMENSION, MENUBAR_APP_DIMENSION))
