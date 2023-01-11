import pandas as pd
from definitions import *
dataset = pd.read_parquet(DATA_PATH)

sampled = dataset.groupby('Label', group_keys=False).apply(lambda x: x.sample(n=625))
sampled.to_parquet(DATA_SAMPLE)