# importing libraries 
import cv2 
import time
import numpy as np 
import RPi.GPIO as GPIO
from picamera2 import Picamera2, Preview
from libcamera import Transform
from ultralytics import YOLO

# Setup camera 
picam = Picamera2()
picam.configure(picam.create_video_configuration({"format": "YUV420"}, transform = Transform(vflip=1)))
picam.start()
model = YOLO('best.pt')

# Set up GPIOs
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

# signal starting of program
GPIO.output(26, GPIO.HIGH)
time.sleep(0.05)
GPIO.output(26, GPIO.LOW)
time.sleep(0.05)
GPIO.output(26, GPIO.HIGH)
time.sleep(0.05)
GPIO.output(26, GPIO.LOW)

# While loop 
while True: 
	
	# Capture frame-by-frame 
	Input_Image = picam.capture_array()
	RGB_image = cv2.cvtColor(Input_Image, cv2.COLOR_YUV420p2RGB)
	
	results = model.predict(RGB_image, show=True)
	for result in results:
		if result:
			GPIO.output(26, GPIO.HIGH)
			print("weapon detected")
		else:
			GPIO.output(26, GPIO.HIGH)
			time.sleep(0.005)
			GPIO.output(26, GPIO.LOW)
			print("no detection")
	
	key = cv2.waitKey(1)
	if key == ord('q'): 
		break

# Close picam
picam.close()