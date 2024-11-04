import pandas as pd
import requests
import time

# OMDb API Key and Base URL
API_KEY = "42373efc"
BASE_URL = "http://www.omdbapi.com/"

# Load the dataset and filter for movies released after 2010
movies_df = pd.read_csv("./data/opening-box-office.csv", encoding="ISO-8859-1")
movies_df = movies_df[movies_df["Year"] >= 2010]

# Limit to a specific number if necessary (e.g., 200 movies)
movies_df = movies_df.head(200)


# Define a function to fetch movie data (lifetime box office, rating, genre) from OMDb API
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


# Prepare lists to store the results
lifetime_revenues = []
ratings = []
genres = []

# Fetch data for each movie
for index, row in movies_df.iterrows():
    title = row["Film"]
    year = row["Year"]
    budget = row["Budget"]  # Use the budget from the CSV

    print(f"Fetching data for {title} ({year})...")
    box_office, rating, genre = fetch_movie_data(title, year)
    lifetime_revenues.append(box_office)
    ratings.append(rating)
    genres.append(genre)

    # Respect API rate limits
    time.sleep(1)

# Add the fetched data to the DataFrame
movies_df["Lifetime_Revenue"] = lifetime_revenues
movies_df["Rating"] = ratings
movies_df["Genre"] = genres

# Keep only the necessary columns: title, rating, budget, genre, lifetime revenue
final_df = movies_df[["Film", "Rating", "Budget", "Genre", "Lifetime_Revenue"]]
final_df.columns = [
    "Title",
    "Rating",
    "Budget",
    "Genre",
    "Lifetime_Revenue",
]  # Rename columns for clarity

# Save to a new CSV file
final_df.to_csv("./data/updated_movies_data.csv", index=False)

print("Data fetching and CSV update complete.")
