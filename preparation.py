import numpy as np 
from sklearn.preprocessing import MinMaxScaler
from upload import data_upload_excell
from settings import data_file_path, data_index_name

path = data_file_path
head = data_index_name

def preprocessing():

    global path, head
    #constants
    P_TRAIN = 0.6
    P_VAL = 0.2
    P_TEST = 0.2
    
    #data importing
    data = data_upload_excell(path, head)

    #data indexing
    train_index = int(np.round(len(data) * P_TRAIN))
    val_index = int(train_index + np.round(len(data) * P_VAL))
    test_index = int(val_index + np.round(len(data) * P_TEST))

    #data splitting
    train = data[:train_index]
    val = data[train_index:val_index]
    test = data[val_index:test_index]

    #building the scaler and fitting to train sample

    scaler = MinMaxScaler()
    scaler.fit(train)

    #scaling the data
    scaled_train = scaler.fit_transform(train)
    scaled_val = scaler.fit_transform(val)
    scaled_test = scaler.fit_transform(test)

    return scaled_train, scaled_val, scaled_test, scaler

