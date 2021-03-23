import numpy as np
'''

Useful functions for preprocessing and evaluation

'''

def split_sequence(sequence, steps):
    X, y = list(), list()
    for index in range(len(sequence)):
        #find the end of the pattern
        end_index = index + steps
        #check if we are beyond the sequence
        if end_index > len(sequence) - 1:
            break
        seq_x, seq_y = sequence[index:end_index], sequence[end_index]
        X.append(seq_x)
        y.append(seq_y)

    return np.array(X), np.array(y)

def accuracy(predictions, test):
    _count = 0
    for index in range(len(predictions)):
        if predictions[index] > 0 and test[index] > 0:
            _count += 1
        if predictions[index] < 0 and test[index] < 0:
            _count += 1
    _accuracy = (_count/len(predictions)) * 100
    return _accuracy

def total_return(predictions, test):
    _sum = 0
    for index in range(len(predictions)):
        if predictions[index] > 0 and test[index] > 0:
            _sum += test[index]
        elif predictions[index] > 0 and test[index] < 0:
            _sum += test[index]
        elif predictions[index] < 0 and test[index] < 0:
            _sum -= test[index]
        else:
            _sum -= test[index]
    return _sum

def predictor(model,period,test_series, TIMESTEP):
    
    batch = np.array([test_series[-TIMESTEP:]])
    predictions = []
    for index in range(period):
        predicted_value= model.predict(batch)[0]
        predictions.append(predicted_value)
        batch = np.append(batch[:,1:,:],[predicted_value],axis=1)
        
    return np.array(predictions)