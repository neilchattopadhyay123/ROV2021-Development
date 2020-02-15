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
DATA_IDX_JOYSTICK = 1
DATA_IDX_VIDEO = 0

# Commands
COMMAND_QUIT = 'quit'

# Camera info
CAMERA_RES = (32*32, 16*32) # Resolution of the camera
CAMERA_MODE = 5 # Camera aspect ratio mode
CAMERA_FPS = 30
CAMERA_SHUTTER_SPEED = 1000
CAMERA_BRIGHTNESS = 65
CAMERA_AWB_MODE = 'incandescent'

# Print types
DEBUG = 'DEBUG'
ERROR = 'ERROR'
INFO = 'INFO'
SUCCESS = 'SUCCESS'

# UI 
SCREEN_DIMENSION = (640, 480)
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
MENUBAR_HEIGHT = 50

APP_DIMENSION = MENUBAR_HEIGHT - (UI_PADDING * 2)
APP_SELECTED_DIMENSION = APP_DIMENSION + UI_PADDING
APP_MENUBAR_OFFSET = MENUBAR_HEIGHT + UI_SCREEN_PADDING

GAUGE_DIMENSION = 150

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
    '"I searched \'muscle beds\' and all I received were a bunch of shirtless men lying down."',
    '"You\'re coating me with your goop!"',
    '"We just nat together."',
    '"I love that kid."',
    '"TAKE MY CHIPS!!"',
    '"disableableable"',
    '"I did a scientific thingamajig."',
    '"Budget Boy!"',
    '"Did you ever hear of the tragedy of Darth Plagueis the Wise? I thought not. It\'s not a story the Jedi would tell you."',
    '"Darth Plagueis was a dark lord of the Sith, so powerful and so wise, he could use the Force to influence the Midiclorians to create life."',
    '"He had such a knowledge of the Dark Side, that he could even keep the ones he cared about from dying."',
    '"The Dark Side of the Force is a pathway to many abilites some consider to be uNNATURAL."',
    '"He became so powerful, the only thing that he was afraid of was losing his power, which eventually of course he did."',
    '"Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself."'
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
