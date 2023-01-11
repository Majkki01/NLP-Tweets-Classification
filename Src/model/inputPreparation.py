import torch
import pandas as pd
import numpy as np
from transformers import BertTokenizer
from definitions import DATA_PATH
import os

tokenizer = BertTokenizer.from_pretrained('bert-base-cased')

labels = {'positive':0,
          'negative':1,
          'uncertainty':2,
          'litigious':3,
          }

data = pd.read_parquet(DATA_PATH)

class Dataset(torch.utils.data.Dataset):

    def __init__(self, data):
        self.labels = np.array([labels[label] for label in data['Label']])
        self.texts = [tokenizer(text, padding='max_length', max_length = 512, truncation=True, return_tensors="pt") for text in data['Text']]

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return self.texts[idx], self.labels[idx]




