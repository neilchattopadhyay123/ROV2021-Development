import pygame

from constants import *

class Display:
    def __init__ (self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        self.panels = []

    def add_panel (self, panel):
        self.panels += [panel];
    
    def draw_ui (self):
        self.screen.fill((0, 0, 0))
        
        for panel in self.panels:
            panel.update()
            panel.draw()

        pygame.display.flip()
