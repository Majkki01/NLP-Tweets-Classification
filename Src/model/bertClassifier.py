import torch.nn as nn
from transformers import BertModel

class BertClassifier(nn.Module):

    def __init__(self, dropout=0.5):
        super(BertClassifier, self).__init__()
        self.bert = BertModel.from_pretrained('bert-base-uncased')
        self.dropout = nn.Dropout(dropout)
        self.linear = nn.Linear(self.bert.config.hidden_size, 4)
        self.relu = nn.ReLU()

    def forward(self, input_id, attention_mask):
        _, output = self.bert(input_ids= input_id, attention_mask=attention_mask)
        output = self.dropout(output)
        output = self.linear(output)
        output = self.relu(output)

        return output