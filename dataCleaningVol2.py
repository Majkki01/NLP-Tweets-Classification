import pandas as pd
import re


def lowercase(data):
    data['Text'] = data['Text'].str.lower()
    return data


def removeURL(data):
    data['Text'] = data['Text'].str.replace(r' *http[^ ]*', '', regex=True)
    data['Text'] = data['Text'].str.replace(r' *www[^ ]*', '', regex=True)
    return data


# def removeTags(data):
#     data['Text'] = data['Text'].str.replace('#', '')
#     data['Text'] = data['Text'].str.replace(r' *@[^ ]*', '', regex=True)
#     return data


# def removePunctuation(data):
#     data['Text'] = data['Text'].str.replace(r'[^\w\s]+', '', regex=True)
#     data['Text'] = data['Text'].str.replace('_', '')
#     return data


def removeNewLine(data):
    data['Text'] = data['Text'].str.replace('\n', ' ')
    return data


#function produces clean text - approach to be validated 
def clean_text(data): 
    data['Text'] = data['Text'].str.replace(r'[^A-Za-z0-9\s]', '', flags=re.UNICODE, regex=True)
    return data

