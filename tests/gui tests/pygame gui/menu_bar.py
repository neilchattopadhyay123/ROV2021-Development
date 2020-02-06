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
        self.hidden = False
        
    def draw (self):
        if not self.hidden:
            draw_rect(self.screen, self.rect, UI_BORDER)

    def draw_apps (self):
        for app in self.apps:
            app.draw(self.screen)

    def toggle_hidden (self):
        self.hidden = not self.hidden

        for app in self.apps:
            app.button.set_position((-500, -500) if self.hidden else app.pos)
        
    def add_app (self, app):
        self.apps.append(app)

class App:
    def __init__ (self, name, menubar, icon_path):
        self.name = name
        self.menubar = menubar

        self.pos = (self.menubar.rect[0] + UI_PADDING + ((MENUBAR_APP_DIMENSION + UI_PADDING) * len(self.menubar.apps)), self.menubar.rect[1] + UI_PADDING)
        self.selected_pos = (self.pos[0] - (UI_PADDING / 2.0), self.pos[1] - (UI_PADDING / 2.0))
        self.rect = pygame.Rect(self.pos, (MENUBAR_APP_DIMENSION, MENUBAR_APP_DIMENSION))
        
        self.icon = pygame.transform.scale(pygame.image.load(icon_path), (MENUBAR_APP_DIMENSION, MENUBAR_APP_DIMENSION))
        self.selected_icon = pygame.transform.scale(self.icon, (MENUBAR_APP_DIMENSION + UI_PADDING, MENUBAR_APP_DIMENSION + UI_PADDING))

        self.button = pygame_gui.elements.UIButton(self.rect, '', manager=self.menubar.ui_manager, tool_tip_text=self.name)

    def draw (self, screen):
        if not self.menubar.hidden:
            draw_icon = self.icon
            draw_pos = self.pos
            
            if in_bounds(self.rect):
                draw_icon = self.selected_icon
                draw_pos = self.selected_pos
            
            screen.blit(draw_icon, draw_pos)
