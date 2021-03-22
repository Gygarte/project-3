#primary library import
import numpy as np
import pandas

def forcast(model, forcast_data):
    forcast = []
    for index in range(len(forcast_data)):
        next_in_line = np.array([forcast_data[index]])
        prediction = model.predict(next_in_line)[0,0]
        forcast.append(prediction)
    return forcast

