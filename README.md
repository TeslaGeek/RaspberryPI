# RaspberryPI
Raspberry PI 3a+ projects

The Pi board was installed with a full BullsEye-arm64 version which came with new camera module libcamera. When libcamera is installed through the RaspiOS, it automatically looks after the camera module 3 detection i.e., unlike previous camera modules (e.g., 1 and 2) you do not need to go to the bios or pi preferences / interface and alter the camera settings!  

To setup the PiCamera module 3, you could follow this link https://www.tomshardware.com/how-to/use-picamera2-take-photos-with-raspberry-pi

Once the camera module is installed, you can access camera controls using picamera2 library. Picamera2 is the libcamera-based replacement for Picamera which was a Python interface to the Raspberry Pi's legacy camera stack. The manual for picamera2 is available from here https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf

To connect the Adafruit ADXL345 accelerometer to the pi board you could follow this link: https://pimylifeup.com/raspberry-pi-accelerometer-adxl345/

Finally if you are comfortable writing your python code on a desktop or a laptop (like me), you could use SSH and AFP server to communicate with the pi board. To find some instructions on the SSH file transfer and AFP servers follow this link : https://pimylifeup.com/raspberry-pi-afp/

There are three python files here, one for recording accelerometer data via threading, another one for recording mjpeg video via threading and the last one for initiating and coordinating the interactions. The main function also has a keyboard listener which terminates the threads when ctrl+C is pressed.
