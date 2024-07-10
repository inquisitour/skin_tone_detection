
# Contributing to Skin Tone Detection Project

Thank you for considering contributing to the Skin Tone Detection Project! We welcome contributions in the form of bug reports, feature requests, code, documentation, and more. This guide will help you understand our contribution process.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How Can I Contribute?](#how-can-i-contribute)
   - [Reporting Bugs](#reporting-bugs)
   - [Suggesting Enhancements](#suggesting-enhancements)
   - [Submitting Pull Requests](#submitting-pull-requests)
3. [Development Process](#development-process)
4. [Style Guide](#style-guide)
5. [License](#license)

## Code of Conduct

This project adheres to the Contributor Covenant Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to [deshmukhpratik931@gmail.com].

## How Can I Contribute?

### Reporting Bugs

If you encounter a bug in the project, please help us by reporting it. Use the following steps:

1. Ensure the bug was not already reported by searching on the [issues page](https://github.com/inquisitour/skin_tone_detection/issues).
2. If you're unable to find an open issue addressing the problem, [open a new one](https://github.com/inquisitour/skin_tone_detection/issues/new).
3. Be sure to include:
   - A descriptive title.
   - A detailed description of the bug.
   - Steps to reproduce the bug.
   - Any relevant logs, screenshots, or additional context.

### Suggesting Enhancements

If you have an idea to improve the project, we'd love to hear it! To suggest an enhancement:

1. Check if the feature request already exists on the [issues page](https://github.com/inquisitour/skin_tone_detection/issues).
2. If not, [create a new issue](https://github.com/inquisitour/skin_tone_detection/issues/new) and provide:
   - A clear and descriptive title.
   - A detailed description of the proposed enhancement.
   - Any supporting material or context.

### Submitting Pull Requests

We welcome and appreciate your pull requests. Follow these steps to submit one:

1. Fork the repository to your own GitHub account.
2. Clone the project to your local machine:
   ```
   git clone https://github.com/inquisitour/skin_tone_detection.git
   ```
3. Create a new branch for your changes:
   ```
   git checkout -b feature/your-feature-name
   ```
4. Make your changes and commit them:
   ```
   git commit -m 'Add feature description'
   ```
5. Push your changes to your forked repository:
   ```
   git push origin feature/your-feature-name
   ```
6. Open a pull request on the original repository. In your pull request, provide:
   - A clear title.
   - A detailed description of your changes.
   - Any related issue numbers (e.g., "Fixes #123").

## Development Process

1. Ensure you have Python 3.7+ installed.
2. Set up your development environment:
   - Create a virtual environment: `python -m venv venv`
   - Activate the virtual environment:
     - Windows: `venv\Scripts\activate`
     - Unix or macOS: `source venv/bin/activate`
   - Install dependencies: `pip install -r requirements.txt`
3. Run tests to verify your changes:
   ```
   python -m unittest discover tests
   ```

## Style Guide

Please adhere to the following style guidelines for your contributions:

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code.
- Write clear, concise, and descriptive commit messages.
- Use meaningful variable and function names.
- Add comments and documentation where necessary to explain your code.

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.
