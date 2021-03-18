/*      This program  reads the angles and heading from the accelerometer, gyroscope
        and compass on a BerryIMU connected to an Arduino.


       The BerryIMUv1, BerryIMUv2 and BerryIMUv3 are supported


       Feel free to do whatever you like with this code.
       Distributed as-is; no warranty is given.

       https://ozzmaker.com/berryimu/

*/

#include "IMU.h"
#include "Adafruit_AHRS_Madgwick.h"
#include <math.h>

#define DT  1/50        // Loop time
#define AA  0.97         // complementary filter constant
#define G_GAIN 0.070    // [deg/s/LSB]

byte buff[6];
int accRaw[3];
int magRaw[3];
int gyrRaw[3];
float m_PI = 3.14159265358979323846;
float rate_gyr_y = 0.0;   // [deg/s]
float rate_gyr_x = 0.0;    // [deg/s]
float rate_gyr_z = 0.0;     // [deg/s]
float gyroXangle = 0.0;
float gyroYangle = 0.0;
float gyroZangle = 0.0;
float AccYangle = 0.0;
float AccXangle = 0.0;
float CFangleX = 0.0;
float CFangleY = 0.0;
float pitch_radians = 0.0;
float yaw_radians = 0.0;
float roll_radians = 0.0;
float pitch_degrees = 0.0;
float yaw_degrees = 0.0;
float roll_degrees = 0.0;
Adafruit_Madgwick gyro;


unsigned long startTime;

void setup() {
         // join i2c bus (address optional for master)
  Serial.begin(115200);  // start serial for output
  delay(500);
  detectIMU();
  
  enableIMU();
  gyro = Adafruit_Madgwick();
  gyro.begin(1/DT);
}

void loop() {
  startTime = millis();

  //Read the measurements from  sensors
  readACC(buff);
  accRaw[0] = (int)(buff[0] | (buff[1] << 8));   
  accRaw[1] = (int)(buff[2] | (buff[3] << 8));
  accRaw[2] = (int)(buff[4] | (buff[5] << 8));

  readMAG(buff);
  magRaw[0] = (int)(buff[0] | (buff[1] << 8));   
  magRaw[1] = (int)(buff[2] | (buff[3] << 8));
  magRaw[2] = (int)(buff[4] | (buff[5] << 8));


  readGYR(buff);
  gyrRaw[0] = (int)(buff[0] | (buff[1] << 8));   
  gyrRaw[1] = (int)(buff[2] | (buff[3] << 8));
  gyrRaw[2] = (int)(buff[4] | (buff[5] << 8));

  //Convert Gyro raw to degrees per second
  rate_gyr_x = (float) gyrRaw[0] * G_GAIN;
  rate_gyr_y = (float) gyrRaw[1]  * G_GAIN;
  rate_gyr_z = (float) gyrRaw[2]  * G_GAIN;

  gyro.updateIMU(rate_gyr_x, rate_gyr_y, rate_gyr_z, accRaw[0], accRaw[1], accRaw[2]);

  float pitch_radians = gyro.getPitchRadians();
  float yaw_radians = gyro.getYawRadians();
  float roll_radians = gyro.getRollRadians();

  float pitch_degrees = gyro.getPitch();
  float yaw_degrees = gyro.getYaw();
  float roll_degrees = gyro.getRoll();

  //Calculate the angles from the gyro
  // gyroXangle+=rate_gyr_x*DT;
  // gyroYangle+=rate_gyr_y*DT;
  // gyroZangle+=rate_gyr_z*DT;

  // //Convert Accelerometer values to degrees
  // AccXangle = (float) (atan2(accRaw[1],accRaw[2])+M_PI)*RAD_TO_DEG;
  // AccYangle = (float) (atan2(accRaw[2],accRaw[0])+M_PI)*RAD_TO_DEG;


  // //If IMU is up the correct way, use these lines
  //       AccXangle -= (float)180.0;
  // if (AccYangle > 90)
  //         AccYangle -= (float)270;
  // else
  //   AccYangle += (float)90;


  // //Complementary filter used to combine the accelerometer and gyro values.
  // CFangleX=AA*(CFangleX+rate_gyr_x*DT) +(1 - AA) * AccXangle;
  // CFangleY=AA*(CFangleY+rate_gyr_y*DT) +(1 - AA) * AccYangle;


  // //Compute heading  
  // float heading = 180 * atan2(magRaw[1],magRaw[0])/m_PI;
  
  // //Convert heading to 0 - 360
  //         if(heading < 0)
  //           heading += 360;
            
  // Serial.print("#AccX\t");
  // Serial.print(AccXangle);
  // Serial.print("\t###  AccY  ");
  // Serial.print(AccYangle);
  
  // Serial.print("  ###  GyrX\t");
  // Serial.print(gyroXangle);
  // Serial.print("  ###  GyrY  \t");
  // Serial.print(gyroYangle);
  // Serial.print("   ###  GyrZ\t");
  // Serial.print(gyroZangle);
  // Serial.print("     ######    CFangleX\t");
  // Serial.print(CFangleX);
  // Serial.print("   ######  CFangleY   \t");
  // Serial.print(CFangleY);
  // Serial.print("   ######  heading   \t");
  // Serial.print(heading); 
  // Serial.print("    --Loop Time--\t");

  //Each loop should be at least 20ms.
  while(millis() - startTime < (DT*1000)){
    delay(1);
  }

  Serial.print("Pitch: " + (String) pitch_degrees);
  Serial.print("Yaw: " + (String) yaw_degrees);
  Serial.print("Roll: " + (String) roll_degrees);
}
