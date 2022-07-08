import cv2
from camera import Camera
from draw import Draw

"""'320.0x240.0': 'OK'
'640.0x480.0': 'OK'
'1280.0x720.0': 'OK'"""

width = 1280
height = 720

cW = 100
cH = 100


print((int(width/2), int(height/2)), (int(width/2), int(height/2)))

initCamera = Camera(width, height)
while True:
    frame = initCamera.getFrame()
    Draw(frame).rectangle((int(width/2-cW), int(height/2 - cH)),
                          (int(cW + width/2), int(cH + height/2)))

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

Camera().closeCamera()
cv2.destroyAllWindows()



