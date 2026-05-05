import os
import pandas as pd


BASE_DIR = os.path.dirname(__file__)
CSV_PATH = os.path.join(BASE_DIR, "..", "lab6", "data", "titanic_train.csv")

data = pd.read_csv(CSV_PATH)

print(data[data["Pclass"] == 3])
print(data[(data["Pclass"] == 2) & (data["Age"] < 30)])
print(data[(data["Sex"] == "female") & (data["Survived"] == 1)])
