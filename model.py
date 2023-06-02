import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import Dataset

class Net(nn.Module):
    #This defines the structure of the NN.
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, bias = False) #in = 28x28x1, out = 26x26x32
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, bias = False) #in = n x n x 32, out = n-2 x n-2 x 64
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, bias = False) #in = n x n x 64, out = n-2 x n-2 x 128
        self.conv4 = nn.Conv2d(128, 256, kernel_size=3, bias = False) #in = n x n x 128, out = n-2 x n-2 x 256
        self.fc1 = nn.Linear(4096, 512, bias = False) # should be nn.Linear(4096,50) TODO: Try with a bigger output layer size
        self.fc2 = nn.Linear(512, 10, bias = False)  # TODO: try with a bigger input layer corresponding fc2.

    def forward(self, x):
        # 28x28x1 
        x = self.conv1(x)  #relu is being applied to height and width only, the second parameter (2 here) should be 32 to cover all the channels. TODO: test without ReLU.
        # 26x26x32
        x = F.max_pool2d(self.conv2(x), 2)
        # 12x12x64
        x = self.conv3(x)
        # 10x10x128
        x = F.max_pool2d(self.conv4(x), 2)
        # 4x4x256
        x = x.view(-1, 4096) #The value here should be (-1, 4096) TODO: Run with default parameters
        x = F.relu(self.fc1(x)) 
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)