import cv2
from camera import Camera
from draw import Draw
from config import *

# initiate camera
initCamera = Camera(WIDTH, HEIGHT)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_upperbody.xml")

while True:
    # get frame
    frame = initCamera.get_frame()
    # convert frame form RGB colors to gray scale
    gray = initCamera.convert_to_gray_scale(frame)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    # draw rectangle in centre of (WIDTH, HEIGHT) with (dW, dH) lengths
    # Draw(frame).rectangle((int(WIDTH/2-DISTANCE_WIDTH/2), int(HEIGHT/2 - DISTANCE_HEIGHT/2)),
    #                       (int(DISTANCE_WIDTH + WIDTH/2), int(DISTANCE_HEIGHT + HEIGHT/2)))
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    bodies = body_cascade.detectMultiScale(gray, 1.3, 4)

    for x, y, w, h in bodies:
        # circle_center = (x + w // 2, y + h // 2)
        # Draw(frame).circle(circle_center, w // 2)
        Draw(frame).rectangle((x, y), (x+w, y+h))
    # show frame on screen
    cv2.imshow("frame", frame)
    # cv2.imshow("gray", gray)

    # press q to end loop
    if cv2.waitKey(1) & 0xFF == ord('q'):

        break
