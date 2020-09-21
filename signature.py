import cv2 as cv
import numpy as np

class SigBackRemoval:
    def __init__(self):
        return

    def process_signature(self, img):
        img = cv.GaussianBlur(img,(5,5),0)
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        ret, img = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
        alpha = np.ones(img.shape, dtype=img.dtype)*255
        out = cv.merge((img, img, img, alpha))
        out[np.all(out == [255, 255, 255, 255], axis=2)] = [0, 0, 0, 0]
        return out