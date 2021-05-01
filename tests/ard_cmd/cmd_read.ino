#include <Wire.h>
#include <Servo.h>

byte micro_pin =  8; // micro       thruster
byte vertL_pin =  9; // vertical    thruster, left  side
byte vertR_pin = 10; // vertical    thruster, right side
byte rotL_pin  = 11; // horizontal  thruster, left  side
byte rotR_pin  = 12; // horizontal  thruster, right side
byte tail_pin  = 13; // vertical    thruster, rear  side
byte mano_pin  = 14; // manipulator servo
byte cam_pin   = 15; // camera      servo
Servo micro;
Servo vertL;
Servo vertR;
Servo rotL;
Servo rotR;
Servo tail;
Servo mano;
Servo cam;


void setup() 
{
    Serial.begin(9600);
    Wire.begin(0x08);

    micro.attach(micro_pin);
    vertL.attach(vertL_pin);
    vertR.attach(vertR_pin);
    rotL.attach(rotL_pin);
    rotR.attach(rotR_pin);
    tail.attach(tail_pin);
    mano.attach(mano_pin);
    cam.attach(cam_pin);
    micro.writeMicroseconds(1500);
    vertL.writeMicroseconds(1500);
    vertR.writeMicroseconds(1500);
    rotL.writeMicroseconds(1500);
    rotR.writeMicroseconds(1500);
    tail.writeMicroseconds(1500);
    mano.writeMicroseconds(1700);

    int cam_pos = 90;

    delay(7000); // ESCs use time to initialize, detect init signal
    
    int data_cache[3][8];
}

void loop() 
{
    rec_sort();
    cache_dump();
}

void rec_sort()
{
    while (Wire.available())
    {   
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 9; j++)
                data_cache[i][j] = Wire.read();
    }
}

void hard_clear() // wipe cache, start button
{
    for (int i = 0; i < 3; i++)
       for (int j = 0; j < 8; j++)
            data_cache[i][j] = 0;
}

void soft_clear() // wipe thruster data, back button
{
    for (int i = 2; i < 6; i++)
        data_cache[0][i] = 0;
    for (int i = 0; i < 8; i++)
        data_cache[1][i] = 0;
    for (int i = 0; i < 4; i++)
        data_cache[2][i] = 0;
}


void byte_parse()
{
    int dpad_up = data_cache[0][0]; // cam to neutral
    int dpad_down = data_cache[0][1]; // cam down 
    int trig_left = 2*data_cache[0][2] + data_cache[0][3]; // micro reverse
    int trig_right = 2*data_cache[0][4] + data_cache[0][5]; // micro forward

    int joy_left_y = 8*data_cache[1][0] + 4*data_cache[1][1] + 2*data_cache[1][2] + data_cache[1][3]; // main forward/backward
    int joy_left_x = 8*data_cache[1][4] + 4*data_cache[1][5] + 2*data_cache[1][6] + data_cache[1][7]; // main turn left/right
    
    int joy_right_y = 8*data_cache[2][0] + 4*data_cache[2][1] + 2*data_cache[2][2] + data_cache[2][3]; // main depth
    int bumper_left = data_cache[2][4]; // close manipulator
    int bumper_right = data_cache[2][5]; // open manipulator
    int back = data_cache[2][6]; // wipe thruster data
    int start = data_cache[2][7]; // wipe all data
}

void run_change()
{
    if (dpad_up)
    {
        cam_pos = 90;
        cam.write(cam_pos); // cam to neutral
    }
    if (dpad_down)
    {
        cam_pos -= 15;
        cam.write(cam_pos); // cam down, by increment
    }
    
    vertL.writeMicroseconds((joy_right_y + 1)*50 + 1100);
    vertR.writeMicroseconds((joy_right_y + 1)*50 + 1100);
    tail.writeMicroseconds((joy_right_y + 1)*50 + 1100);

    rotL.witeMicroseconds(((joy_left_x + 1)*25 + 1300) + ((joy_left_y + 1)*25 + 1300));
    rotR.witeMicroseconds(1-((joy_left_x + 1)*25 + 1300) + ((joy_left_y + 1)*25 + 1300));

    if (trig_right > trig_left)
        micro.writeMicroseconds((trig_right + 1)*25 + 1500); // run micro forward
    else if (trig_left > trig_right)
        micro.writeMicroseconds(1-(trig_left + 1*25) + 1500); // run micro backward
    else
        micro.writeMicroseconds(1500); // set micro to neutral

    if (bumper_left) {
        mano.writeMicroseconds(1300); // close manipulator
    }

    if (bumper_right) {
        mano.writeMicroseconds(1700); // open manipulator
    }



}

