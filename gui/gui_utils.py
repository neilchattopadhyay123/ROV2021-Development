import pygame

from constants import UI_COLOR_1
from constants import UI_COLOR_2
from constants import UI_COLOR_3
from constants import UI_COLOR_4

def draw_rect(screen, rect, border, fill_color=UI_COLOR_2, border_color=UI_COLOR_1):
    border_rect = pygame.Rect((rect[0] - border, rect[1] - border), (rect[2] + (border * 2), rect[3] + (border * 2)))

    pygame.draw.rect(screen, border_color, border_rect)
    pygame.draw.rect(screen, fill_color, rect)

def in_bounds (rect):
    mouse_pos = pygame.mouse.get_pos()

    inside_x = mouse_pos[0] > rect[0] and mouse_pos[0] < rect[0] + rect[2]
    inside_y = mouse_pos[1] > rect[1] and mouse_pos[1] < rect[1] + rect[3]

    return inside_x and inside_y

def draw_text (screen, font, text, pos, center, color=UI_COLOR_1):
    text_surface = font.render(text, False, color)

    if center:
        center_pos = (pos[0] - (text_surface.get_size()[0] / 2), pos[1] - (text_surface.get_size()[1] / 2))
        screen.blit(text_surface, center_pos)
    else:
        screen.blit(text_surface, pos)
