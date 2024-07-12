def audit_documentation(readme_path):
    with open(readme_path, 'r') as file:
        readme = file.read()
    
    return {
        "mentions_dataset": "dataset" in readme.lower(),
        "mentions_limitations": "limitation" in readme.lower(),
        "mentions_bias": "bias" in readme.lower(),
        "has_usage_guidelines": "usage" in readme.lower() and "guideline" in readme.lower()
    }