import importlib

def analyze_config(config_path):
    config = importlib.import_module(config_path)
    return {k: v for k, v in config.__dict__.items() if not k.startswith('__')}