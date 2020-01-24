import pygame

from constants import *

class Panel:
    def __init__ (self, display, w, h, halign, valign):
        self.display = display

        self.valign = valign
        self.halign = halign

        self.w = (display.width - (UI_PADDING * 2) if w == -1 else w)
        self.h = (display.height - (UI_PADDING * 2) if h == -1 else h)
        self._x = ((self.display.width * self.halign) / 2) - ((self.w * self.halign) / 2) + ((1 - self.halign) * UI_PADDING)
        self._y = ((self.display.height * self.valign) / 2) - ((self.h * self.valign) / 2) + ((1 - self.valign) * UI_PADDING)

        self.collapsed = False
        self._curr_offset = [0, 0]
        self._collapsed_offset = (((self.halign - 1) * (UI_PADDING + self.w)), ((self.valign - 1) * (UI_PADDING + self.h)))

    def toggle (self):
        self.collapsed = not self.collapsed

    def update (self):
        move_x = (self.halign - 1) * (1 if self.collapsed else -1) * UI_SPEED
        move_y = (self.valign - 1) * (1 if self.collapsed else -1) * UI_SPEED

        self._curr_offset[0] += move_x
        self._curr_offset[1] += move_y

        lower_x = ((2 - self.halign) * self._collapsed_offset[0]) / 2
        lower_y = ((2 - self.valign) * self._collapsed_offset[1]) / 2
        upper_x = (self.halign * self._collapsed_offset[0]) / 2
        upper_y = (self.valign * self._collapsed_offset[1]) / 2
        
        self._curr_offset[0] = LIMIT(self._curr_offset[0], lower_x, upper_x)
        self._curr_offset[1] = LIMIT(self._curr_offset[1], lower_y, upper_y)
        
    def draw (self):
        pygame.draw.rect(self.display.screen, UI_COLOR, pygame.Rect(self._x + self._curr_offset[0], self._y + self._curr_offset[1], self.w, self.h))
