import pandas as pd
import os
import kagglehub

# Download latest version of dataset from Kaggle
path = kagglehub.dataset_download("darkmatternet/french-motor-tpl-claims-frequency-and-severity")

# Load datasets
df_freq = pd.read_csv(os.path.join(path, "freMTPL2freq.csv"))
df_sev = pd.read_csv(os.path.join(path, "freMTPL2sev.csv"))

print(df_sev.head())
