# train.py
import os
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from models.cnn_model import create_skin_tone_model
from data.data_preprocessing import load_and_preprocess_data
from config import SAVED_MODELS_DIR, BATCH_SIZE, EPOCHS, LEARNING_RATE

def train_model():
    (X_train, y_train), (X_val, y_val), _ = load_and_preprocess_data()
    
    model = create_skin_tone_model()
    model.compile(optimizer=Adam(learning_rate=LEARNING_RATE),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
    checkpoint = ModelCheckpoint(os.path.join(SAVED_MODELS_DIR, 'best_model.h5'),
                                 save_best_only=True, monitor='val_accuracy', mode='max')
    early_stopping = EarlyStopping(patience=10, restore_best_weights=True)
    reduce_lr = ReduceLROnPlateau(factor=0.2, patience=5, min_lr=1e-6)
    
    history = model.fit(X_train, y_train,
                        batch_size=BATCH_SIZE,
                        epochs=EPOCHS,
                        validation_data=(X_val, y_val),
                        callbacks=[checkpoint, early_stopping, reduce_lr])
    
    return model, history

if __name__ == "__main__":
    model, history = train_model()
    # Save the final model
    model.save(os.path.join(SAVED_MODELS_DIR, 'final_model.h5'))
    print("Training completed. Model saved.")
