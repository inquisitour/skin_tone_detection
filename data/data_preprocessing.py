# data/data_preprocessing.py
import os
import sys

# Add the root directory to the Python path
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

# Add the DeepGaze submodule to the Python path
deepgaze_dir = os.path.join(root_dir, 'deepgaze')
sys.path.append(deepgaze_dir)

import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from config import BASE_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR, IMAGE_SIZE, SKIN_TONE_CLASSES, MIN_SKIN_RANGE, MAX_SKIN_RANGE
from deepgaze.color_detection import RangeColorDetector

def load_and_preprocess_data():
    images = []
    labels = []
    
    skin_detector = RangeColorDetector(MIN_SKIN_RANGE, MAX_SKIN_RANGE)
    
    print(f"RAW_DATA_DIR: {RAW_DATA_DIR}")
    print(f"SKIN_TONE_CLASSES: {SKIN_TONE_CLASSES}")
    
    if not os.path.exists(RAW_DATA_DIR):
        raise ValueError(f"RAW_DATA_DIR does not exist: {RAW_DATA_DIR}")
    
    for class_index, class_name in enumerate(SKIN_TONE_CLASSES):
        class_dir = os.path.join(RAW_DATA_DIR, class_name)
        print(f"Processing class: {class_name}, directory: {class_dir}")
        
        if not os.path.exists(class_dir):
            print(f"Warning: Directory does not exist: {class_dir}")
            continue
        
        image_files = [f for f in os.listdir(class_dir) if f.endswith('.jpg')]
        print(f"Found {len(image_files)} .jpg.chip files in {class_dir}")
        
        image_count = 0
        for image_name in image_files:
            image_path = os.path.join(class_dir, image_name)
            image = cv2.imread(image_path)
            if image is not None:
                # Detect skin
                skin_mask = skin_detector.returnMask(image)
                skin_image = cv2.bitwise_and(image, image, mask=skin_mask)
                
                # Resize the skin image
                skin_image = cv2.resize(skin_image, IMAGE_SIZE)
                
                images.append(skin_image)
                labels.append(class_index)
                image_count += 1
            else:
                print(f"Warning: Could not read image {image_path}")
        
        print(f"Processed {image_count} images for class {class_name}")
    
    if not images:
        raise ValueError("No images were successfully loaded and processed. Check the RAW_DATA_DIR and ensure it contains the expected subdirectories with .jpg.chip files.")
    
    images = np.array(images) / 255.0
    labels = to_categorical(np.array(labels), num_classes=len(SKIN_TONE_CLASSES))
    
    print(f"Total images processed: {len(images)}")
    print(f"Shape of images array: {images.shape}")
    print(f"Shape of labels array: {labels.shape}")
    
    X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
    
    return (X_train, y_train), (X_val, y_val), (X_test, y_test)

def save_processed_data(X_train, y_train, X_val, y_val, X_test, y_test):
    if not os.path.exists(PROCESSED_DATA_DIR):
        os.makedirs(PROCESSED_DATA_DIR)
    
    np.save(os.path.join(PROCESSED_DATA_DIR, 'X_train.npy'), X_train)
    np.save(os.path.join(PROCESSED_DATA_DIR, 'y_train.npy'), y_train)
    np.save(os.path.join(PROCESSED_DATA_DIR, 'X_val.npy'), X_val)
    np.save(os.path.join(PROCESSED_DATA_DIR, 'y_val.npy'), y_val)
    np.save(os.path.join(PROCESSED_DATA_DIR, 'X_test.npy'), X_test)
    np.save(os.path.join(PROCESSED_DATA_DIR, 'y_test.npy'), y_test)
    print("Processed data saved successfully.")

def main():
    try:
        print("Starting data preprocessing...")
        
        # Check directory structure
        print(f"Checking directory structure:")
        print(f"BASE_DIR: {BASE_DIR}")
        print(f"RAW_DATA_DIR: {RAW_DATA_DIR}")
        if os.path.exists(RAW_DATA_DIR):
            print("RAW_DATA_DIR exists.")
            for class_name in SKIN_TONE_CLASSES:
                class_dir = os.path.join(RAW_DATA_DIR, class_name)
                if os.path.exists(class_dir):
                    print(f"  - {class_name} directory exists.")
                    jpg_chip_files = [f for f in os.listdir(class_dir) if f.endswith('.jpg')]
                    print(f"    Found {len(jpg_chip_files)} .jpg files.")
                else:
                    print(f"  - {class_name} directory does not exist.")
        else:
            print("RAW_DATA_DIR does not exist.")
        
        (X_train, y_train), (X_val, y_val), (X_test, y_test) = load_and_preprocess_data()
        print(f"Training set shape: {X_train.shape}")
        print(f"Validation set shape: {X_val.shape}")
        print(f"Test set shape: {X_test.shape}")
        
        save_processed_data(X_train, y_train, X_val, y_val, X_test, y_test)
        print("Data preprocessing completed successfully.")
    except Exception as e:
        print(f"An error occurred during data preprocessing: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
