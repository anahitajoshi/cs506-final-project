import os
from flask import Flask, request, render_template, redirect, url_for, flash
from model.pipeline import (
    load_model_and_features,
    load_all_genres,
    get_tweet_sentiment,
    predict_revenue_for_movie,
    extract_tweets_with_sentiments,  # Import the new function
)

app = Flask(__name__)
app.secret_key = "your_secret_key"

UPLOAD_FOLDER = "data"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

voting_reg, genre_cols, feature_cols = load_model_and_features()
all_genres = load_all_genres()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        movie_name = request.form.get("movie_name")
        user_budget = request.form.get("budget")
        user_genre = request.form.get("genre")
        file = request.files.get("tweets_csv")

        if not movie_name or not user_budget or not user_genre or not file:
            flash("All fields are required.", "error")
            return redirect(url_for("index"))

        csv_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(csv_path)

        try:
            user_budget = float(user_budget)
        except ValueError:
            flash("Budget must be numeric.", "error")
            return redirect(url_for("index"))

        # Compute sentiment from user’s tweets CSV
        user_derived_sentiment, sentiment_scores = get_tweet_sentiment(csv_path)

        # Extract a sample of tweets and their sentiments
        tweets_with_sentiments = extract_tweets_with_sentiments(csv_path)

        # Predict revenue
        predicted_revenue = predict_revenue_for_movie(
            voting_reg,
            all_genres,
            genre_cols,
            feature_cols,
            user_budget,
            user_derived_sentiment,
            user_genre,
        )

        return render_template(
            "result.html",
            movie_name=movie_name,
            sentiment_score=user_derived_sentiment,
            predicted_revenue=predicted_revenue,
            genre=user_genre,
            budget=user_budget,
            sentiment_scores=sentiment_scores,  # Pass all sentiment scores
            tweets_with_sentiments=tweets_with_sentiments,  # Pass extracted tweets with sentiments
        )
    return render_template("index.html")
