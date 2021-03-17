import pandas as pd 
import numpy as np 

'''

Upload from diffrent file type to a matrix

Return a matrix 
'''

def data_upload_csv(path, index_col):
    _data = pd.read_csv(path, index_col=index_col)

    return np.array(_data)

def data_upload_excell(path, index_col):
    _data = pd.read_excel(path, index_col=index_col, )

    return np.array(_data)