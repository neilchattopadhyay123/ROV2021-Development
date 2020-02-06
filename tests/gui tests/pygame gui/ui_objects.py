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
        self.is_open_folder = False # If there is an open folder on the menubar
        self.selected_app = '' # If an app on the menubar is currently selected

        self.resize() # Calculate the size of the menubar

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

            try:
                self.apps[i].resize()
            except:
                pass

    def update (self, mouse_data):
        # Update all the apps on the menubar
        if not self.is_hidden:
            for app in self.apps:
                app.update(mouse_data)
        
    def draw (self):
        # If the menubar is not hidden, draw the menubar and the apps on it
        if not self.is_hidden:
            draw_rect(self.screen, self.rect, UI_BORDER) # Draw menubar

            self.is_open_folder = False
            # Check if any folders are open
            for app in self.apps:
                try:
                    if app.is_open:
                        self.is_open_folder = True
                except:
                    pass
            
            # Draw apps and get a selected app if one is selected
            self.selected_app = ''
            for i in range(len(self.apps)):
                self.apps[i].draw(self.screen)

                if self.apps[i].is_selected:
                    self.selected_app = self.apps[i].name

                if not self.is_open_folder:
                    text_color = UI_COLOR_3 if self.apps[i].is_selected else UI_COLOR_1
                    text_pos = (self.apps[i].idle_rect.centerx, self.apps[i].idle_rect.bottom + (UI_PADDING * 4))
                    
                    draw_text(self.screen, self.font, KEYBIND_MENUBAR_SHORTCUTS[i][0], text_pos, True, color=text_color)

            # Draw the name of the selected app
            if self.selected_app != '':
                draw_text(self.screen, self.font, self.selected_app, (self.rect[0] + self.rect[2] + (UI_PADDING * 2), UI_SCREEN_PADDING + self.vertical_offset), False, color=UI_COLOR_3)

    def toggle_hidden (self):
        self.is_hidden = not self.is_hidden
        
    def add_app (self, app):
        if len(self.apps) < MENUBAR_APP_COUNT:
            self.apps.append(app)

            self.resize()
        else:
            print('Cannot add another app! [Limit reached]')

class App:
    def __init__ (self, name, menubar, icon_path, function=None):
        self.name = name # Name of app
        self.menubar = menubar # The parent menubar

        self.idle_rect = pygame.Rect(0, 0, APP_DIMENSION, APP_DIMENSION)
        self.selected_rect = pygame.Rect(0, 0, APP_DIMENSION + UI_PADDING, APP_DIMENSION + UI_PADDING)
        
        self.icon = pygame.transform.scale(pygame.image.load(icon_path), (self.idle_rect[2], self.idle_rect[3]))
        self.selected_icon = pygame.transform.scale(self.icon, (self.selected_rect[2], self.selected_rect[3]))

        self.rect = self.idle_rect
        self.is_selected = False

        self.function = function

    def update (self, mouse_data):
        if mouse_data[0] and self.is_selected:
            if self.function != None:
                self.function()

            self.is_selected = False
        elif not mouse_data[0]:
            self.is_selected = in_bounds(self.rect)

    def draw (self, screen):
        draw_icon = self.selected_icon if self.is_selected else self.icon
        self.rect = self.selected_rect if self.is_selected else self.idle_rect
        
        screen.blit(draw_icon, self.rect)

    def set_icon (self, icon):
        self.icon = pygame.transform.scale(icon, (self.idle_rect[2], self.idle_rect[3]))
        self.selected_icon = pygame.transform.scale(self.icon, (self.selected_rect[2], self.selected_rect[3]))

    def set_pos (self, pos):
        self.idle_rect = pygame.Rect(pos, (APP_DIMENSION, APP_DIMENSION))
        self.selected_rect = pygame.Rect(pos[0] - (UI_PADDING / 2.0), pos[1] - (UI_PADDING / 2.0), APP_SELECTED_DIMENSION, APP_SELECTED_DIMENSION)
        
        self.rect = self.idle_rect

class Folder (App):
    def __init__ (self, name, menubar, layer):
        self.app = super()
        
        self.is_open = False
                
        self.folder_menubar = MenuBar(menubar.screen, menubar.font, layer * FOLDER_MENUBAR_OFFSET)
        
        self.app.__init__(name, menubar, FOLDER_ICON_PATH, self.toggle_is_open)

    def update (self, mouse_data):
        self.app.update(mouse_data)
        self.folder_menubar.update(mouse_data)

    def draw (self, screen):
        if self.is_open:
            self.folder_menubar.draw()

        self.app.draw(screen)

    def resize (self):
        self.folder_menubar.resize()

    def toggle_is_open (self):
        self.is_open = not self.is_open

        self.app.set_icon(pygame.image.load(FOLDER_OPEN_ICON_PATH) if self.is_open else pygame.image.load(FOLDER_ICON_PATH))

    def add_app (self, app):
        self.folder_menubar.add_app(app)
