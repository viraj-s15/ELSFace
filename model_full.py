import torch
from torch import nn

class High2Low_simple(nn.Module):
    def __init__(self):
        super(High2Low_simple, self).__init__()
        self.linear = nn.Linear(10, 1)  # This is an example. Adjust the input and output dimensions as needed.

    def forward(self, x):
        return self.linear(x)