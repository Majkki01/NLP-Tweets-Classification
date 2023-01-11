import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(ROOT_DIR, '../../dataset')

DATA_PATH = os.path.join(DATA_DIR, 'dataset_clean.parquet')

SAVE_MODEL_PATH = os.path.join(DATA_DIR, 'trained_model.pt')

DATA_SAMPLE = os.path.join(DATA_DIR, 'dataset_sample.parquet')

print(DATA_PATH)
