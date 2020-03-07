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

**How to Set Up Raspberry Pi**
> Materials :
> - Raspberry Pi
> - Raspberry Pi Power Cable
> - HDMI Cable
> - External Monitor
> - USB Keyboard
> - USB Mouse
> - Micro SD card to USB adapter
> - Laptop / Desktop (WINDOWS)
> - Ethernet Cable

- Download the [Raspian OS](https://www.raspberrypi.org/downloads/raspbian/, "Raspian OS Download Page"). Download the .ZIP file underneath the "Raspian Buster with Desktop" option. When the download finishes, unzip the folder and there should be an image file inside. Save this for later.
- Download and install [BalenaEtcher](https://www.balena.io/etcher/, "BalenaEtcher Download").
- Run the BalenaEtcher software and it should be telling you to select an image. Click the "Select Image" button and navigate to the image file for Raspian OS that you downloaded earlier. Then, plug in the micro SD card to the computer using an adapter. In BalenaEtcher, click the "Select Target" button and select the micro SD that was just plugged in. **BE CAREFUL! If you have multiple USB devices plugged in, make sure you are selecting the right one. This process will overwrite all the data stored.**
- Click the "Flash" button in BalenaEtcher and it should start flashing the device. This process takes around 10 minutes. While it is flashing the device, go download and install [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/, "VNC Viewer Download"). This will be used later once the IP of the Raspberry Pi is set up. **NOTE: If a window pops up telling you to format the micro SD card, hit "Cancel". We just did that by flashing the device.**
- Once the micro SD is done flashing, safely eject the device and plug the micro SD card into the Raspberry Pi. Make sure the Raspberry Pi is unplugged when you do this. The connectors (the little gold bars) on the micro SD card should be facing up when you insert the micro SD card into the Raspberry Pi.
- Plug the Raspberry Pi into an external monitor using an HDMI cable. Plug in a USB mouse and keyboard into the USB slots on the Raspberry Pi. Then, plug in the Raspberry Pi into a power source. There are 2 LED lights on the Raspberry Pi. One is red, and the other is green. The red LED light means that the Raspeberry Pi has power, so if it lit up then you are good. The green LED lights up whenever the micro SD card is being used. When the Raspberry Pi first starts up, this green light should be flashing a lot as it loads the Raspian OS.
- At this point, you should see the Raspberry Pi desktop! There should be a welcome screen telling you that you need to set up the Raspberry Pi. Follow the on-screen instructions. **NOTE: If you cannot connect to wifi at this time, that is fine. However, we will need it later to install the necessary libraries.** When prompted to update the system, click "Skip". We will do that later. Once the setup is complete, click the "Restart" button. The Rasperry Pi should reboot.
- Once the desktop is visible again, we need to set up the Raspberry Pi IP address. Open a termial window by clicking the terminal icon on the taskbar at the top of the screen. Type the command `sudo nano etc/dhcpcd.conf` and hit "Enter". You should now see a lot of lines of code. These lines depict different settings about your Raspberry Pi. Scroll down until you see a line that reads "Example Static IP Configuration". Delete the "#" in front of the first 2 lines underneath the "Example Static IP Configuration" line. The IP address is set on the second line that should read something along the lines of `static_ip_address=192.168.X.XX/24`. In order to change it, we need to change the last 2 numbers of the IP address. Set the IP address to `192.168.2.4`. **NOTE: Leave the `/24` at the end of the line. This is very important.** The IP address should be changed now. To exit the editor, do "CTRL+X" to save the file. Type "Y" to save the changes, and then press "Enter" to exit the editor. You should return to the normal terminal window.
- Now we need to allow the Raspberry Pi to access its ethernet port. For some reason, this setting is by default disabled. Click the "Raspberry Pi" button and under the tab "Preferences", click on "Raspberry Pi Configuration". This should open a new window. Go to the "Interfaces" tab and enable "Camera", "SSH", "VNC", "SPI", and "I2C". Then click "OK". When it asks you to reboot, click "No".
- Shut down the Raspberry Pi by clicking "Raspberry Pi" button in the top left of the screen, and then navigating to the "Shutdown" option. You can also type the command `poweroff` in the terminal. Unplug the Raspberry Pi from the external monitor as well as unplug the USB devices.
- Now, we need to make sure your computer's IP address is able to communicate to your Raspberry Pi. On your desktop/laptop, open the Control Panel my searching for "Control Panel" in the Windows search bar. Click the "Network and Internet" option, then click "Network and Sharing Center". On the left side of the window, click the option "Change adapter settings". This should open a new window. Right-click on the ethernet connection and select "Properties". Highlight the option "Internet Protocol Version 4 (TCP/IPv4)" inside the box by clicking the option (NOT THE CHECK BOX). Then select the "Properties" button below the box of options. To set an IP address, select the "Use the following IP address" option. This should now allow you to type in a custom IP address. For the "IP address", we need to make sure the first 3 numbers are the same as on the Raspberry Pi. Make the IP address `192.168.2.5`. The "Subnet Mask" should automatically fill in when you are finished typing the IP address, but if it does not, make the "Subnet Mask" `255.255.255.0`. Then click "OK" at the buttom of the screen. Close out of all the Control Panel tabs.
- Plug in the ethernet cable into the Raspberry Pi and connect it to your computer. Then plug in your Raspberry Pi back into a power source.
- Open "VNC Viewer" which you should have installed earlier. In the bar at the top, type in the IP address that we gave the Raspberry Pi, which was `192.168.2.4`. Then press "Enter" and a window should pop up. Click "Continue" and in the "Username" box, type `pi`. In the "Password" box, type in the password you set earlier. Tick the checkmark box for "Remember Password" so you do not have to type in the password every time you connect to your Raspberry Pi. **If it does not connect, there are a few things we can check:**
  - Make sure the ethernet cable is plugged in.
  - Disable your firewall, as it could be preventing a connection to be set up.
- You should now see the Raspberry Pi desktop inside a new window on your computer screen! To finish the setup, type in the commands below into the terminal:
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
