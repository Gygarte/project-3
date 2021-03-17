from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator

'''
Data, targets are train data

'''

def generator_builder(data, targets, TIMESTEPS):

    generator = TimeseriesGenerator(data=data,targets= targets, length=TIMESTEPS)

    return generator

