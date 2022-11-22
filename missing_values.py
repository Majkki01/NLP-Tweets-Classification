import pandas as pd
import matplotlib.pyplot as plt

# Reading data from csv
dataset = pd.read_csv('dataset.csv')

# Bar plot of missing values
nulls = dataset.isnull().sum().sort_values(ascending=False)
nulls.plot(
    kind='bar', figsize=(13, 10))
plt.title('Missing values in the dataset')
plt.xlabel('Column title')
plt.ylabel('Number of missing values')
plt.show()

# Filtering dataset
dataset['Language'].value_counts().head(20)
df_eng = dataset[dataset['Language'] == 'en'].reset_index(drop=True)

