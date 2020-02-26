import pygame

from gui_utils import *
from constants import *

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
        if not self.is_hidden: # If the menubar is not hidden, update apps
            if key_data[KEYBIND_MENUBAR_DISABLE[1]]: # Toggles between hidden and shown
                menubar.toggle_hidden()
            
            for i in range(len(self.apps)): # Updates apps on menubar
                self.apps[i].update(mouse_data, key_data)

                if key_data[KEYBIND_MENUBAR_SHORTCUTS[i][1]]: # Checks if app shortcut was pressed
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

    def toggle_hidden (self): # Switches is_hidden boolean variable when called
        self.is_hidden = not self.is_hidden
        
    def add_app (self, app): # Appends new app to menubar and auto resizes
        if len(self.apps) < MENUBAR_APP_COUNT:
            self.apps.append(app)

            self.resize()
            
        else:
            PRINT('Cannot add app ' + ENC_VALUE(app.name) + ' to MenuBar! (len=' + str(MENUBAR_APP_COUNT), ERROR)
