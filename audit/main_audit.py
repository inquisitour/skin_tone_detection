import os
import sys
import json
import tensorflow as tf
import logging
import argparse

# Import audit modules
from data_audit import audit_data
from model_audit import review_model_architecture
from config_audit import analyze_config
from training_audit import audit_training_process
from prediction_audit import analyze_prediction_script
from evaluation_audit import review_evaluation_metrics
from documentation_audit import audit_documentation
from integration_audit import audit_system_integration
from comparative_audit import comparative_analysis
from report_generator import generate_report

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_test_data(data_path):
    """Load actual test data instead of using random data."""
    try:
        # Replace this with actual data loading logic
        return tf.data.Dataset.load(data_path)
    except Exception as e:
        logging.error(f"Failed to load test data: {str(e)}")
        return None

def perform_audit(project_dir, config):
    audit_results = {}
    
    try:
        # 1. Data Audit
        logging.info("Starting Data Audit...")
        data_dir = os.path.join(project_dir, config['data_dir'])
        audit_results["data_audit"] = audit_data(data_dir)
        
        # 2. Model Architecture Review
        logging.info("Starting Model Architecture Review...")
        model_path = os.path.join(project_dir, config['model_path'])
        model = review_model_architecture(model_path)
        
        # 3. Configuration Analysis
        logging.info("Starting Configuration Analysis...")
        config_path = os.path.join(project_dir, config['config_file'])
        audit_results["config_analysis"] = analyze_config(config_path)
        
        # 4. Training Process Audit
        logging.info("Starting Training Process Audit...")
        train_script_path = os.path.join(project_dir, config['train_script'])
        audit_results["training_process"] = audit_training_process(train_script_path)
        
        # 5. Prediction Script Analysis
        logging.info("Starting Prediction Script Analysis...")
        predict_script_path = os.path.join(project_dir, config['predict_script'])
        audit_results["prediction_script"] = analyze_prediction_script(predict_script_path)
        
        # 6. Evaluation Metrics Review
        logging.info("Starting Evaluation Metrics Review...")
        evaluate_script_path = os.path.join(project_dir, config['evaluate_script'])
        test_data = load_test_data(config['test_data_path'])
        if test_data is not None:
            audit_results["evaluation_metrics"] = review_evaluation_metrics(evaluate_script_path, model, test_data)
        else:
            audit_results["evaluation_metrics"] = "Failed to load test data"
        
        # 7. Documentation Audit
        logging.info("Starting Documentation Audit...")
        readme_path = os.path.join(project_dir, config['readme_file'])
        audit_results["documentation"] = audit_documentation(readme_path)
        
        # 8. Overall System Integration
        logging.info("Starting Overall System Integration Audit...")
        audit_results["system_integration"] = audit_system_integration(project_dir)
        
        # 9. Comparative Analysis
        logging.info("Starting Comparative Analysis...")
        test_images = [os.path.join(project_dir, img) for img in config['test_images']]
        audit_results["comparative_analysis"] = comparative_analysis(model, test_images)
        
        # 10. Generate Report
        logging.info("Generating Audit Report...")
        report_path = os.path.join(project_dir, config['report_output'])
        generate_report(audit_results, report_path)
        
        logging.info(f"Audit completed successfully. Report saved to {report_path}")
    
    except Exception as e:
        logging.error(f"An error occurred during the audit: {str(e)}")
        sys.exit(1)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Skin Tone Detection Project Audit")
    parser.add_argument('--config', type=str, default='audit_config.json', 
                        help='Path to the audit configuration file')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    
    # Determine the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Load configuration
    config_path = os.path.join(script_dir, args.config)
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
    except Exception as e:
        logging.error(f"Failed to load configuration file: {str(e)}")
        sys.exit(1)
    
    # Use the project_directory from config, or default to parent of script directory
    project_directory = config.get('project_directory', os.path.dirname(script_dir))
    perform_audit(project_directory, config)