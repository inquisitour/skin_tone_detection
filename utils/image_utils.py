import cv2
import numpy as np
from deepgaze.color_detection import SkinDetector
from config import IMAGE_SIZE

def preprocess_image(image):
    image = cv2.resize(image, IMAGE_SIZE)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image / 255.0

def detect_skin(image):
    skin_detector = SkinDetector()
    return skin_detector.returnSkinMask(image)
