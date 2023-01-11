import torch
from transformers import BertTokenizer
import pandas as pd
import numpy as np
from clean_tweet import run_cleaning_pipeline

def predict_sentiment(tweet: str):

    labels_list = ['positive', 'negative', 'uncertainty', 'litigious']

    tokenizer = BertTokenizer.from_pretrained('bert-base-cased')

    model_path = 'dataset/trained_model.pt'
    model = torch.load(model_path)
    model.eval()

    tweet_series = pd.DataFrame({'Text': [tweet]})
    tweet_clean = run_cleaning_pipeline(tweet_series)['Text'][0]

    tensors = tokenizer(tweet_clean, padding='max_length', max_length = 512, truncation=True, return_tensors="pt")

    input_ids = tensors['input_ids'].to('cpu')
    attention_mask = tensors['attention_mask'].to('cpu')

    output = model(input_ids, attention_mask)
    _, prediction = torch.max(output, dim=1)

    return labels_list[prediction[0]]
