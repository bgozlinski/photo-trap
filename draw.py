import cv2


class Draw:
    def __init__(self, image):
        self.image = image

    def rectangle(self, x, y):
        cv2.rectangle(self.image, x, y, (0, 0, 255), 2)
