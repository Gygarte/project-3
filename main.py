#!./venv/bin/activate bash
#standard library import
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import sys
import os
#3rd-party library import
from sklearn.preprocessing import MinMaxScaler
#local library import
from builders.build_tuner import tuner_builder_hyperband
from builders.build_network import builder
from builders.callback import callback_builder
from processes.preparation import preprocessing
from processes.forcast import forcast
from utils.utils import split_sequence
from utils.utils import predictor
from utils.utils import accuracy
from utils.utils import total_return
from settings.settings import epochs
from system.system import system




set_up = True #system()

if set_up == True:
    
    
    #settings

    EPOCHS = epochs

    #constants

    TIMESTEP = 5
    FEATURES = 1

    #data importing
    scaled_train, scaled_val, scaled_test, scaler = preprocessing()

    #x, y splitting
    x_train, y_train = split_sequence(scaled_train, TIMESTEP)
    x_val, y_val = split_sequence(scaled_val, TIMESTEP)
    x_test, y_test = split_sequence(scaled_test, TIMESTEP)

    callback = callback_builder()


    tuner = tuner_builder_hyperband()
    tuner.search(x_train, y_train, epochs=200,  validation_data = (x_val, y_val))

    best_hp = tuner.get_best_hyperparameters(num_trials=1)[0]

    print(f"""
    The hyperparameter search is complete. The optimal parameters are:
    --> units: {best_hp.get('units')}
    --> learning_rate: {best_hp.get('learning_rate')}
    """)

    model = tuner.hypermodel.build(best_hp)
    model.fit(x_train, y_train, epochs = 100, validation_data= (x_val, y_val))
    evaluation = model.evaluate(x_test, y_test)

    print("[test loss, test accuracy]:", evaluation)
    
    
    forcast = forcast(model, x_test)
    print(forcast)
    data = {'Forcast':forcast, 'Real':y_test.reshape(len(y_test),)}
    df = pd.DataFrame(data)
    plt.plot(df)
    plt.show()
    
    


    

   

