import pygame
import Adafruit_PCA9685
import time
import math

#Main Boolean
RUNNING = True

#Thrusters IDs
I2C_THRUST_1 = 1 #Vertical
I2C_THRUST_2 = 2 #Horizontal
I2C_THRUST_3 = 3 #Vertical
I2C_THRUST_4 = 4 #Horizontal
I2C_THRUST_5 = 5 #Vertical

# -1 = Reversed thruster direction, 1 = Normal thruster direction
THRUST_1_ALT = 1       #Front Right
THRUST_2_ALT = 1       #Front Left
THRUST_3_ALT = 1        #Back Right
THRUST_4_ALT = 1        #Back Left
THRUST_5_ALT = 1       #Middle Right


THRUSTER_AXIS_MOVE = 1
JOYSTICKS = []
JOYSTICK_AXIS_TURN = 0
JOYSTICK_AXIS_VERT = 3

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
    global JOYSTICKS

    pygame.init()

    JOYSTICKS = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    print('Found joystick.')

    if len(JOYSTICKS) > 0:
        for joystick in JOYSTICKS:
            joystick.init()
    
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

def set_pwm_value (channel, VAL, max_pw, min_pw, middle_pw):
    '''Set the PWM VAL of an esc/servo'''

    global PWM
    global PWM_TIMER_COUNT

    pw_range = (abs(max_pw - middle_pw) + abs(min_pw - middle_pw)) / 2
    pw = middle_pw + (VAL * pw_range)

    pw = pw if pw <= max_pw else max_pw
    pw = pw if pw >= min_pw else min_pw

    PWM.set_pwm(channel, 0, int(pw / PWM_TIMER_COUNT))

    return pw

setup()
set_pwm_value(0, 0, ESC_MAX_PW, ESC_MIN_PW, ESC_MIDDLE_PW)
set_pwm_value(1, 0, ESC_MAX_PW, ESC_MIN_PW, ESC_MIDDLE_PW)

time.sleep(5)
startTime = time.time()

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 1:
                RUNNING = False

    print(-JOYSTICKS[0].get_axis(THRUSTER_AXIS_MOVE))
    #print(set_pwm_value(1, -JOYSTICKS[0].get_axis(THRUSTER_AXIS_MOVE), ESC_MAX_PW, ESC_MIN_PW, ESC_MIDDLE_PW))
    #set_pwm_value(0, -JOYSTICKS[0].get_axis(THRUSTER_AXIS_MOVE), ESC_MAX_PW, ESC_MIN_PW, ESC_MIDDLE_PW)
    time.sleep(0.01)
    
PWM.set_all_pwm(0, 0)
PWM = None
