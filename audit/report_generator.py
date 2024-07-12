import json

def generate_report(audit_results):
    report = {
        "data_audit": audit_results["data_audit"],
        "model_architecture": "See model summary",
        "config_analysis": audit_results["config_analysis"],
        "training_process": audit_results["training_process"],
        "prediction_script": audit_results["prediction_script"],
        "evaluation_metrics": audit_results["evaluation_metrics"],
        "documentation": audit_results["documentation"],
        "system_integration": audit_results["system_integration"],
        "comparative_analysis": audit_results["comparative_analysis"]
    }
    
    with open("audit_report.json", "w") as f:
        json.dump(report, f, indent=4)
    
    print("Audit report generated: audit_report.json")