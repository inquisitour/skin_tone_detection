import os
import cv2
from collections import Counter

def audit_data(data_dir):
    class_counts = Counter()
    image_quality = {}
    
    for class_name in os.listdir(data_dir):
        class_dir = os.path.join(data_dir, class_name)
        if not os.path.isdir(class_dir):
            continue
        
        image_quality[class_name] = Counter()
        for image_name in os.listdir(class_dir):
            if image_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(class_dir, image_name)
                quality = analyze_image_quality(image_path)
                image_quality[class_name][quality] += 1
                if quality == "good":
                    class_counts[class_name] += 1
    
    return class_counts, image_quality

def analyze_image_quality(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return "corrupt"
    
    if image.shape[0] < 100 or image.shape[1] < 100:
        return "low_resolution"
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if cv2.meanStdDev(gray)[1][0][0] < 20:
        return "low_contrast"
    
    return "good"