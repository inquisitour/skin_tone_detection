# data/data_preprocessing.py
import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from config import RAW_DATA_DIR, PROCESSED_DATA_DIR, IMAGE_SIZE, SKIN_TONE_CLASSES

def load_and_preprocess_data():
    images = []
    labels = []
    
    for class_index, class_name in enumerate(SKIN_TONE_CLASSES):
        class_dir = os.path.join(RAW_DATA_DIR, class_name)
        for image_name in os.listdir(class_dir):
            if image_name.endswith('.jpg.chip'):  # Make sure processing the correct files
                image_path = os.path.join(class_dir, image_name)
                image = cv2.imread(image_path)
                if image is not None:
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    image = cv2.resize(image, IMAGE_SIZE)
                    images.append(image)
                    labels.append(class_index)
                else:
                    print(f"Warning: Could not read image {image_path}")
    
    images = np.array(images) / 255.0
    labels = to_categorical(np.array(labels), num_classes=len(SKIN_TONE_CLASSES))
    
    X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
    
    return (X_train, y_train), (X_val, y_val), (X_test, y_test)

if __name__ == "__main__":
    (X_train, y_train), (X_val, y_val), (X_test, y_test) = load_and_preprocess_data()
    print(f"Training set shape: {X_train.shape}")
    print(f"Validation set shape: {X_val.shape}")
    print(f"Test set shape: {X_test.shape}")