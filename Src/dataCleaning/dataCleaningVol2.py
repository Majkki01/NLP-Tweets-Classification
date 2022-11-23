import pandas as pd


def lowercase(data):
    data['Text'] = data['Text'].str.lower()
    return data


def removeURL(data):
    data['Text'] = data['Text'].str.replace(r' *http[^ ]*', '')
    data['Text'] = data['Text'].str.replace(r' *www[^ ]*', '')
    return data


def removeTags(data):
    data['Text'] = data['Text'].str.replace('#', '')
    data['Text'] = data['Text'].str.replace(r' *@[^ ]*', '')
