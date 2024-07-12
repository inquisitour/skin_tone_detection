def analyze_prediction_script(predict_script_path):
    with open(predict_script_path, 'r') as file:
        predict_script = file.read()
    
    return {
        "handles_edge_cases": "try:" in predict_script and "except:" in predict_script,
        "uses_post_processing": "def post_process" in predict_script
    }