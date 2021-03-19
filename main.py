#!./venv/bin/activate bash
#standard library import
import numpy as np
import sys
import os
#3rd-party library import
from sklearn.preprocessing import MinMaxScaler
#local library import
from builders.build_tuner import tuner_builder_hyperband
from builders.build_network import builder
from builders.callback import callback_builder
from processes.preparation import preprocessing
from utils.utils import split_sequence
from utils.utils import predictor
from utils.utils import accuracy
from utils.utils import total_return
from settings.settings import epochs
from system.system import system



set_up = system()

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
    --> _units: {best_hp.get('_units')}
    --> learning_rate: {best_hp.get('learning_rate')}
    --> layers: {best_hp.get('layers')}
    """)

    model = tuner.hypermodel.build(best_hp)
    model.fit(x_train, y_train, epochs = 500, validation_data= (x_val, y_val))
    evaluation = model.evaluate(x_test, y_test)

    print("[test loss, test accuracy]:", evaluation)


    '''
    #forcasting on test data
    perioada = 5
    test = scaler.inverse_transform(scaled_test)
    predictions = predictor(model, perioada, scaled_test, TIMESTEP)

    accuracy = accuracy(predictions[:].tolist(),test[:perioada].tolist())
    return_of_strategy = total_return(predictions[:,0].tolist(),test[:perioada, 0].tolist())
'''

   

