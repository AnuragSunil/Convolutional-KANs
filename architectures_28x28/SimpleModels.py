from torch import nn
import sys
import torch.nn.functional as F

# directory reach
# sys.path.append('../kan_convolutional')

class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 5, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(5, 5, kernel_size=3, padding=1)

        self.maxpool = nn.MaxPool2d(kernel_size=2)
        
        self.flatten = nn.Flatten()
        self.fc = nn.Linear(245, 10)
        self.name = "CNN (Small)"

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.maxpool(x)
        x = F.relu(self.conv2(x))
        x = self.maxpool(x)
        x = self.flatten(x)
        x = self.fc(x)
        x = F.log_softmax(x, dim=1)

        return x
    
class newSmallCNN(nn.Module):
    def __init__(self):
        super(newSmallCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 5, kernel_size=3, padding=(0, 0))
        self.conv2 = nn.Conv2d(5, 25, kernel_size=3, padding=(0, 0))

        self.maxpool = nn.MaxPool2d(kernel_size=2)
        
        self.flatten = nn.Flatten()
        self.fc = nn.Linear(625, 10)
        self.name = "New CNN (Small)"

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.maxpool(x)
        x = F.relu(self.conv2(x))
        x = self.maxpool(x)
        x = self.flatten(x)
        x = self.fc(x)
        x = F.log_softmax(x, dim=1)
        return x
class newMediumCNN(newSmallCNN):
    pass
class SimpleCNN_2(nn.Module):
    def __init__(self):
        super(SimpleCNN_2, self).__init__()
        self.conv1 = nn.Conv2d(1, 5, kernel_size=3, padding=0)
        self.conv2 = nn.Conv2d(5, 25, kernel_size=3, padding=0)

        self.maxpool = nn.MaxPool2d(kernel_size=2)
        
        self.flatten = nn.Flatten()
        self.fc = nn.Linear(625, 245)
        self.fc2 = nn.Linear(245, 10)
        self.name = "CNN (Medium)"

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.maxpool(x)
        x = F.relu(self.conv2(x))
        x = self.maxpool(x)
        x = self.flatten(x)
        x = self.fc(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.log_softmax(x, dim=1)
        return x

class SimpleLinear(nn.Module):
    def __init__(self):
        super(SimpleLinear, self).__init__()
        # Definir una sola capa lineal con 'input_features' entradas y 10 salidas
        self.linear = nn.Linear(28*28, 10)
        self.flatten = nn.Flatten()
        self.name = "1 Layer MLP"


    def forward(self, x):
        # Pasar los datos a través de la capa lineal
        x = self.flatten(x)
        x = self.linear(x)
        x = F.log_softmax(x, dim=1)

        return x
class CNN_deeper(nn.Module):
    def __init__(self):
        super(CNN_deeper, self).__init__()
        self.conv1 = nn.Conv2d(1, 5, kernel_size=3, padding=(0, 0))
        self.conv2 = nn.Conv2d(5, 25, kernel_size=3, padding=(0, 0))
        self.conv3 = nn.Conv2d(25, 25*5, kernel_size=2, padding=(0, 0))

        self.maxpool = nn.MaxPool2d(kernel_size=2)
        
        self.flatten = nn.Flatten()
        self.fc = nn.Linear(4*125, 10)
        self.name = "CNN 3 Conv layers & 1 MLP"

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.maxpool(x)
        x = F.relu(self.conv2(x))
        x = self.maxpool(x)
        x = F.relu(self.conv3(x))
        x = self.maxpool(x)
        x = self.flatten(x)
        x = self.fc(x)
        x = F.log_softmax(x, dim=1)
        return x