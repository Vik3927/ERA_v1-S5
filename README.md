# S5 - modularised CNN training
This project trains a neural network on the MNIST dataset using PyTorch.

## Project Structure

The project is structured as follows:

- `model.py`: Contains the definition of the custom model.
- `utils.py`: Contains utility functions for data loading, training, and evaluation.
- `S5.ipynb`: Provides step by step insight into the pipeline and a playground to train the model on and experiment with it.

## Requirements

- Python (>=3.6)
- PyTorch (>=1.9)
- torchvision (>=0.10)

## Installation

1. Clone the repository:

        git clone https://github.com/Vik3927/S5-modularised-CNN-training.git

2. Install the required dependencies:

        pip install torch torchvision


## Usage

1. Set the desired configurations in `utils.py`, such as batch size, learning rate, and number of epochs.

2. Run the training script:
`python utils.py`

3. The training will start, and you will see the loss for each epoch printed in the console. After training, the script will display the test accuracy.


## EDA
The notebook can be used for a visual EDA on the dataset. Use `Code block 6` in the `S5.ipynb` notebook to plot multiple frames from the dataset at once.
The `num_frames` can be configured to see the desired number of frames at once.

## Train
After setting the desired configurations, there are 2 ways to train the model.
1. Simply run the following command in terminal

        python utils.py

2. Import `utils.py` as a module in your notebook using

        from utils import main
        main()

## Visualize model training performance
The model training metrics can be viewed in both forms of training. 

### For notebook training
Run the last cell after code block 9 to plot the accuracy under training.

### For training from terminal
Soon as the training is completed an image, with the same metrics, titled `metrics_accuracy.png` is stored in the directory.

## License

This project is licensed under No License and is free to be used and experimented with.

## Acknowledgements

This project is an assignment for The School of AI and drew its inspiration from Pytorch, MNIST dataset and the goal of scoring 400 points on this assignment.

## Contributing

Contributions and corrections are welcome! If you find any issues, please create a GitHub issue.

## Contact

For any questions or inquiries, feel free to contact [vikrantsinghchatole@gmail.com](mailto:vikrantsinghchatole@gmail.com).
