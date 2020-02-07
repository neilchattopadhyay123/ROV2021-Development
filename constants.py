import struct
import cv2
import pygame

# Socket info
HOST = '192.168.2.1' # The server ip
PORT = 6900 # The port to connect over
TIMEOUT = 5 # The time without data being sent before the server disconnects from the client
PAYLOAD_SIZE = struct.calcsize(">L")
PACKET_SIZE = 2048 # The size of each packet of data being sent over
ENCODE_PARAM = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

# Command indexes
DATA_IDX_COMMAND = 0
DATA_IDX_VIDEO = 0

# Commands
COMMAND_QUIT = 'quit'

# Camera info
CAMERA_RES = (640, 480) # Resolution of the camera

# Print types
DEBUG = 'DEBUG'
ERROR = 'ERROR'
INFO = 'INFO'
SUCCESS = 'SUCCESS'

# UI 
SCREEN_DIMENSION = (960, 540)
UI_PADDING = 5
UI_SCREEN_PADDING = UI_PADDING * 2
UI_BORDER = 5
FPS = 60

UI_COLOR_1 = pygame.Color('#283149') # https://colorhunt.co/palette/114174
UI_COLOR_2 = pygame.Color('#404b69')
UI_COLOR_3 = pygame.Color('#f73859')
UI_COLOR_4 = pygame.Color('#dbedf3')

# UI
MENUBAR_APP_COUNT = 10
MENUBAR_HEIGHT = 70

APP_DIMENSION = MENUBAR_HEIGHT - (UI_PADDING * 2)
APP_SELECTED_DIMENSION = APP_DIMENSION + UI_PADDING
APP_MENUBAR_OFFSET = MENUBAR_HEIGHT + UI_SCREEN_PADDING

GAUGE_DIMENSION = 200

# Icons
ICON_UNKNOWN = 'gui/images/icon_unknown.png'
ICON_FOLDER = 'gui/images/icon_folder.png'
ICON_FOLDER_OPEN = 'gui/images/icon_folder_open.png'

# Keybinds
KEYBIND_MENUBAR_DISABLE = ('P', pygame.K_p)
KEYBIND_MENUBAR_SHORTCUTS = [('1', pygame.K_1), ('2', pygame.K_2), ('3', pygame.K_3), ('4', pygame.K_4), ('5', pygame.K_5), ('6', pygame.K_6), ('7', pygame.K_7), ('8', pygame.K_8), ('9', pygame.K_9), ('0', pygame.K_0)]

# qUoTeS
QUOTES = [
    '"Hear me out..."',
    '"Death! Death! DEATH!!"',
    '"Hello there!"',
    '"Gooey"',
    '"gENeraL KENoBoiauwdhaiwudn"',
    '"I search \'muscle beds\' and all I received were a bunch of shirtless men lying down."',
    '"You\'re coating me with your goop!"',
    '"We just nat together."',
    '"I love that kid."',
    '"TAKE MY CHIPS!!"',
    '"disableableable"'
]

def LIMIT (value, lower, upper):
    ''' Limit a value to an upper and lower bound '''
    
    if value < lower:
        value = lower
    
    if value > upper:
        value = upper

    return value

def ENC_VALUE (value):
    ''' Put emphasis on a value by printing brackets around it '''
    
    return '[' + str(value) + ']'

def PRINT (string, print_type=INFO):
    ''' Print something in a cool and helpful way '''
    
    print(ENC_VALUE(print_type) + '> ' + str(string))
