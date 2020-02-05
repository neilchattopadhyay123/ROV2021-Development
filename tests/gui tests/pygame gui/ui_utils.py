import pygame

SCREEN_H_ADJ = 215
SCREEN_W_ADJ = 215
SCREEN_DIMENSION = (960, 540)

UI_MAIN_THEME_PATH = 'loggerhead-theme.json'
UI_COLOR_1 = pygame.Color('#283149')
UI_COLOR_2 = pygame.Color('#404b69')
UI_COLOR_3 = pygame.Color('#f73859')
UI_COLOR_4 = pygame.Color('#dbedf3')
UI_PADDING = 5
UI_SCREEN_PADDING = UI_PADDING * 2
UI_BORDER = 5

MENUBAR_APP_COUNT = 7
MENUBAR_HEIGHT = 70
MENUBAR_APP_DIMENSION = MENUBAR_HEIGHT - (UI_PADDING * 2)
MENUBAR_WIDTH = UI_PADDING + (MENUBAR_APP_DIMENSION + UI_PADDING) * MENUBAR_APP_COUNT

KEYBIND_DISABLE_MENUBAR = ('0', pygame.K_0)

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

def LIMIT (value, lower, upper):
    ''' Limit a value to an upper and lower bound '''
    
    if value < lower:
        value = lower
    
    if value > upper:
        value = upper

    return value
