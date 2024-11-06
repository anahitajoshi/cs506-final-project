import pandas as pd
import requests
import time

API_KEY = "42373efc"
BASE_URL = "http://www.omdbapi.com/"

movies_df = pd.read_csv("./data/opening-box-office.csv", encoding="ISO-8859-1")
movies_df = movies_df[movies_df["Year"] >= 2010]

movies_df = movies_df.head(200)


def fetch_movie_data(movie_title, release_year):
    params = {"t": movie_title, "y": int(release_year), "apikey": API_KEY}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if data.get("Response") == "True":
            box_office = data.get("BoxOffice", "N/A")
            rating = data.get("imdbRating", "N/A")
            genre = data.get("Genre", "N/A")
            return box_office, rating, genre
        else:
            print(f"No data found for {movie_title} ({release_year})")
            return None, None, None
    else:
        print(
            f"Error fetching data for {movie_title} ({release_year}), status code: {response.status_code}"
        )
        return None, None, None


lifetime_revenues = []
ratings = []
genres = []

for index, row in movies_df.iterrows():
    title = row["Film"]
    year = row["Year"]
    budget = row["Budget"]

    print(f"Fetching data for {title} ({year})...")
    box_office, rating, genre = fetch_movie_data(title, year)
    lifetime_revenues.append(box_office)
    ratings.append(rating)
    genres.append(genre)

    time.sleep(1)

movies_df["Lifetime_Revenue"] = lifetime_revenues
movies_df["Rating"] = ratings
movies_df["Genre"] = genres

final_df = movies_df[["Film", "Rating", "Budget", "Genre", "Lifetime_Revenue"]]
final_df.columns = [
    "Title",
    "Rating",
    "Budget",
    "Genre",
    "Lifetime_Revenue",
]

final_df.to_csv("./data/updated_movies_data.csv", index=False)

print("Data fetching and CSV update complete.")
