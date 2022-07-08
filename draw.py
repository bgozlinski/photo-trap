import cv2


class Draw:

    """
    class to draw shapes.
    """

    def __init__(self, image):
        self.image = image

    # draw rectangle between x,y points.
    def rectangle(self, x, y):
        cv2.rectangle(self.image, x, y, (0, 0, 255), 2)
