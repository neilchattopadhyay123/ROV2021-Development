import pygame

DEFAULT_DIMENSION = (800, 600)
UI_COLOR_1 = pygame.Color('#283149')
UI_COLOR_2 = pygame.Color('#404b69')
UI_COLOR_3 = pygame.Color('#f73859')
UI_COLOR_4 = pygame.Color('#dbedf3')
UI_SCREEN_PADDING = 10
UI_PADDING = 5
UI_BORDER = 5

MENUBAR_HEIGHT = 50
APP_DIMENSION = MENUBAR_HEIGHT - (UI_PADDING * 2)

def draw_rect(screen, rect, border, fill_color=UI_COLOR_2, border_color=UI_COLOR_1):
    border_rect = pygame.Rect((rect[0] - border, rect[1] - border), (rect[2] + (border * 2), rect[3] + (border * 2)))

    pygame.draw.rect(screen, border_color, border_rect)
    pygame.draw.rect(screen, fill_color, rect)
