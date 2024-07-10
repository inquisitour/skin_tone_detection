# Skin Tone Detection

This project implements a robust skin tone detection system using deep learning techniques and the Deepgaze library.

## Setup and Installation

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix or MacOS: `source venv/bin/activate`
4. Install the required packages: `pip install -r requirements.txt`

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

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
