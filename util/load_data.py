from configuration import Conf
import pandas as pd
import numpy as np


def load_clinical_flag():
    return pd.read_csv(Conf.path_clinical_flag, engine='python')


def load_patient_data():
    return pd.read_csv(Conf.path_patient_data, engine='python')

def load_observation_data():
    return pd.read_csv(Conf.path_observation_data, engine='python')

class Information():
    def __init__(self):
        pass

    @property
    def num_patients(self):
        num_patient = load_patient_data()
        return len(np.unique(num_patient['subjectId']))
