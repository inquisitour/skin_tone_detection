# Step-by-Step Guide for Skin Tone Detection Project

This guide will walk you through the process of setting up, running, and evaluating the skin tone detection project that combines DeepGaze and a custom CNN model.

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
   │   ├── image1.jpg.chip
   │   ├── image2.jpg.chip
   │   └── ...
   ├── brown/
   │   ├── image1.jpg.chip
   │   ├── image2.jpg.chip
   │   └── ...
   └── white/
       ├── image1.jpg.chip
       ├── image2.jpg.chip
       └── ...
   ```

## 3. Data Preprocessing

1. Run the data preprocessing script:
   ```
   python data/data_preprocessing.py
   ```
2. This script will:
   - Load images from the raw data directory
   - Use DeepGaze to detect skin areas in each image
   - Preprocess the skin-detected areas for CNN input
   - Split the data into training, validation, and test sets
3. Verify that the script runs without errors and prints the shapes of the datasets.

## 4. Model Training

1. Start the model training process:
   ```
   python train.py
   ```
2. The script will train the CNN model using the preprocessed data.
3. Monitor the console output for training progress, including loss and accuracy for each epoch.
4. The best model will be saved in the `models/saved_models` directory.

## 5. Model Evaluation

1. After training, evaluate the model's performance:
   ```
   python evaluate.py
   ```
2. This script will load the best model and evaluate it on the test set.
3. Review the printed classification report, which includes precision, recall, and F1-score for each class.
4. Examine the confusion matrix visualization to understand the model's performance across different skin tones.

## 6. Making Predictions

1. To test the model on new images, run:
   ```
   python predict.py
   ```
2. When prompted, enter the path to an image file.
3. The script will:
   - Use DeepGaze to detect skin areas in the input image
   - Apply the trained CNN model to classify the skin tone
   - Display the predicted skin tone and show a visualization of the detected skin areas

## 7. Experimenting with the Project

To experiment with the current setup:

1. **Adjust DeepGaze parameters**: Modify the skin detection threshold in `utils/image_utils.py` to see how it affects the overall system performance.

2. **Modify CNN architecture**: Experiment with different network structures in `models/cnn_model.py`.

3. **Enhance data preprocessing**: Add data augmentation techniques in `data/data_preprocessing.py` to improve model robustness.

4. **Fine-tune hyperparameters**: Adjust learning rate, batch size, or number of epochs in `config.py`.

5. **Analyze model performance**: After each training run, compare the evaluation results to understand how your changes impact the model's effectiveness across different skin tones.

6. **Test with diverse images**: Use `predict.py` with a variety of images to assess the system's performance in real-world scenarios.

Remember to document your experiments, noting any changes made and their impacts on model performance. This will help guide further improvements to the project.

## Troubleshooting

- If you encounter "module not found" errors, ensure your virtual environment is activated and all requirements are installed.
- For CUDA-related errors, verify that your TensorFlow installation is compatible with your GPU drivers.
- If you face memory issues during training, try reducing the `BATCH_SIZE` in `config.py`.

For any other issues, refer to the documentation of the libraries used (TensorFlow, OpenCV, DeepGaze) or seek help in their respective community forums.
