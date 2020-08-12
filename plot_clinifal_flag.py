from util.load_data import load_clinical_flag
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = load_clinical_flag()

types = {
    'Diastolic': 'Diastolic blood pressure is out of range.',
    'Systolic': 'Systolic blood pressure is out of range.',
    'Pulse': 'Alert: Abnormal pulse is observed from blood pressure cuff.',
    'Body Temperature': 'High body temperature is noted.',
}

sizes = []
labels = []
for key, value in types.items():
    sizes.append(len(data.loc[data['message'].str.startswith(value)]))
    labels.append(key)

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.0, 0.0, 0.1, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

num_patients = len(np.unique(data['subject']))
data['datetimeCreated'] = pd.to_datetime(data['datetimeCreated'])
dates = sorted(list(data['datetimeCreated']))
plt.axis('equal')
plt.title('Data collected from {} Patients from {} to {}'.format(num_patients,
                                                                 str(dates[0].date()), str(dates[-1].date())))
plt.tight_layout()
plt.savefig('results/clinical_flags.png')
plt.show()
