import pigpio
import subprocess
import time
import pygame

THRUSTER_ID = 0
THRUSTER_AXIS = 1

FREQ = 100
MIDDLE = 1500
RANGE = 400

GPIO = None

JOYSTICKS = []

def setup ():
    global THRUSTER_ID
    global GPIO
    global FREQ
    global JOYSTICKS
    
    pygame.init()

    JOYSTICKS = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    print('Found joystick.')

    if len(JOYSTICKS) > 0:
        for joystick in JOYSTICKS:
            joystick.init()
    
    subprocess.call('sudo pigpio', shell=True)
    time.sleep(0.5)

    GPIO = pigpio.pi()
    if not GPIO.connected:
        print('Could not connect to ESC.')
    else:
        print('Connected to ESC.')

        GPIO.set_mode(THRUSTER_ID, pigpio.ALT4)
        GPIO.set_PWM_range(THRUSTER_ID, 100)

        print('Thruster PWM range is ' + str(GPIO.get_PWM_range(THRUSTER_ID)))

        GPIO.set_PWM_frequency(THRUSTER_ID, FREQ)

        print('Thruster PWM frequency is ' + str(GPIO.get_PWM_FREQUENCY(THRUSTER_ID)))

def main ():
    global THRUSTER_ID
    global THRUSTER_AXIS
    global GPIO
    global MIDDLE
    global RANGE
    global FREQ
    global JOYSTICKS
    
    setup()
    
    running = True
        
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 1:
                    running = False

        pwm_value = int((MIDDLE + (-JOYSTICKS[0].get_axis(THRUSTER_AXIS) * RANGE)) / FREQ)
        print(pwm_value)
        
        GPIO.set_PWM_dutycycle(THRUSTER_ID, pwm_value)

    GPIO.set_PWM_dutycycle(THRUSTER_ID, 0)
    GPIO.stop()

if __name__ == '__main__':
    main()

pygame.quit()
