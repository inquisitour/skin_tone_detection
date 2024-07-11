# models/cnn_model.py
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Input
from tensorflow.keras.models import Model
from config import IMAGE_SIZE, NUM_CLASSES

def create_skin_tone_model():
    input_tensor = Input(shape=(*IMAGE_SIZE, 3))
    base_model = MobileNetV2(weights='imagenet', include_top=False, input_tensor=input_tensor)
    
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(1024, activation='relu')(x)
    predictions = Dense(NUM_CLASSES, activation='softmax')(x)
    
    model = Model(inputs=input_tensor, outputs=predictions)
    return model

if __name__ == "__main__":
    model = create_skin_tone_model()
    model.summary()