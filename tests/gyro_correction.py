from gyro_tests.gyro import Gyro
from pi_tests.thrusters_test import set_pwm_value
import pygame

import matplotlib
import numpy
import time

gyro = Gyro(period=.1)

gyro.start()

gyro.get_pitch()
