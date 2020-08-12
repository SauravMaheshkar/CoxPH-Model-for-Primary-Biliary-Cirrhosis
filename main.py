## Importing Packages ##
import os
import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from lifelines import CoxPHFitter
from lifelines.utils import concordance_index as cindex

def predict(dataframe): 
    """
    Function for returning the expected lifetime based on the Input Data
    """

    ## Loading the Dataset ##
    input_path = "input/"
    df = pd.read_csv(os.path.join(input_path, "pbc.csv"))

    ## Some Pre-Processing ## 
    for i in df.index:
        df.at[i, 'sex'] = 0 if df.loc[i, 'sex'] == "f" else 1

    ## Splitting the Dataset ##
    np.random.seed(0)
    df_dev, df_test = train_test_split(df, test_size = 0.2)
    df_train, df_val = train_test_split(df_dev, test_size = 0.25)

    ## Creating a encoding function ##
    def one_hot_encoder(dataframe, columns):
        return pd.get_dummies(dataframe, columns = columns, drop_first = True, dtype = np.float64)

    to_encode = ["edema","stage"]
    one_hot_train = one_hot_encoder(df_train, to_encode)
    one_hot_val = one_hot_encoder(df_val, to_encode)
    one_hot_test = one_hot_encoder(df_test, to_encode) 
    one_hot_train.dropna(inplace = True)

    ## Fitting the Model ##
    cph = CoxPHFitter()
    cph.fit(one_hot_train, duration_col = 'age', event_col = 'status', step_size=0.1)

    return cph.predict_expectation(dataframe)[0]
