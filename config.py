import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DATA_DIR = os.path.join(BASE_DIR, 'data', 'raw')
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, 'data', 'processed')
SAVED_MODELS_DIR = os.path.join(BASE_DIR, 'models', 'saved_models')

IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 50
LEARNING_RATE = 0.001
NUM_CLASSES = 3
SKIN_TONE_CLASSES = ['black', 'brown', 'white']
