import cv2
import numpy as np

def comparative_analysis(model, test_images):
    results = {}
    for image_path in test_images:
        image = cv2.imread(image_path)
        image = cv2.resize(image, (224, 224))  # Adjust size as needed
        image = image / 255.0  # Normalize
        prediction = model.predict(np.expand_dims(image, axis=0))
        results[image_path] = np.argmax(prediction)
    return results