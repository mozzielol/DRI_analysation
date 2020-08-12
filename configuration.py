

class Configuration:
    def __init__(self):
        pass

    @property
    def path_clinical_flag(self):
        return '/Users/mozzie/Desktop/DATA/covirus/raw_data/tihmdri/DRI_May/Flags.csv'

    @property
    def path_patient_data(self):
        return '/Users/mozzie/Desktop/DATA/covirus/raw_data/tihmdri/DRI_May/Patients.csv'

    @property
    def path_observation_data(self):
        return '/Users/mozzie/Desktop/DATA/covirus/raw_data/tihmdri/DRI_May/Observations.csv'


Conf = Configuration()