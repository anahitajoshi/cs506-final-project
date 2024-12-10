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
    all_genres = set(
        [col.split("_", 1)[1] for col in genre_cols if col.startswith("Genre_")]
    )  # Extract genres

    # Ensure all genres from `genre_cols` are included in `all_genres`
    assert all([f"Genre_{genre}" in genre_cols for genre in all_genres])

    # Test with valid inputs
    revenue = predict_revenue_for_movie(
        voting_reg,
        all_genres,
        genre_cols,
        feature_cols,
        user_budget=25000000,
        user_derived_sentiment=0.5,
        user_genre="Horror",  # Use a valid genre from `genre_cols`
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
