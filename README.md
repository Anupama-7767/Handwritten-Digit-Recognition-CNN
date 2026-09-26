# Handwritten Digit Recognition CNN

A small Streamlit application that recognizes handwritten digits from 0 to 9. Draw a digit on the canvas and the app uses a trained TensorFlow/Keras convolutional neural network to display its prediction and confidence.

## Project Contents

```text
.
|-- app.py
|-- mnist_cnn.keras
|-- requirement.txt
|-- data/
|   |-- mnist_train.csv
|   `-- mnist_test.csv
`-- notebook/
	`-- mnist_CNN.ipynb
```

The trained model file `mnist_cnn.keras` must remain in the project root because `app.py` loads it when the application starts. The CSV files are used by the training notebook.

## Setup

Use a Python version supported by TensorFlow 2.21.0. From the project root, create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirement.txt
```

## Run the App

From the project root, run:

```powershell
streamlit run app.py
```

Open the local URL printed by Streamlit, draw a digit, and select **Predict**.

## Training Notebook

Open `notebook/mnist_CNN.ipynb` in Jupyter or VS Code. The notebook currently reads the CSV files from an absolute path on the original author's computer. Before running it on another machine, update those two `read_csv` paths to `data/mnist_train.csv` and `data/mnist_test.csv` (relative to the project root).
