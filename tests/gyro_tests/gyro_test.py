# MPU6050 9-DoF Example Printout

# https://makersportal.com/blog/2019/11/11/raspberry-pi-python-accelerometer-gyroscope-magnetometer#interfacing=

from mpu9250_i2c import *

time.sleep(1) # delay necessary to allow mpu9250 to settle

print('recording data')
while 1:
    try:
        ax,ay,az,wx,wy,wz = mpu6050_conv() # read and convert mpu6050 data
        # mx,my,mz = AK8963_conv() # read and convert AK8963 magnetometer data

        print('{}'.format('-'*30))
        print('accel [g]: x = {}, y = {}, z = {}'.format(ax,ay,az))
        print('gyro [dps]:  x = {}, y = {}, z = {}'.format(wx,wy,wz))
        # print('mag [uT]:   x = , y = , z = '.format(mx,my,mz))
        # print('{}'.format('-'*30))
    except Exception as e:
        print(str(e))
        
    time.sleep(0.1)
