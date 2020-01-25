import struct

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

HOST = '192.168.2.1'
PORT = 6969

DATA_IDX_COMMAND = 0
DATA_IDX_VIDEO = 0

COMMAND_QUIT = 'quit'

CAMERA_RES = (640, 480)

TIMEOUT = 5 # seconds
PAYLOAD_SIZE = struct.calcsize(">L")
PACKET_SIZE = 2048
ENCODE_PARAM = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

DEBUG = 'DEBUG'
ERROR = 'ERROR'
INFO = 'INFO'
SUCCESS = 'SUCCESS'

QUOTES = [
    '"Hear me out..."',
    '"Death! Death! DEATH!!"',
    '"Hello there!"'
]

def LIMIT (value, lower, upper):
    if value < lower:
        value = lower
    
    if value > upper:
        value = upper

    return value

def ENC_VALUE (value):
    return '[' + str(value) + ']'

def PRINT (string, print_type=INFO):
    print(ENC_VALUE(print_type) + '> ' + str(string))
