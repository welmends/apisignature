from config import Config
import logging
import cv2 as cv
import numpy as np

class SigBackRemoval:
    def process_signature(self, image):
        if np.shape(image) == ():
            logging.error('Signature image is empty')
            return None

        img = image.copy()
        out = None
        try:
            img = cv.GaussianBlur(img,(5,5),0)
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            ret, img = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
            alpha = np.ones(img.shape, dtype=img.dtype)*255
            out = cv.merge((img, img, img, alpha))
            out[np.all(out == [255, 255, 255, 255], axis=2)] = [0, 0, 0, 0]
        except:
            logging.ERROR('Signature image processing failed')

        return out