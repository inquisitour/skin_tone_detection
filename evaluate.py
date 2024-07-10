# evaluate.py
from tensorflow.keras.models import load_model
from data.data_preprocessing import load_and_preprocess_data
from utils.evaluation_utils import evaluate_model
from config import SAVED_MODELS_DIR
import os

def evaluate():
    _, _, (X_test, y_test) = load_and_preprocess_data()
    model = load_model(os.path.join(SAVED_MODELS_DIR, 'best_model.h5'))
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    evaluate()
