import os

def audit_system_integration(project_dir):
    files = os.listdir(project_dir)
    return {
        "has_config": "config.py" in files,
        "has_train": "train.py" in files,
        "has_predict": "predict.py" in files,
        "has_evaluate": "evaluate.py" in files
    }