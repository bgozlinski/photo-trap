import cv2
from camera import Camera
from draw import Draw
from config import *

"""'320.0x240.0': 'OK'
'640.0x480.0': 'OK'
'1280.0x720.0': 'OK'"""

# initiate camera
initCamera = Camera(WIDTH, HEIGHT)

while True:
    # get frame
    frame = initCamera.getFrame()
    # draw rectangle in centre of frame with cW, cH distance from centre.
    cW, cH = 100, 100
    Draw(frame).rectangle((int(WIDTH/2-cW), int(HEIGHT/2 - cH)),
                          (int(cW + WIDTH/2), int(cH + HEIGHT/2)))
    # show frame on screen
    cv2.imshow("Frame", frame)

    # press q to end loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

