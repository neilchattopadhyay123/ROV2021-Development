import FaBo9Axis_MPU9250
import time
import sys

mpu9250 = FaBo9Axis_MPU9250.MPU9250()

try:
    while True:
        print("ACCEL | " + str(mpu9250.readAccel()))
        print("GYRO  | " + str(mpu9250.readGyro()))
        print("MAG   | " + str(mpu9250.readMagnet()))
        print("TEMP  | " + str(mpu9250.readTemperature()))
        print("------------------------------------------------------")

        time.sleep(0.5)
except KeyboardInterrupt:
    sys.exit()
        
