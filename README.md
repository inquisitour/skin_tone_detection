# Skin Tone Detection

This project implements a robust and adaptive skin tone detection system using deep learning techniques in combination with the DeepGaze library.

## Setup and Installation

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix or macOS: `source venv/bin/activate`
4. Install the required packages: `pip install -r requirements.txt`

## Key Features

- Utilizes DeepGaze for initial skin detection
- Employs a CNN model for accurate skin tone classification
- Supports multiple skin tone categories (black, brown, white)

## Usage

1. Prepare your dataset in the `data/raw` directory
2. Run data preprocessing: `python data/data_preprocessing.py`
3. Train the model: `python train.py`
4. Evaluate the model: `python evaluate.py`
5. Make predictions: `python predict.py`

For detailed instructions, refer to the [Step-by-Step Guide](guide.md).

## Project Structure

- `data/`: Contains raw and processed data, along with preprocessing scripts
- `models/`: Defines the CNN model architecture
- `utils/`: Utility functions for image processing and evaluation
- `config.py`: Configuration settings for the project
- `train.py`: Script for training the model
- `predict.py`: Script for making predictions on new images
- `evaluate.py`: Script for evaluating the model's performance

## System Architecture

1. Skin Detection: DeepGaze library is used for initial skin area detection
2. Feature Extraction & Classification: Custom CNN model for skin tone classification
3. Post-processing: Combining DeepGaze skin mask with CNN predictions for final output

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

Further improvement [plan](plan.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
