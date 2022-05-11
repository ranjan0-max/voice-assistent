# import win32api

# drives = win32api.GetLogicalDriveStrings()
# # drives = drives.split('\000')[:-1]
# drive=[]
# drive.append(drives[0])
# drive.append(drives[4])
# print(drive)

import pyautogui
import pywhatkit
import time
import random


# pyautogui.press('super')
# # time.sleep(0.5)
# for i in 'word pad':
#     pyautogui.press(i)
# time.sleep(0.5)
# pyautogui.press('enter')
# for i in range(0,2):
# import the opencv library
import cv2


# define a video capture object
vid = cv2.VideoCapture(0)

while(True):
	ret, frame = vid.read()

	# Display the resulting frame
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
vid.release()
cv2.destroyAllWindows()
