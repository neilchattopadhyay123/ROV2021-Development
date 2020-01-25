import struct
import cv2

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

UI_COLOR = (240, 240, 240)
UI_PADDING = 10
UI_SPEED = 10

UI_DIMEN_FILL = -1
UI_HALIGN_LEFT = 0
UI_HALIGN_CENTER = 1
UI_HALIGN_RIGHT = 2
UI_VALIGN_TOP = 0
UI_VALIGN_CENTER = 1
UI_VALIGN_BOTTOM = 2

FPS = 60

# ------------------------------------------------------

# Socket info
HOST = '192.168.2.1' # The server ip
PORT = 6969 # The port to connect over
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

# qUoTeS
QUOTES = [
    '"Hear me out..."',
    '"Death! Death! DEATH!!"',
    '"Hello there!"'
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
