# ROV2020-Development
Loggerhead ROV 2020 Development

# Libraries
Links :
- https://github.com/adafruit/Adafruit_Python_PCA9685
- https://github.com/adafruit/Adafruit_Python_PCA9685
- https://github.com/adafruit/Adafruit_Python_PureIO
- https://pypi.org/project/opencv-python/
- https://pypi.org/project/opencv-contrib-python/
- https://www.pygame.org/docs/
- https://picamera.readthedocs.io/en/release-1.13/
- https://github.com/bluerobotics/ms5837-python
- https://pypi.org/project/Pillow/2.2.2/
- https://matplotlib.org/
- https://pypi.org/project/RPi.GPIO/
- https://github.com/morgil/madgwick_py
- https://github.com/ozzmaker/BerryIMU

**Commands to run on a Raspberry Pi to install necessary packages :**
```
cd ~

sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get autoremove -y

sudo apt install -y apt-file
sudo apt-get install -y idle3
sudo apt-get install -y git
sudo apt-get install -y build-essential
sudo apt-get install -y python-dev

sudo apt-file update

sudo pip3 install --upgrade pip

sudo pip3 install opencv-python
sudo pip3 install pip-review
sudo pip3 install matplotlib
sudo pip3 install Pillow

sudo apt-get install -y libglib2.0-dev
sudo apt-get install -y libgirepository1.0-dev
sudo apt-get install -y libcairo2-dev

sudo apt-get install -y libhdf5-103
sudo apt-get install -y libatlas3-base
sudo apt-get install -y libjasper1
sudo apt-get install -y libqtgui4
sudo apt-get install -y libqt4-test

sudo pip3 install docutils --upgrade --ignore-installed
sudo pip3 install pigpio --upgrade --ignore-installed
sudo pip3 install psutil --upgrade --ignore-installed
sudo pip3 install pyxdg --upgrade --ignore-installed
sudo pip3 install PyYAML --upgrade --ignore-installed
sudo pip3 install roman --upgrade --ignore-installed
sudo pip3 install simplejson --upgrade --ignore-installed

sudo pip-review --local --verbose --auto

sudo pip3 install opencv-contrib-python==4.1.0.25
sudo pip3 install wrapt==1.11.*

git clone https://github.com/adafruit/Adafruit_Python_PCA9685.git ./Adafruit_Python_PCA9685
git clone https://github.com/adafruit/Adafruit_Python_GPIO.git ./Adafruit_Python_GPIO
git clone https://github.com/adafruit/Adafruit_Python_PureIO.git ./Adafruit_Python_PureIO
```
