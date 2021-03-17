from tensorflow.keras.callbacks import EarlyStopping

def callback_builder():

    callback = EarlyStopping(monitor="accuracy", patience= 30, restore_best_weights= True)

    return callback