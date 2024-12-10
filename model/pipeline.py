import os
import pandas as pd
import numpy as np
import joblib
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

MODEL_PATH = os.path.join("model", "voting_reg.pkl")
FEATURES_PATH = os.path.join("model", "features.pkl")
HIST_DATA_PATH = os.path.join("data", "historical_movies.csv")

analyzer = SentimentIntensityAnalyzer()


def load_model_and_features():
    voting_reg = joblib.load(MODEL_PATH)
    feature_info = joblib.load(FEATURES_PATH)
    genre_cols = feature_info["genre_cols"]
    feature_cols = feature_info["feature_cols"]
    return voting_reg, genre_cols, feature_cols


def load_all_genres():
    hist_df = pd.read_csv(HIST_DATA_PATH)
    hist_df["Genre"] = hist_df["Genre"].fillna("")
    hist_df["MovieGenreList"] = hist_df["Genre"].apply(
        lambda x: [g.strip() for g in str(x).split(",") if g.strip() != ""]
    )
    all_genres = set([g for glist in hist_df["MovieGenreList"] for g in glist])
    return all_genres


def get_tweet_sentiment(csv_path):
    tweets_df = pd.read_csv(csv_path)
    tweets_df["Sentiment"] = tweets_df["Content"].apply(
        lambda text: analyzer.polarity_scores(str(text))["compound"]
    )
    mean_sentiment = tweets_df["Sentiment"].mean()
    all_sentiments = tweets_df["Sentiment"].tolist()
    return mean_sentiment, all_sentiments


def predict_revenue_for_movie(
    voting_reg,
    all_genres,
    genre_cols,
    feature_cols,
    user_budget,
    user_derived_sentiment,
    user_genre,
):
    movie_data = {}
    movie_data["Budget_log"] = np.log1p(user_budget)
    movie_data["Derived_Sentiment"] = user_derived_sentiment
    movie_data["BudgetSentiment"] = (
        movie_data["Budget_log"] * movie_data["Derived_Sentiment"]
    )

    # Set genre indicators
    for g in all_genres:
        if g == user_genre:
            movie_data[f"Genre_{g}"] = 1
        else:
            movie_data[f"Genre_{g}"] = 0

    # Genre-based interactions
    for gc in genre_cols:
        movie_data[f"Budget_{gc}"] = movie_data["Budget_log"] * movie_data[gc]

    movie_features = pd.DataFrame([movie_data])[feature_cols]
    pred_log = voting_reg.predict(movie_features)[0]
    pred = np.expm1(pred_log)
    return pred


def extract_tweets_with_sentiments(csv_path, sample_size=50):
    tweets_df = pd.read_csv(csv_path)
    tweets_df["Sentiment"] = tweets_df["Content"].apply(
        lambda text: analyzer.polarity_scores(str(text))["compound"]
    )
    # Take a sample of tweets for the table
    sampled_tweets = tweets_df[["Content", "Sentiment"]].head(sample_size)
    return sampled_tweets.to_dict(orient="records")
