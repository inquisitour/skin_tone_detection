import tensorflow as tf

def review_model_architecture(model_path):
    model = tf.keras.models.load_model(model_path)
    model.summary()
    return model