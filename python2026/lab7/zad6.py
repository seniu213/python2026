import os
import pandas as pd


BASE_DIR = os.path.dirname(__file__)
CSV_PATH = os.path.join(BASE_DIR, "..", "lab6", "data", "titanic_train.csv")

data = pd.read_csv(CSV_PATH)

print(data.loc[5])
print(data.loc[5:10])
print(data.loc[5, "Name"])
print(data.iloc[1])
print(data.iloc[5:10])
print(data.iloc[5, 3])
