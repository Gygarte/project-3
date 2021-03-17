import kerastuner as kt 
from build_net import builder

def tuner_builder_hyperband():

    tuner = kt.Hyperband(hypermodel= builder, objective = "val_loss", max_epochs = 150, directory = "./tuner_data/sine_4")

    return tuner

def tuner_builder_random():
    tuner = kt.RandomSearch(hypermodel = builder , objective = "val_loss", max_trials=10, directory = "my_dir", )

    return tuner

