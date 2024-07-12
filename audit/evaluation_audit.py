import numpy as np
from sklearn.metrics import confusion_matrix, classification_report

def review_evaluation_metrics(evaluate_script_path, model, test_data):
    y_true = []
    y_pred = []
    for x, y in test_data:
        y_true.extend(y.numpy())
        y_pred.extend(np.argmax(model.predict(x), axis=1))
    
    report = classification_report(y_true, y_pred, output_dict=True)
    cm = confusion_matrix(y_true, y_pred)
    
    return report, cm