import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from config import SAVED_MODELS_DIR, IMAGE_SIZE, SKIN_TONE_CLASSES

def preprocess_image(image_path):
    img = load_img(image_path, target_size=IMAGE_SIZE)
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

def predict_skin_tone(image_path):
    model = load_model(os.path.join(SAVED_MODELS_DIR, 'best_model_phase2.keras'))
    processed_image = preprocess_image(image_path)
    prediction = model.predict(processed_image)
    predicted_class = SKIN_TONE_CLASSES[np.argmax(prediction)]
    confidence = np.max(prediction)
    return predicted_class, confidence

if __name__ == "__main__":
    image_path = input("Enter the path to the image: ")
    predicted_class, confidence = predict_skin_tone(image_path)
    print(f"Predicted skin tone: {predicted_class}")
    print(f"Confidence: {confidence:.2f}")
