import pygame

SCREEN_DIMENSION = (960, 540)

UI_COLOR_1 = pygame.Color('#283149')
UI_COLOR_2 = pygame.Color('#404b69')
UI_COLOR_3 = pygame.Color('#f73859')
UI_COLOR_4 = pygame.Color('#dbedf3')
UI_PADDING = 5
UI_SCREEN_PADDING = UI_PADDING * 2
UI_BORDER = 5

MENUBAR_APP_COUNT = 10
MENUBAR_HEIGHT = 70

APP_DIMENSION = MENUBAR_HEIGHT - (UI_PADDING * 2)
APP_SELECTED_DIMENSION = APP_DIMENSION + UI_PADDING

FOLDER_MENUBAR_OFFSET = MENUBAR_HEIGHT + (UI_SCREEN_PADDING * 2)
FOLDER_ICON_PATH = 'icon_folder.png'
FOLDER_OPEN_ICON_PATH = 'icon_folder_open.png'

KEYBIND_MENUBAR_DISABLE = ('P', pygame.K_p)
KEYBIND_MENUBAR_SHORTCUTS = [('1', pygame.K_1), ('2', pygame.K_2), ('3', pygame.K_3), ('4', pygame.K_4), ('5', pygame.K_5), ('6', pygame.K_6), ('7', pygame.K_7), ('8', pygame.K_8), ('9', pygame.K_9), ('0', pygame.K_0)]

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
