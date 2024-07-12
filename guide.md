# Updated Step-by-Step Guide for Skin Tone Detection Project

This guide walks you through the process of setting up, running, and evaluating the skin tone detection project that combines DeepGaze and a custom CNN model.

## 1. Environment Setup

1. Ensure you have Python 3.7+ installed on your system.
2. Clone the project repository to your local machine.
3. Navigate to the project directory in your terminal.
4. Create a virtual environment:
   ```
   python -m venv venv
   ```
5. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
6. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## 2. Data Preparation

1. Create a `data/raw` directory in your project folder if it doesn't exist.
2. Collect images for each skin tone category (black, brown, white).
3. Organize your dataset in the `data/raw` directory as follows:
   ```
   data/raw/
   ├── black/
   │   ├── image1.jpg
   │   ├── image2.jpg
   │   └── ...
   ├── brown/
   │   ├── image1.jpg
   │   ├── image2.jpg
   │   └── ...
   └── white/
       ├── image1.jpg
       ├── image2.jpg
       └── ...
   ```

## 3. Data Preprocessing

1. Review and adjust the skin detection parameters in `config.py` if necessary.
2. Run the data preprocessing script:
   ```
   python data/data_preprocessing.py
   ```
3. This script will:
   - Load images from the raw data directory
   - Use DeepGaze to detect skin areas in each image
   - Preprocess the skin-detected areas for CNN input
   - Split the data into training, validation, and test sets
4. Verify that the script runs without errors and prints the shapes of the datasets.
5. Manually inspect some preprocessed images to ensure correct skin detection.

## 4. Model Architecture

1. Review the CNN model architecture in `models/cnn_model.py`.
2. Consider starting with a simpler architecture if facing performance issues.
3. Implement data augmentation techniques in the model or data loading process.

## 5. Model Training

1. Adjust hyperparameters in `config.py` if needed (learning rates, batch size, epochs).
2. Start the model training process:
   ```
   python train.py
   ```
3. Monitor the console output for training progress, including loss and accuracy for each epoch.
4. After training, examine the generated training history plot.

## 6. Model Evaluation

1. Run the evaluation script:
   ```
   python evaluate.py
   ```
2. Review the printed classification report, which includes precision, recall, and F1-score for each class.
3. Examine the confusion matrix visualization to understand the model's performance across different skin tones.
4. If the model shows poor performance (e.g., heavy bias towards one class):
   - Check for class imbalance in your dataset
   - Review preprocessing steps for potential biases
   - Consider implementing class weighting or oversampling techniques

## 7. Improving Model Performance

If the model's performance is unsatisfactory:

1. Data Quality:
   - Ensure your dataset is diverse and correctly labeled
   - Add more varied samples if certain classes are underrepresented

2. Preprocessing:
   - Fine-tune the skin detection algorithm to reduce potential biases
   - Implement additional data augmentation techniques

3. Model Architecture:
   - Experiment with different CNN architectures
   - Consider using transfer learning with pre-trained models

4. Training Process:
   - Adjust learning rates, potentially using learning rate schedules
   - Implement regularization techniques (e.g., dropout, L2 regularization)
   - Use techniques like gradient clipping to handle potential instability

5. Balanced Learning:
   - Implement class weighting in the loss function
   - Use oversampling or undersampling techniques for imbalanced classes

6. Feature Visualization:
   - Implement techniques like activation maximization or Grad-CAM to understand what features the model is learning

## 8. Making Predictions

Once the model's performance has improved:

1. Develop a prediction script (`predict.py`) to use the trained model on new images.
2. Ensure the prediction process includes the same preprocessing steps used during training.
3. Implement a user-friendly interface for making predictions, if desired.

## 9. Iterative Improvement

Repeat steps 4-8 as necessary, making incremental improvements and re-evaluating performance until satisfactory results are achieved.

Remember to document changes, findings, and results throughout the process. This will help in understanding what works best for your specific skin tone detection task.
