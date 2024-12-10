import os
import pandas as pd
import numpy as np
from model.pipeline import (
    load_model_and_features,
    get_tweet_sentiment,
    predict_revenue_for_movie,
    extract_tweets_with_sentiments,
)


def test_load_model_and_features():
    voting_reg, genre_cols, feature_cols = load_model_and_features()
    assert voting_reg is not None, "Model failed to load"
    assert isinstance(genre_cols, list), "Genre columns should be a list"
    assert isinstance(feature_cols, list), "Feature columns should be a list"


def test_get_tweet_sentiment():
    # Create a mock tweets CSV
    mock_data = pd.DataFrame(
        {
            "Content": ["I love this movie!", "It was terrible", "An average film"],
        }
    )
    mock_csv = "mock_tweets.csv"
    mock_data.to_csv(mock_csv, index=False)

    mean_sentiment, all_sentiments = get_tweet_sentiment(mock_csv)
    os.remove(mock_csv)

    assert isinstance(mean_sentiment, float), "Mean sentiment should be a float"
    assert len(all_sentiments) == len(
        mock_data
    ), "Sentiment scores not matching number of tweets"


def test_predict_revenue_for_movie():
    voting_reg, genre_cols, feature_cols = load_model_and_features()
    all_genres = {"Horror", "Comedy", "Action"}  # Mock genres

    # Mock feature keys based on genre_cols
    movie_data = {f"Genre_{g}": 0 for g in all_genres}
    movie_data.update({"Budget_log": 0, "Derived_Sentiment": 0, "BudgetSentiment": 0})

    # Ensure all genre columns in feature_cols are mocked
    for col in genre_cols:
        if col not in movie_data:
            movie_data[col] = 0

    # Add interaction terms
    for gc in genre_cols:
        movie_data[f"Budget_{gc}"] = 0

    # Test with valid inputs
    revenue = predict_revenue_for_movie(
        voting_reg,
        all_genres,
        genre_cols,
        feature_cols,
        user_budget=25000000,
        user_derived_sentiment=0.5,
        user_genre="Horror",
    )
    assert revenue > 0  # Revenue should be positive for valid inputs


def test_extract_tweets_with_sentiments():
    # Create a mock tweets CSV
    mock_data = pd.DataFrame(
        {
            "Content": ["Tweet 1", "Tweet 2", "Tweet 3", "Tweet 4", "Tweet 5"],
        }
    )
    mock_csv = "mock_tweets.csv"
    mock_data.to_csv(mock_csv, index=False)

    extracted_tweets = extract_tweets_with_sentiments(mock_csv, sample_size=3)
    os.remove(mock_csv)

    assert (
        len(extracted_tweets) == 3
    ), "Extracted tweets count does not match the sample size"
    assert "Content" in extracted_tweets[0], "Extracted tweets missing 'Content' field"
    assert (
        "Sentiment" in extracted_tweets[0]
    ), "Extracted tweets missing 'Sentiment' field"
