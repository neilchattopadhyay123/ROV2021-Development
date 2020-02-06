import pygame
from ui_utils import *

class MenuBar:
    def __init__ (self, screen, font, vertical_offset=0):
        self.screen = screen # The pygame screen
        self.font = font # The pygame font
        
        self.rect = pygame.Rect(0, 0, MENUBAR_HEIGHT, MENUBAR_HEIGHT) # The actual menubar rectangle
        self.vertical_offset = vertical_offset

        self.apps = [] # List of all apps on the menubar
        
        self.is_hidden = False # If the menubar is hidden or not
        self.has_open_app = False # If there is an open folder on the menubar

        self.resize() # Calculate the size of the menubar

    def update (self, mouse_data, key_data):
        # Update all the apps on the menubar
        if not self.is_hidden:
            if key_data[KEYBIND_MENUBAR_DISABLE[1]]:
                menubar.toggle_hidden()
            
            for i in range(len(self.apps)):
                self.apps[i].update(mouse_data, key_data)

                if key_data[KEYBIND_MENUBAR_SHORTCUTS[i][1]]:
                    self.apps[i].run()
        
    def draw (self):
        # If the menubar is not hidden, draw the menubar and the apps on it
        if not self.is_hidden:
            draw_rect(self.screen, self.rect, UI_BORDER) # Draw menubar

            self.has_open_app = False
            # Check if any folders are open
            for app in self.apps:
                try:
                    if app.is_open:
                        self.has_open_app = True
                except:
                    pass
            
            # Draw apps and get a selected app if one is selected
            for i in range(len(self.apps)):
                self.apps[i].draw(self.screen)

                if self.apps[i].is_selected:
                    text_pos = (self.rect[0] + self.rect[2] + (UI_PADDING * 2), self.rect[1])
                    
                    draw_text(self.screen, self.font, self.apps[i].name, text_pos, False, color=UI_COLOR_3)

                if not self.has_open_app:
                    text_color = UI_COLOR_3 if self.apps[i].is_selected else UI_COLOR_1
                    text_pos = (self.apps[i].idle_rect.centerx, self.apps[i].idle_rect.bottom + (UI_PADDING * 4))
                    
                    draw_text(self.screen, self.font, KEYBIND_MENUBAR_SHORTCUTS[i][0], text_pos, True, color=text_color)

    def resize (self):
        # Calculate the dimensions and position of the menuber
        w = (len(self.apps) * APP_DIMENSION) + (LIMIT(len(self.apps) - 1, 0, len(self.apps)) * UI_PADDING) + (UI_PADDING * 2)
        h = MENUBAR_HEIGHT
        x = (self.screen.get_size()[0] / 2) - (w / 2)
        y = UI_SCREEN_PADDING + self.vertical_offset

        self.rect = pygame.Rect(x, y, w, h)

        # Calculate the position of the apps on the menubar
        for i in range(len(self.apps)):
            x = self.rect[0] + UI_PADDING + (i * (APP_DIMENSION + UI_PADDING))
            y = self.rect[1] + UI_PADDING

            self.apps[i].set_pos((x, y))

    def toggle_hidden (self):
        self.is_hidden = not self.is_hidden
        
    def add_app (self, app):
        if len(self.apps) < MENUBAR_APP_COUNT:
            self.apps.append(app)

            self.resize()
        else:
            print('Cannot add another app! [Limit reached]')

class App:
    def __init__ (self, name, menubar, idle_icon_path='icon_unknown.png', open_icon_path=None, function=None, is_folder=False):
        self.name = name # Name of app
        self.menubar = menubar # The parent menubar
        self.function = function

        if is_folder:
            self.function = self.toggle_is_open
            
            idle_icon_path = 'icon_folder.png'
            open_icon_path = 'icon_folder_open.png'

        self.idle_rect = pygame.Rect(0, 0, APP_DIMENSION, APP_DIMENSION)
        self.selected_rect = pygame.Rect(0, 0, APP_DIMENSION + UI_PADDING, APP_DIMENSION + UI_PADDING)
        self.rect = self.idle_rect
        
        self.idle_icon = pygame.transform.scale(pygame.image.load(idle_icon_path), self.idle_rect.size)
        self.selected_icon = pygame.transform.scale(self.idle_icon, self.selected_rect.size)
        self.open_icon = pygame.transform.scale(pygame.image.load(idle_icon_path if open_icon_path == None else open_icon_path), self.idle_rect.size)
        self.open_selected_icon = pygame.transform.scale(self.open_icon, self.selected_rect.size)
        self.icon = self.idle_icon

        self.sub_apps = []
        self.sub_app_menubar = MenuBar(self.menubar.screen, self.menubar.font, self.menubar.rect[1] + FOLDER_MENUBAR_OFFSET)
        
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
        
