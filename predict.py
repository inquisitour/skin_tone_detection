# predict.py
import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from utils.image_utils import preprocess_image, detect_skin
from config import SAVED_MODELS_DIR, SKIN_TONE_CLASSES

def predict_skin_tone(image_path):
    model = load_model(os.path.join(SAVED_MODELS_DIR, 'best_model.h5'))
    
    image = cv2.imread(image_path)
    original_image = image.copy()
    
    skin_mask = detect_skin(image)
    
    preprocessed_image = preprocess_image(image)
    prediction = model.predict(np.expand_dims(preprocessed_image, axis=0))[0]
    predicted_class = SKIN_TONE_CLASSES[np.argmax(prediction)]
    
    # Visualization
    skin_tone_image = np.zeros_like(original_image)
    skin_tone_color = {
        'black': (0, 0, 0),
        'brown': (0, 128, 128),
        'white': (255, 255, 255)
    }[predicted_class]
    
    skin_tone_image[skin_mask > 0] = skin_tone_color
    
    return predicted_class, skin_tone_image

if __name__ == "__main__":
    image_path = input("Enter the path to the image: ")
    predicted_class, skin_tone_image = predict_skin_tone(image_path)
    print(f"Predicted skin tone: {predicted_class}")
    cv2.imshow("Skin Tone Detection", skin_tone_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
