"""radar - simultaneous localization and mapping"""
import os
import cv2
from display import Display

W = 1920//2
H = 1080//2

RESOURCES = os.path.join(os.getcwd(), "resources")
videofile = os.path.join(RESOURCES, "test_countryroad.mp4")

disp = Display(W, H)

def process_frame(frame):
    frame = cv2.resize(frame, (W, H))
    disp.paint(frame)

cap = cv2.VideoCapture(videofile)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    process_frame(frame)

# release the capture
cap.release()

