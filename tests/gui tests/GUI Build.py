import pygame
from pygame.locals import *
pygame.init()
import tkinter as tk
from tkinter import *
import os
import serial
import math
import sys
root = tk.Tk()
import time
from dial import *

root.title('Loggerhead ROV GUI')
menubar = Menu(root)
root.config(menu=menubar)

#Constants
global screen_w
global screen_h
global menuSwitch
global sensorSwitch
global GaugesSwitch
global CompSwitch
global AutoSwitch
global ImageRecSwitch
global ControlsDisplay
global controlLabel
global horizonDisplay

#Inital Variables
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
menuSwitch = True
ControlsDisplay = False
controlLabel = None
horizonDisplay = False

#Tracks keys pressed
def key(event):
    if(event.char == '\x1b'):
        exitFullscreen()
    if(event.char == '`'):
        fullscreen()
    if(event.char == '1'):
        hideMenu()


    #Temp
    if(event.char == '2'):
        openHorizon()

        
    #Prints key press
    print ('pressed', repr(event.char))

#Toggles Labels
def toggle(label, r, c):
    if label.winfo_ismapped():
        label.grid_remove()
    else:
        label.grid(row=r, column=c)


#Hide/Show Top Bar menu
def hideMenu():
    global menuSwitch
    
    emptyMenu = Menu(root)
    if menuSwitch:
        root.config(menu=emptyMenu)
    else:
        root.config(menu=menubar)
    menuSwitch = not menuSwitch
    
#Fullscreen
def fullscreen():
    global screen_w, screen_h
    root.overrideredirect(True)
    root.geometry('%dx%d+0+0' % (screen_w, screen_h))

def exitFullscreen():
    global screen_w, screen_h
    root.overrideredirect(False)
    root.geometry('%dx%d+0+0' % (screen_w/2, screen_h/2))

#Shows Controls for ROV
def openControls():
    global ControlsDisplay
    global controlLabel

    if controlLabel == None:
        file = open("ROV Controls.txt", 'r')
        if file is not None:
            #Create Label to display controls
            content = file.read()
            var = StringVar()
            var.set(content)
            controlLabel = tk.Label(root, textvariable=var, relief=RAISED)
            controlLabel.grid(row=0, column=2)
    else:
        toggle(controlLabel, 0, 2)

#Camera Display
    
#Guages Display    
def openHorizon():
    global horizonDisplay

    horizonWindow_w = 300 #Gauge size is set to 300x300 pixels in dial.py
    horizonWindow_h = 300 

    while not horizonDisplay:
        # Initialise screen and set screen pos
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (screen_w-horizonWindow_w, screen_h-horizonWindow_h)
        screen = pygame.display.set_mode((horizonWindow_w, horizonWindow_h))
        screen.fill(0x222222)
           
        # Initialise Dials.
        horizon = Horizon(0,0)

        # Dummy test data
        curPos = pygame.mouse.get_pos()
        rf_data = {'RX_est_x':curPos[0]/2, 'RX_est_y':curPos[1]/2}
        pygame.time.delay(100)

        if(not rf_data == None):
            # Update dials.
            horizon.update(screen, 127 - rf_data['RX_est_x'], 127 - rf_data['RX_est_y'] )
            pygame.display.update()

            

#Menus
submenu = Menu(menubar)
menubar.add_cascade(label='Menu', menu=submenu)
submenu.add_command(label='Hide Menu', command=hideMenu)
submenu.add_command(label='Exit', command=exit)

Sensors = Menu(menubar)
menubar.add_cascade(label='Sensors', menu=Sensors)
Sensors.add_command(label='On/Off')

Gauges = Menu(menubar)
menubar.add_cascade(label='Gauges', menu=Gauges)
Gauges.add_command(label='On/Off', command=openHorizon)

Components = Menu(menubar)
menubar.add_cascade(label='Components', menu=Components)
Components.add_command(label='On/Off')


Autonomous = Menu(menubar)
menubar.add_cascade(label='Autonomous', menu=Autonomous)

ImageRecog = Menu(menubar)
menubar.add_cascade(label='Image Recognition', menu=ImageRecog)

Help = Menu(menubar)
menubar.add_cascade(label='Help', menu=Help)
Help.add_command(label='Controls', command=openControls)


root.bind('<Key>', key)


