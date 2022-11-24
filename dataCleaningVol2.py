import pandas as pd
import string

df = pd.read_parquet('C:\\Users\\tomek\\Desktop\\tweets\\NLP-Tweets-Classification\\dataset\\dataset.parquet')

def lowercase(data):
    data['Text'] = data['Text'].str.lower()
    return data


def removeURL(data):
    data['Text'] = data['Text'].str.replace(r' *http[^ ]*', '', regex=True)
    data['Text'] = data['Text'].str.replace(r' *www[^ ]*', '', regex=True)
    return data


def removeTags(data):
    data['Text'] = data['Text'].str.replace('#', '')
    data['Text'] = data['Text'].str.replace(r' *@[^ ]*', '', regex=True)
    return data

def removePunctuation(data):
    data['Text'] = data['Text'].str.replace(r'[^\w\s]+', '', regex=True)
    data['Text'] = data['Text'].str.replace('_', '')
    
    print(data['Text'].head(40))
    return data

def removeNewLine(data):
    data['Text'] = data['Text'].str.replace('\n', ' ')
    return data


