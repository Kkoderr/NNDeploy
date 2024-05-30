import os
import pandas as pd
import pickle 

from src.config import config

def load_datasets(file_name):

    file_path = os.path.join(config.DATAPATH, file_name)