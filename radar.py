"""radar - simultaneous localization and mapping"""
import os
import cv2
import numpy as np
from display import Display
from extractor import Extractor

W = 1920//2
H = 1080//2

# Colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)

RESOURCES = os.path.join(os.getcwd(), "resources")
videofile = os.path.join(RESOURCES, "test_countryroad.mp4")

disp = Display(W, H)
fe = Extractor()

#initialize orb detector
orb = cv2.ORB_create(edgeThreshold=15, patchSize=31,
                     nlevels=8, fastThreshold=20,
                     scaleFactor=1.2, WTA_K=2,
                     scoreType=cv2.ORB_FAST_SCORE,
                     firstLevel=0, nfeatures=1024)

def process_frame(frame):
    frame = cv2.resize(frame, (W, H))
    matches = fe.extract(frame)
    # print("%d matches" % (len(matches)))
    # kp, desc = orb.detectAndCompute(frame, None)
    for pt1, pt2 in matches:
        u1,v1 = map(lambda x: round(x), pt1)
        u2,v2 = map(lambda x: round(x), pt2)

        # draw matches
        cv2.circle(frame, (u1,v1), color=GREEN, radius=3)
        cv2.line(frame, (u1,v1), (u2, v2), RED, 2)
    # draw only keypoints location, not size and orientation
    #img = cv2.drawKeypoints(frame, kp, None, GREEN,
    #                        flags=cv2.DrawMatchesFlags_DEFAULT)
    disp.paint(frame)

if __name__ == "__main__":
    cap = cv2.VideoCapture(videofile)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        process_frame(frame)

    # release the capture
    cap.release()

