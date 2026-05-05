import os
import pandas as pd


BASE_DIR = os.path.dirname(__file__)
CSV_PATH = os.path.join(BASE_DIR, "..", "lab6", "data", "titanic_train.csv")

data = pd.read_csv(CSV_PATH)

print(data.iloc[3:9, :3])
print(data["Age"].mean())
print(int(data["Survived"].sum()))
print(data.groupby("Sex").describe())
pclass_count = data["Pclass"].value_counts()
print(pclass_count.reindex([1, 3]).fillna(0).astype(int))
