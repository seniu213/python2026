import os
import pandas as pd


BASE_DIR = os.path.dirname(__file__)
CSV_PATH = os.path.join(BASE_DIR, "..", "lab6", "data", "titanic_train.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "titanic_under_25_pclass2.csv")

data = pd.read_csv(CSV_PATH)

selected = data[(data["Age"] < 25) & (data["Pclass"] == 2)]
print(selected)
selected.to_csv(OUTPUT_PATH, index=False)

print(data.shape[0])
data["AgeGroup"] = pd.cut(data["Age"], bins=range(0, 91, 10), right=False)
print(data.groupby(["Sex", "Pclass", "AgeGroup"]).size())
print(int(data["Survived"].sum()))
