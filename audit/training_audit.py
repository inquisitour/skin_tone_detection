def audit_training_process(train_script_path):
    with open(train_script_path, 'r') as file:
        train_script = file.read()
    
    return {
        "uses_data_augmentation": "ImageDataGenerator" in train_script,
        "uses_early_stopping": "EarlyStopping" in train_script,
        "uses_learning_rate_scheduler": "LearningRateScheduler" in train_script
    }