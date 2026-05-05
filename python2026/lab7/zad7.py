import os
import pandas as pd


BASE_DIR = os.path.dirname(__file__)
CSV_PATH = os.path.join(BASE_DIR, "..", "lab6", "data", "titanic_train.csv")

data = pd.read_csv(CSV_PATH)

print(data["Age"].min())
age_mean = data["Age"].mean()
data["Age"] = data["Age"].fillna(age_mean)
print(data.loc[[2, 4, 30], ["Age", "Name", "Sex"]])
