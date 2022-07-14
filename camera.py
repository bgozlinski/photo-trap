import cv2
from config import *


class Camera:
    """
    Class to assign camera.
    """

    def __init__(self, width, height):
        self.capture = cv2.VideoCapture(1)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.capture.set(5, FRAMERATE)

    def get_frame(self):
        # Capture frame-by-frame.
        # ret returns True if frame is successfully captured.
        ret, frame = self.capture.read()
        return frame

    @staticmethod
    def convert_to_gray_scale(rgb_frame):
        return cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2GRAY)


