from picamera import PiCamera
from time import sleep
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)
camera = PiCamera()
while True:
	msg = ser.readline()
	print(msg)
	if "record" in msg:
		camera.start_preview()
		
		camera.start_recording('/home/pi/Desktop/video.h264')
		camera.wait_recording(20)
		camera.stop_recording()
		 
		camera.stop_preview()
		exit()
