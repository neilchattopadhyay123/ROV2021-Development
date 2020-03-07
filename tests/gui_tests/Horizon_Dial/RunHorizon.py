import pygame
from pygame.locals import *
pygame.init()
import tkinter as tk
from tkinter import *
import os
root = tk.Tk()
import time
from dial import *

def openHorizon():
    horizonDisplay = False
    horizonWindow_w = 300 #Gauge size is set to 300x300 pixels in dial.py
    horizonWindow_h = 300
    
    # Initialise screen and set screen pos
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode((horizonWindow_w, horizonWindow_h), pygame.NOFRAME)
    screen.fill(0x222222)
    screen.set_alpha(None)
       
    # Initialise Dials.
    horizon = Horizon(0,0)

    while not horizonDisplay:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                horizonDisplay = True
        
        # Dummy test data
        curPos = pygame.mouse.get_pos()
        rf_data = [curPos[0], curPos[1]]

        horizon.update(screen, rf_data[0] - (horizonWindow_w / 2), rf_data[1] - (horizonWindow_h / 2))

        pygame.display.update()

openHorizon()
