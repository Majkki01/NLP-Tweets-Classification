import torch
import pandas as pd
import numpy as np
from transformers import BertTokenizer
import os

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

labels = {'positive':0,
          'negative':1,
          'uncertainty':2,
          'litigious':3,
          }

data_path = 'C:/Users/maciejsw/OneDrive - Intel Corporation/Desktop/studia/nlp/NLP-Tweets-Classification/dataset/'
data = pd.read_parquet(f'{data_path}/dataset_clean.parquet')

class Dataset(torch.utils.data.Dataset):

    def __init__(self, data):
        self.labels = np.array([labels[label] for label in data['Label']])
        self.texts = [tokenizer(text, padding='max_length', max_length = 512, truncation=True, return_tensors="pt") for text in data['Text']]

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return self.texts[idx], self.labels[idx]

test1 = Dataset(data)
print(len(test1))