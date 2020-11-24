import os
from glob import glob

MODEL_PATH = 'models/'
MAX_NUM_FILES = 3

models = glob(MODEL_PATH + '*.tar.gz')
if len(models) > MAX_NUM_FILES:
    for file in models[:-MAX_NUM_FILES]:
        if os.path.exists(file):
            os.remove(file)
