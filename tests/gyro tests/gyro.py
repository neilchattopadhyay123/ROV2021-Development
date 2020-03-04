import sys

sys.path.append('/home/pi/Desktop/ROV2020-Development/tests/gyro tests/gyro_sensor')

from gyro_sensor import IMU
from filter.madgwickahrs import MadgwickAHRS
from filter.quaternion import Quaternion
import numpy as np
import time
import datetime

sample_period = 0

IMU.detectIMU()
IMU.initIMU()

filter = MadgwickAHRS()

accelerometer_values = []
gyro_values = []

start_time = time.time()

for i in range(20000000):

    end_time = time.time()

    ACCx = IMU.readACCx()
    ACCy = IMU.readACCy()
    ACCz = IMU.readACCz()
    GYRx = IMU.readGYRx()
    GYRy = IMU.readGYRy()
    GYRz = IMU.readGYRz()

    accelerometer_values.append(IMU.readACCx())
    accelerometer_values.append(IMU.readACCy())
    accelerometer_values.append(IMU.readACCz())

    gyro_values.append(IMU.readGYRx())
    gyro_values.append(IMU.readGYRy())
    gyro_values.append(IMU.readGYRz())

    if (i % 100) == 0:
        print('gyro array:', gyro_values)
        print('accelerometer_array', accelerometer_values)

    if i == 0:
        start_time = time.time()
        sample_period = start_time - end_time

    filter.samplePeriod = sample_period

    filter.update_imu(gyro_values, accelerometer_values)
    roll, pitch, yaw = filter.quaternion.to_euler_angles()

    if (i % 100) == 0:
        print("roll: ", roll, "pitch: ", pitch, "yaw: ", yaw)

    if i != 0:
        start_time = time.time()
