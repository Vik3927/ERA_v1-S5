# ERA_v1-S5
This project trains a neural network on the MNIST dataset using PyTorch.

## Project Structure

The project is structured as follows:

- `model.py`: Contains the definition of the custom model.
- `utils.py`: Contains utility functions for data loading, training, and evaluation.
- `MNIST_build_and_train.ipynb`: Provides step by step insight into the pipeline and a playground to train the model on and experiment with it.

## Requirements

- Python (>=3.6)
- PyTorch (>=1.9)
- torchvision (>=0.10)

## Installation

1. Clone the repository:

`git clone https://github.com/Vik3927/ERA_v1-S5.git`

2. Install the required dependencies:

`pip install torch torchvision`



## Usage

1. Set the desired configurations in `utils.py`, such as batch size, learning rate, and number of epochs.

2. Run the training script:
`python utils.py`

3. The training will start, and you will see the loss for each epoch printed in the console. After training, the script will display the test accuracy.

## License

This project is licensed under No License and is free to be used and experimented with.

## Acknowledgements

This project is an assignment for The School of AI and drew its inspiration from Pytorch, MNIST dataset and the goal of scoring 400 points on this assignment.

## Contributing

Contributions and corrections are welcome! If you find any issues, please create a GitHub issue.

## Contact

For any questions or inquiries, feel free to contact [vikrantsinghchatole@gmail.com](mailto:vikrantsinghchatole@gmail.com).