import pandas as pd
import re
import matplotlib.pyplot as plt


def lowercase(data):
    data['Text'] = data['Text'].str.lower()
    return data


def extractHashtags(tweet):
    tags = re.findall(r'#[^ ]*', tweet)
    Tags.extend(tags)


df = pd.read_parquet('../../dataset/dataset.parquet')

Tags = []

df = lowercase(df)
df['Text'].apply(extractHashtags)

Tags_series = pd.Series(Tags)

Tags_series.value_counts()[:30].plot(kind='barh', figsize=(15,12))
plt.savefig('tags_bar.png')
plt.show()
