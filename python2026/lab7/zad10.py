import os
import pandas as pd


BASE_DIR = os.path.dirname(__file__)
CSV_PATH = os.path.join(BASE_DIR, "..", "lab6", "data", "movies.csv")

data = pd.read_csv(CSV_PATH)
data["budget"] = pd.to_numeric(data["budget"], errors="coerce")
data["title_year"] = pd.to_numeric(data["title_year"], errors="coerce")

print(data["title_year"].dropna().astype(int).value_counts().sort_index())

most_likes = data.loc[data["movie_facebook_likes"].idxmax(), ["movie_title", "movie_facebook_likes"]]
print(most_likes)

budget_over_240 = data[data["budget"] > 240000000]
print(budget_over_240.groupby("color").size())

color_movies = data[data["color"] == "Color"]
max_color_budget = color_movies.loc[color_movies["budget"].idxmax(), ["movie_title", "budget"]]
print(max_color_budget)

pirates = data[data["movie_title"].str.contains("Pirates of the Caribbean", case=False, na=False)][["movie_title", "budget", "director_name"]]
if pirates.empty:
    print("Brak filmu Piraci z Karaibow")
else:
    print(pirates)

max_budget = data.loc[data["budget"].idxmax(), ["movie_title", "budget"]]
print(max_budget)
