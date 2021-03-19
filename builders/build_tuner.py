

#3rd-party imports
import kerastuner as kt 

#local imports
from .build_network import builder
from settings.settings import project_name

_project_name = project_name

def tuner_builder_hyperband():

    global _project_name

    tuner = kt.Hyperband(hypermodel= builder, objective = "val_loss", max_epochs = 150, directory = f"./tuner_data/{_project_name}")

    return tuner

def tuner_builder_random():

    global _project_name

    tuner = kt.RandomSearch(hypermodel = builder , objective = "val_loss", max_trials=10, directory = f'./tuner_data/{_project_name}', )

    return tuner

