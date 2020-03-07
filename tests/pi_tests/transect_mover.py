import pygame
import Adafruit_PCA9685
import time
import math

#Main Boolean
RUNNING = True

#Thrusters IDs
I2C_THRUST_2 = 2 #Horizontal
I2C_THRUST_4 = 4 #Horizontal

PWM = None # Adafruit PWM board object

FREQ = 200 # PWM frequency being sent to the esc/servos
ADJUST_25MHZ = 1.0247 # Correction factor for 25MHz oscillator tolerance (each PCA9685 board may be different!)

ESC_MAX_PW = 1900 # ESC pulsewidth ranges
ESC_MIDDLE_PW = 1500
ESC_MIN_PW = 1100

# Calculate PWM prescale value
PRESCALE_VAL = 25000000.0 # 25 MHz
PRESCALE_VAL /= 4096 # 12-bit
PRESCALE_VAL /= float(FREQ)
PRESCALE_VAL -= 1.0
PRESCALE = int(math.floor(PRESCALE_VAL + 0.5))
PWM_TIMER_COUNT = (1 / (25000000.0 * ADJUST_25MHZ)) * PRESCALE * 1000000.0 # This is the microsecond step size (adjusted) of pwm counter

def setup():
    global PWM
    global FREQ

    pygame.init()

    try:
        PWM = Adafruit_PCA9685.PCA9685()
        PWM.set_pwm_freq(FREQ)

        print('Successfully set up I2C board.')
        print('> 25MHz Adjustment Scale Factor : ' + str(ADJUST_25MHZ))
        print('> Target Frequency [Hz] : ' + str(FREQ))
        print('> Actual Approx [Adjusted] [Hz] : [ {:3.3f} ]'.format(FREQ * ADJUST_25MHZ))
        print('> PRESCALE : ' + str(PRESCALE))
        print('> PWM Timer Count [Adjusted] [us] : [ {:3.3f} ]'.format(PWM_TIMER_COUNT))

    except Exception as e:
        print('Could not set up I2C board : ' + str(e))

    def set_pwm_value(channel, VAL):
        '''Set the PWM VAL of an esc/servo'''

        global PWM
        global PWM_TIMER_COUNT
        global ESC_MAX_PW
        global ESC_MIN_PW
        global ESC_MIDDLE_PW

        pw_range = (abs(ESC_MAX_PW - ESC_MIDDLE_PW) + abs(ESC_MIN_PW - ESC_MIDDLE_PW)) / 2
        pw = ESC_MIDDLE_PW + (VAL * pw_range)

        pw = pw if pw <= ESC_MAX_PW else ESC_MAX_PW
        pw = pw if pw >= ESC_MIN_PW else ESC_MIN_PW

        PWM.set_pwm(channel, 0, int(pw / PWM_TIMER_COUNT))

        return pw

    setup()

    # Initializing Thrusters
    set_pwm_value(I2C_THRUST_2, 0)
    set_pwm_value(I2C_THRUST_4, 0)

    time.sleep(5)
    startTime = time.time()
    counter=15
    while RUNNING:
        set_pwm_value(I2C_THRUST_2, 1750)
        set_pwm_value(I2C_THRUST_4, 1750)
        time.sleep(1)
        counter=counter+1
        if counter==15:
            RUNNING=False

PWM.set_all_pwm(0, 0)
PWM = None