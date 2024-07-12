# train.py
import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from models.cnn_model import create_skin_tone_model
from config import PROCESSED_DATA_DIR, SAVED_MODELS_DIR, BATCH_SIZE, EPOCHS, LEARNING_RATE, IMAGE_SIZE

def load_data():
    X_train = np.load(os.path.join(PROCESSED_DATA_DIR, 'X_train.npy'))
    y_train = np.load(os.path.join(PROCESSED_DATA_DIR, 'y_train.npy'))
    X_val = np.load(os.path.join(PROCESSED_DATA_DIR, 'X_val.npy'))
    y_val = np.load(os.path.join(PROCESSED_DATA_DIR, 'y_val.npy'))
    return X_train, y_train, X_val, y_val

def create_callbacks(phase):
    checkpoint = ModelCheckpoint(
        os.path.join(SAVED_MODELS_DIR, f'best_model_phase{phase}.keras'),
        save_best_only=True, 
        monitor='val_accuracy', 
        mode='max'
    )
    early_stopping = EarlyStopping(patience=10, restore_best_weights=True)
    reduce_lr = ReduceLROnPlateau(factor=0.2, patience=5, min_lr=1e-6)
    return [checkpoint, early_stopping, reduce_lr]

def train_model():
    # Load preprocessed data
    X_train, y_train, X_val, y_val = load_data()
    
    print(f"Training data shape: {X_train.shape}")
    print(f"Validation data shape: {X_val.shape}")
    
    # Create model
    model = create_skin_tone_model(fine_tune=False)
    model.compile(
        optimizer=Adam(learning_rate=LEARNING_RATE),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    # Phase 1: Training with frozen base model
    print("Phase 1: Training with frozen base model")
    history1 = model.fit(
        X_train, y_train,
        batch_size=BATCH_SIZE,
        epochs=EPOCHS // 2,
        validation_data=(X_val, y_val),
        callbacks=create_callbacks(1)
    )
    
    # Phase 2: Fine-tuning
    print("Phase 2: Fine-tuning")
    for layer in model.layers[-20:]:
        layer.trainable = True
    
    model.compile(
        optimizer=Adam(learning_rate=LEARNING_RATE / 10),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    history2 = model.fit(
        X_train, y_train,
        batch_size=BATCH_SIZE,
        epochs=EPOCHS // 2,
        validation_data=(X_val, y_val),
        callbacks=create_callbacks(2)
    )
    
    return model, (history1, history2)

def plot_training_history(history1, history2):
    # Combine histories
    acc = history1.history['accuracy'] + history2.history['accuracy']
    val_acc = history1.history['val_accuracy'] + history2.history['val_accuracy']
    loss = history1.history['loss'] + history2.history['loss']
    val_loss = history1.history['val_loss'] + history2.history['val_loss']
    
    # Plot training & validation accuracy values
    plt.figure(figsize=(12, 4))
    plt.subplot(121)
    plt.plot(acc)
    plt.plot(val_acc)
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='upper left')
    plt.axvline(x=len(history1.history['accuracy']), color='r', linestyle='--')

    # Plot training & validation loss values
    plt.subplot(122)
    plt.plot(loss)
    plt.plot(val_loss)
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='upper left')
    plt.axvline(x=len(history1.history['loss']), color='r', linestyle='--')
    
    plt.tight_layout()
    plt.savefig(os.path.join(SAVED_MODELS_DIR, 'training_history.png'))
    plt.close()

if __name__ == "__main__":
    print("Starting model training...")
    
    if not os.path.exists(SAVED_MODELS_DIR):
        os.makedirs(SAVED_MODELS_DIR)
    
    model, (history1, history2) = train_model()
    
    # Save the final model
    model.save(os.path.join(SAVED_MODELS_DIR, 'final_model.keras'))
    print("Training completed. Final model saved.")
    
    # Plot and save training history
    plot_training_history(history1, history2)
    print("Training history plot saved.")
    
    # Print final accuracy
    final_train_acc = history2.history['accuracy'][-1]
    final_val_acc = history2.history['val_accuracy'][-1]
    print(f"Final training accuracy: {final_train_acc:.4f}")
    print(f"Final validation accuracy: {final_val_acc:.4f}")
