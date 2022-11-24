import os
from dataCleaningVol2 import *


#to be changed
data_path = f'{os.path.dirname(os.path.dirname(os.getcwd()))}/dataset/' 
data = pd.read_parquet(f'{data_path}/dataset.parquet')

def run_cleaning_pipeline(data):
    #to be improved
    data = lowercase(data)
    data = removeURL(data)
    data = removeNewLine(data)
    data = clean_text(data)
    return data

run_cleaning_pipeline(data).to_csv(f'{data_path}/dataset_clean.csv')
