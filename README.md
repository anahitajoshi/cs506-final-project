# CS 506 Final Project
Edaad Azman, Jason Anghad, Anahita Joshi, Pavana Manoj, Zac Lan

**Final**
**Project Details**:<br />

**How to Build and Run**:<br />
# Instructions to Build and Run the Project

This document provides a step-by-step guide to build, run, and reproduce the results of this project.

## Prerequisites
Ensure you have the following installed:
- **Python 3.9 or higher**
- **pip** (Python package manager)
- **Make** (for running Makefile commands)


## Step 1: Install Dependencies
To set up the environment and install the required dependencies, run the following command:

```bash
make install
```

This command will:
1. Create a Python virtual environment (`venv`).
2. Install all necessary dependencies listed in `requirements.txt`.

## Step 2: Prepare the Datasets

### 2.1 Historical Movie Dataset
- The historical dataset (`data/historical_movies.csv`) is already included in the project. No additional steps are needed for this dataset.

### 2.2 Scraping Tweets
- To scrape tweets for sentiment analysis:
  1. Activate the virtual environment:
     ```bash
     . venv/bin/activate
     ```
  2. Navigate to the `scrapers/twitter-scraper` directory:
     ```bash
     cd scrapers/twitter-scraper
     ```
  3. Run the scraper with desired parameters:
     ```bash
     python twitter_scraper.py --keyword "MovieName" --count 100
     ```
     Replace `MovieName` with the movie title you want to scrape tweets for, and `100` with the desired number of tweets. This will generate a CSV file (`tweets.csv`) in the `tweets` directory.

## Step 3: Train the Model and Extract Features

The training process and feature extraction must be run using the provided `final.ipynb` notebook.

1. Activate the virtual environment:
   ```bash
   . venv/bin/activate
   ```
2. Open the notebook:
   ```bash
   jupyter notebook final.ipynb
   ```
3. Execute the notebook cells step by step to:
   - Train models using the historical dataset.
   - Save the trained model (`model/voting_reg.pkl`) and extracted features (`model/features.pkl`).

These files are critical for enabling the prediction functionality of the web application.

## Step 4: Run the Web Application

To start the Flask web application, run:

```bash
make run
```

This will:
1. Start the Flask development server at `http://0.0.0.0:5001`.
2. You can access the web page in your browser at `http://localhost:5001`.

## Step 5: Interact with the Application

1. On the webpage, upload the CSV file of tweets (generated in **Step 2.2**) and enter:
   - **Movie Name**: The name of the movie.
   - **Budget**: The budget of the movie.
   - **Genre**: The primary genre of the movie.
2. Click "Submit" to see:
   - The predicted lifetime revenue for the movie.
   - Sentiment analysis of the uploaded tweets.

## Step 6: Run Tests

To ensure the project works as expected, run the tests using:

```bash
make tests
```

This will:
1. Execute unit tests for key functionalities, including model loading, sentiment analysis, revenue prediction, and the web application routes.
2. Verify the robustness and correctness of the application.


## Step 7: Clean Up (Optional)

To clean up the environment, remove the virtual environment, and delete any cached files, run:

```bash
make clean
```

This will:
1. Delete the `venv` directory.
2. Remove all `.pyc` files in the project.

## Summary of Commands
| Command           | Description                                      |
|--------------------|--------------------------------------------------|
| `make install`     | Installs dependencies and sets up the environment. |
| `make run`         | Starts the Flask web application.               |
| `make tests`       | Runs unit tests for the application.            |
| `make clean`       | Cleans up the environment.                      |

By following these steps, you will successfully build, run, and interact with the project to reproduce the results.


**Results**:<br />
Visualizations of data: <br />
Data processing and modeling: <br />
Results/demo: <br />


-----
**Midterm Progress Demo Video Link**:<br />
https://www.youtube.com/watch?v=HUV24do8u14

**Data Collection for Midterm:**<br />
For our preliminary data collection, we have focused on scraping Twitter using Selenium for specific movies. We are using a WebDriver to automate scrolling on the Twitter webpage. The “Tweet” information we are gathering includes username, handle, the actual tweet content, hashtags, mentions, the tweet link, etc. that we can use later. All of this information from one Tweet will be gathered in a CSV file with the other tweets we searched for.
	In the next part of the code, we define the main scraping process through the Twitter_Scraper class. This class handles setting up a WebDriver, logging in to Twitter, navigating to specific tweet feeds, and gathering data based on parameters like username, hashtag, or query. It also includes error-handling methods for login steps, like inputting the username and password, and managing any unusual activity prompts from Twitter.
After configuring an instance of Twitter_Scraper with login credentials and parameters such as date range and the search query "Extraction 2," the scraper logs in, navigates to Twitter's search results, and starts collecting tweets that match our criteria. Each tweet’s details, including content, likes, retweets, and timestamp, are stored as data points.
Finally, the save_to_csv function structures the collected tweets into a CSV file, including columns for engagement metrics and tweet metadata. This CSV file serves as a dataset for further analysis, providing an organized snapshot of Twitter’s response to specific search terms or hashtags.
The bom_scraper file collects the theater release data needed by fetching it from the OMDb API such as the lifetime revenue, budget and rating  and then appends this information to the original csv found on the dataset found on kaggle titled “Opening Weekend Box Office Performance”. It then cleans up the data by keeping only the relevant columns and saves the updated csv. 


**Data Processing & Modeling & Preliminary Results for Midterm**:<br />
Overview:<br />
The final.py script is designed as of right now to predict the overall performance of the Smile 2. As we progress in the project however, we will allow the user to input their movie of choice. For now we are combining historical movie data and real-time sentiment analysis from social media. Using machine learning, specifically gradient boosting regression, the script produces sentiment scores, budget data, and genre similarity to create a predictive model. This approach allows for the model to capture historical performance patterns and current audience sentiment to provide an accurate revenue estimate.
						
Data Loading and Preparation:<br />	
The script loads two primary datasets. The first is historical movie dara which contains attributes for various movies, including genres, budgets, and IMDb ratings. The second is social media sentiment data which consists of tweets about the movie “Smile 2” meant to gauge audience sentiment and mood. We set key attributes specific to “Smile 2” such as its budget and primary genres such as horror and thriller. These attributes help to better filter and select comparable movies for analysis.
						
Sentiment Analysis on Tweets:<br />				
We are using TextBlob which calculates the sentiment polarity for each tweet. It ranges from -1 to 1. 1 means its positive, neutral is 0 and -1 means negative reception. An average sentiment score is derived from the tweets which represents the general public’s view towards “Smile 2”. The average score will later become a very important feature in out prediction model.
						
Derived Sentiment for Historical Movies:<br />				
Since the data for the historical movies do not have tweet data, the script assigns them a sentiment score based on their IMDB rating. High rating will be anything higher than 7/5. Mid-ranfe will be 5.5 - 7.5 and low rating will be anything less than 5.5
						
Genre Similarity Calculation:<br />
A genre similarity score is calculated by comparing the genres of each historical movie to “Smile 2”. Movies with overlapping genres receive higher similarity scores. Using data from both the budget and genre similarity, the script filters out the movies that are too dissimilar such as movies with budgets within 50-150% of “Smile 2”’s budget and a genre similarity will be used for further analysis later on.
						
Feature Engineering:<br />
The budget is used to compare movies with similar production scales. Genre similarity quantifies the audience overlap with “Smile 2”. Average sentiment captures the real-time public interest in “Smile 2”. Derived sentiment represents sentiment scores based on historical movies. Sentiment-Genre Interactions combines derived sentiment and genre similarity scores ot emphasize genre-specific audience interest.
						
Model Training and Evaluation:<br />
We use a Gradient Boosting Regressor due to its strong predictions and it can handle complex, nonlinear relationships. The data is split into training and testing sets and it is trained on the engineering features and evaluated using the test set. We measure the performance using the R-squared score to see how the predicted values align with the actual box office revenues in the test dataset.
						
Predicting “Smile 2” Box Office Revenue:<br />
Using the training model, the script predicts the box office revenue for “Smile 2”. The model takes in the movie’s budget, genre similarity, average sentiment score, and sentiment-genre interaction score from the web scarping. The script that predicts the lifetime revenue for the movie based on the mode’s assessment, taking into account its historical performance patterns and real-time public sentiment. 

**Description of Project**
- The project aims to predict the box office performance of a movie by analyzing both public sentiment and engagement metrics related to its trailer. Public discussions, particularly on platforms like YouTube and Twitter, generate valuable data on how audiences react to trailers. By combining sentiment analysis with engagement indicators (e.g., comment volume, likes, view count), we aim to create a model that estimates a movie's box office earnings within a short time frame after the trailer release.

**Goals**
- The objective is to predict whether a movie will perform strongly at the box office by analyzing the public's initial response to its trailer. 
- The project aims to use sentiment, engagement metrics, and additional features such as genre and budget to predict the movie's opening weekend box office revenue.  

**Data needed, how to collect**
- Trailer data from YouTube. Comments, views, likes
- Scraping social media sites (Twitter, Reddit) for sentiment analysis
- Getting theater release data from boxofficeMojo
- If it’s a franchise, maybe data for the success of the previous installments

**How to model data**
- Use VADER or BERT models to get polarity scores for data
- Linear regression and random forest for modeling opening weekend revenue based on polarity scores and other engagement metrics

**Plan to visualize data**
- Heatmaps to visualize the relationship between sentiment, engagement, and franchise history. 
- Line graphs to show the trend sentiment changes between trailer release and movie release 

**Test plan**
- Collect data on various different types of movies ranging from blockbusters to smaller hits and also based on genre. 
- Time-Based Testing: Use trailers released before a specific date as training data and those released after as test data
- Withhold 20% of the collected data as a test set to evaluate model performance
