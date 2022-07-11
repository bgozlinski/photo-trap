import cv2
from camera import Camera
from draw import Draw
from config import *

# initiate camera
initCamera = Camera(WIDTH, HEIGHT)

while True:
    # get frame
    frame = initCamera.getFrame()
    # draw rectangle in centre of (WIDTH, HEIGHT) with (dW, dH) lengths.
    Draw(frame).rectangle((int(WIDTH/2-DISTANCE_WIDTH/2), int(HEIGHT/2 - DISTANCE_HEIGHT/2)),
                          (int(DISTANCE_WIDTH + WIDTH/2), int(DISTANCE_HEIGHT + HEIGHT/2)))
    # show frame on screen
    cv2.imshow("Frame", frame)

    # press q to end loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

