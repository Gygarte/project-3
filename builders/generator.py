
'''
Data, targets are train data

'''

#3rd-party imports
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator

def generator_builder(data, targets, TIMESTEPS):

    generator = TimeseriesGenerator(data=data,targets= targets, length=TIMESTEPS)

    return generator

