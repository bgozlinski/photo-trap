import cv2


class Camera:
    def __init__(self, width, height):
        self.capture = cv2.VideoCapture(1)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.capture.set(5, 25)

    def getFrame(self):
        frame = self.capture.read()[1]
        return frame

    def closeCamera(self):
        self.capture.release()
