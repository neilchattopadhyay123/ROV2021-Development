import sys

sys.path.append('/home/pi/Desktop/ROV2020-Development/tests/gyro tests/gyro_sensor')

from gyro_sensor import IMU
from filter.madgwickahrs import MadgwickAHRS
from filter.quaternion import Quaternion
import numpy as np
import time
from threading import Thread


class Gyro(Thread):
    period = 1 / 256
    roll, pitch, yaw = 0, 0, 0

    def __init__(self, period=None):
        super().__init__()
        if period is not None:
            self.period = period

    def get_euler_angles(self):
        return self.roll, self.pitch, self.yaw

    def run(self):
        IMU.detectIMU()
        IMU.initIMU()

        filter = MadgwickAHRS(sample_period=self.period)

        accelerometer_values = [0, 0, 0]
        gyro_values = [0, 0, 0]

        i = 0

        start_time = 0

        while True:
            if i != 0:
                end_time = time.time()
                time.sleep(self.period - (end_time - start_time))

            accelerometer_values[0] = IMU.readACCx()
            accelerometer_values[1] = IMU.readACCy()
            accelerometer_values[2] = IMU.readACCz()

            gyro_values[0] = IMU.readGYRx()
            gyro_values[1] = IMU.readGYRy()
            gyro_values[2] = IMU.readGYRz()

            start_time = time.time()

            filter.update_imu(gyro_values, accelerometer_values)
            self.roll, self.pitch, self.yaw = filter.quaternion.to_euler_angles()

            if i % 30 == 0:
                print('roll: ', self.roll, 'pitch: ', self.pitch, 'yaw: ', self.yaw)

            i += 1
