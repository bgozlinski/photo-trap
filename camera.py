import cv2


class Camera:
    """
    Class to assign camera.
    """
    def __init__(self, width, height):
        self.capture = cv2.VideoCapture(1)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.capture.set(5, 25)

    # get single frame
    def getFrame(self):
        frame = self.capture.read()[1]
        return frame
    # close camera
    def closeCamera(self):
        self.capture.release()
