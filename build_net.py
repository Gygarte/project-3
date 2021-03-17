from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import Adam


def builder (hp):

    #hyperparameters
    units = hp.Int("units", min_value = 1, max_value = 100, step = 15)
    _units = hp.Int("_units", min_value = 1, max_value = 100, step = 15)
    learning_rate = hp.Choice("learning_rate",values=[1e-2, 1e-3, 1e-4])
    layers = hp.Int('layers', min_value=1, max_value=10, step=1)
    #drop = hp.Choice('drop', values=[0.10,0.25,0.5,0.65])
    #_drop = hp.Choice('_drop', values=[0.10,0.25,0.5,0.65])

    #model
    model = Sequential()
    model.add(LSTM(units= units , input_shape=(5,1), return_sequences=True , dropout=0.1))

    for layer in range(layers):
        model.add(LSTM(_units,return_sequences=True, dropout=0.65 ))
    model.add(Dense(units= 1,activation="sigmoid"))

    model.compile(optimizer = Adam(learning_rate = learning_rate), loss = "mse", metrics= ['accuracy'])

    return model
