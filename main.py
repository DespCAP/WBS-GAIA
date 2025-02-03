import pandas as pd
from load import mark_data
from train import split
from parameters import instruct
import pickle

if instruct.load_data:
    # Load previously marked data
    dt = pd.read_csv('marked\marked_data.csv')
else:
    # Mark data
    dt = mark_data(save_data=True)
    
if instruct.load_models:
    # Load models
    with open('raw_models.pkl', 'rb') as f:
        loaded_models = pickle.load(f)
    # Load the SMOTE models
    with open('re_models_smote.pkl', 'rb') as f:
        smote_loaded_models = pickle.load(f)

else:
    # Train ML model(s)
    X_train, X_test, y_train, y_test = split()