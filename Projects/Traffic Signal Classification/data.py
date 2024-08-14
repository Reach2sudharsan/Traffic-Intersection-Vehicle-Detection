import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms,models,datasets
import matplotlib.pyplot as plt
from PIL import Image
from torch import optim
device = 'cuda' if torch.cuda.is_available() else 'cpu'
import cv2, glob, numpy as np, pandas as pd
from glob import glob
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, Dataset
from skimage.transform import resize
import pickle

class TrafficDataset(Dataset):
    def __init__(self, file, X_size, y_size, split):
        self.file = file
        self.X_size = X_size
        self.y_size = y_size
        
        with open(self.file, 'rb') as f:
            self.data = pickle.load(f)
       
        self.X = None
        self.y = None
        if split=="train":
            self.X = self.data["x_train"]
            self.y = self.data["y_train"]
        elif split=="valid":
            self.X = self.data["x_validation"]
            self.y = self.data["y_validation"]
        elif split=="test":
            self.X = self.data["x_test"]
            self.y = self.data["y_test"]

        self.length = len(self.X)
    
    def __len__(self):
        return self.length

    def __getitem__(self, ix):
        image = self.X[ix]
        image_resized = resize(image, (3, self.X_size, self.y_size))
        return torch.tensor(image_resized).float().to(device), torch.tensor(self.y[ix]).float().to(device)

def get_data():
    file = "../../datasets/traffic_signs_preprocessed/data3.pickle"
    X_size = 224
    y_size = 224
    
    train = TrafficDataset(file, X_size, y_size, "train")
    train_dl = DataLoader(train, batch_size=32, shuffle=True, drop_last=True)

    val = TrafficDataset(file, X_size, y_size, "valid")
    val_dl = DataLoader(val, batch_size=32, shuffle=True, drop_last=True)

    return train_dl, val_dl