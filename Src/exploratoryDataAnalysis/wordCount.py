import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from plotly import graph_objs as go
import kaleido

dataset = pd.read_parquet('dataset/dataset.parquet')

text_len = []
for text in dataset.Text:
    tweet_len = len(text.split())
    text_len.append(tweet_len)

dataset['Text_len'] = text_len
labels = dataset['Text_len'].value_counts().sort_index().index[1:11]
values = dataset['Text_len'].value_counts().sort_index().values[1:11]

layout = go.Layout(title='Count of tweets with less than 10 words')
fig = go.Figure(data=[go.Bar(x=labels, y=values)], layout=layout)
fig.show()
fig.write_image('Src/exploratoryDataAnalysis/results/fig1.png')

plt.figure(figsize=(20,20))
ax = sns.countplot(x='Text_len', data=dataset[(dataset['Text_len']<=100) & (dataset['Text_len']>10)], palette='Pastel2_r')
plt.title('Count of tweets with high number of words', fontsize=20)
plt.yticks([])
ax.bar_label(ax.containers[0])
plt.ylabel('count')
plt.xlabel('')
plt.savefig('Src/exploratoryDataAnalysis/results/fig2.png')
