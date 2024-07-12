import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from sklearn.metrics import confusion_matrix, classification_report
from config import PROCESSED_DATA_DIR, SAVED_MODELS_DIR, SKIN_TONE_CLASSES

def load_test_data():
    X_test = np.load(os.path.join(PROCESSED_DATA_DIR, 'X_test.npy'))
    y_test = np.load(os.path.join(PROCESSED_DATA_DIR, 'y_test.npy'))
    return X_test, y_test

def evaluate_model():
    # Load the best model
    model = load_model(os.path.join(SAVED_MODELS_DIR, 'best_model_phase2.keras'))
    
    # Load test data
    X_test, y_test = load_test_data()
    
    # Evaluate the model
    loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
    print(f"Test accuracy: {accuracy:.4f}")
    print(f"Test loss: {loss:.4f}")
    
    # Get predictions
    y_pred = model.predict(X_test)
    y_pred_classes = np.argmax(y_pred, axis=1)
    y_true_classes = np.argmax(y_test, axis=1)
    
    # Confusion Matrix
    cm = confusion_matrix(y_true_classes, y_pred_classes)
    plt.figure(figsize=(10, 8))
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('Confusion Matrix')
    plt.colorbar()
    tick_marks = np.arange(len(SKIN_TONE_CLASSES))
    plt.xticks(tick_marks, SKIN_TONE_CLASSES, rotation=45)
    plt.yticks(tick_marks, SKIN_TONE_CLASSES)
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.savefig(os.path.join(SAVED_MODELS_DIR, 'confusion_matrix.png'))
    
    # Classification Report
    report = classification_report(y_true_classes, y_pred_classes, target_names=SKIN_TONE_CLASSES)
    print("Classification Report:")
    print(report)

if __name__ == "__main__":
    evaluate_model()
