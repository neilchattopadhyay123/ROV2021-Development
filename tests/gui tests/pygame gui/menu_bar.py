import pygame
import pygame_gui
from ui_utils import *

class MenuBar:
    def __init__ (self, screen):
        self.screen = screen

    def draw (self):
        w, h = self.screen.get_size()
        bar = pygame.Rect((w / 4, 10), (w / 2, 50))

        draw_rect(self.screen, bar, 5)
