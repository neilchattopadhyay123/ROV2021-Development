import pygame
from pygame.locals import *
pygame.init()
import tkinter as tk
from tkinter import *
import os
root = tk.Tk()
import time
from dial import *


global horizonDisplay

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
horizonDisplay = False

def openHorizon():
    global horizonDisplay

    horizonWindow_w = 300 #Gauge size is set to 300x300 pixels in dial.py
    horizonWindow_h = 300

    while not horizonDisplay:
        # Initialise screen and set screen pos
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (screen_w-horizonWindow_w, screen_h-horizonWindow_h)
        screen = pygame.display.set_mode((horizonWindow_w, horizonWindow_h), pygame.NOFRAME)
        screen.fill(0x222222)
        screen.set_alpha(None)
           
        # Initialise Dials.
        horizon = Horizon(0,0)

        # Dummy test data
        curPos = pygame.mouse.get_pos()
        rf_data = {'RX_est_x':curPos[0]/2, 'RX_est_y':curPos[1]/2}
        
        if(not rf_data == None):
            # Update dials.
            horizon.update(screen, 127 - rf_data['RX_est_x'], 127 - rf_data['RX_est_y'] )
            pygame.display.update()

openHorizon()
