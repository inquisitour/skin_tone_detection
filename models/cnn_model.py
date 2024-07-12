# models/cnn_model.py
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Input, Dropout, BatchNormalization
from tensorflow.keras.models import Model
from tensorflow.keras.regularizers import l2
from config import IMAGE_SIZE, NUM_CLASSES

def create_skin_tone_model(fine_tune=True):
    input_tensor = Input(shape=(*IMAGE_SIZE, 3))
    
    # Using EfficientNetB0 as the base model
    base_model = EfficientNetB0(weights='imagenet', include_top=False, input_tensor=input_tensor)
    
    # Freeze the base model layers
    base_model.trainable = False
    
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = BatchNormalization()(x)
    x = Dropout(0.5)(x)
    x = Dense(512, activation='relu', kernel_regularizer=l2(0.01))(x)
    x = BatchNormalization()(x)
    x = Dropout(0.3)(x)
    x = Dense(256, activation='relu', kernel_regularizer=l2(0.01))(x)
    x = BatchNormalization()(x)
    predictions = Dense(NUM_CLASSES, activation='softmax')(x)
    
    model = Model(inputs=input_tensor, outputs=predictions)
    
    if fine_tune:
        # Unfreeze the top layers of the base model
        for layer in base_model.layers[-20:]:
            layer.trainable = True
    
    return model

if __name__ == "__main__":
    model = create_skin_tone_model()
    model.summary()
