import pandas as pd
import numpy as np
import os
import torch
from transformers import BertTokenizer
import torch.nn as nn
from transformers import BertModel
from torch.optim import Adam
from tqdm import tqdm
from inputPreparation import Dataset
from bertClassifier import BertClassifier

#data_path = f'{os.path.dirname(os.path.dirname(os.getcwd()))}/dataset/'
data_path = 'C:/Users/maciejsw/OneDrive - Intel Corporation/Desktop/studia/nlp/NLP-Tweets-Classification/dataset/'
data = pd.read_parquet(f'{data_path}/dataset_clean.parquet')
data = data.head(100).sample(frac=0.1)
#splitting dataset into train set (80%), validation set (10%) and test set (10%)
data_train, data_val, data_test = np.split(data.sample(frac=1, random_state=42), [int(.8*len(data)), int(.9*len(data))])

def train(model, train_data, val_data, learning_rate, epochs):

    train, val = Dataset(train_data), Dataset(val_data)

    train_dataloader = torch.utils.data.DataLoader(train, batch_size=2, shuffle=True)
    val_dataloader = torch.utils.data.DataLoader(val, batch_size=2)

    use_cuda = torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")

    criterion = nn.CrossEntropyLoss()
    optimizer = Adam(model.parameters(), lr= learning_rate)

    if use_cuda:

            model = model.cuda()
            criterion = criterion.cuda()
    
    for epoch_num in range(epochs):

            total_acc_train = 0
            total_loss_train = 0

            for train_input, train_label in tqdm(train_dataloader):

                train_label = train_label.to(device)
                mask = train_input['attention_mask'].to(device)
                input_id = train_input['input_ids'].squeeze(1).to(device)

                output = model(input_id, mask)
                
                batch_loss = criterion(output, train_label.long())
                total_loss_train += batch_loss.item()
                
                acc = (output.argmax(dim=1) == train_label).sum().item()
                total_acc_train += acc

                model.zero_grad()
                batch_loss.backward()
                optimizer.step()
            
            total_acc_val = 0
            total_loss_val = 0

            with torch.no_grad():

                for val_input, val_label in val_dataloader:

                    val_label = val_label.to(device)
                    mask = val_input['attention_mask'].to(device)
                    input_id = val_input['input_ids'].squeeze(1).to(device)

                    output = model(input_id, mask)

                    batch_loss = criterion(output, val_label.long())
                    total_loss_val += batch_loss.item()
                    
                    acc = (output.argmax(dim=1) == val_label).sum().item()
                    total_acc_val += acc
            
            print(
                f'Epochs: {epoch_num + 1} | Train Loss: {total_loss_train / len(train_data): .3f} \
                | Train Accuracy: {total_acc_train / len(train_data): .3f} \
                | Val Loss: {total_loss_val / len(val_data): .3f} \
                | Val Accuracy: {total_acc_val / len(val_data): .3f}')

EPOCHS = 1
model = BertClassifier()
LR = 1e-6
train(model, data_train, data_val, LR, EPOCHS)

save_path = data_path + "trained_model.pt"
torch.save(model, save_path)