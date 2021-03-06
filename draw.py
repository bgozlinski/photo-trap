import cv2


class Draw:

    """
    class to draw shapes.
    """

    def __init__(self, image):
        self.image = image

    def rectangle(self, x, y):
        # draw rectangle between x,y points
        cv2.rectangle(self.image, x, y, (0, 0, 255), 1)

    def circle(self, center, r):
        # draw circle in center_coordinates and radius
        cv2.circle(self.image, center, r, (255, 0, 0), 5)
