import RPi.GPIO as GPIO

# code will only run on raspberry pi

# set upt the numbering of pins
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

channel = 11

# setup the input of the pin
GPIO.setup(channel, GPIO.IN)

# checks for if it is leaking
while True:
    if GPIO.input(channel) == 1:
        print('leaking')

# reset the pins
GPIO.cleanup()