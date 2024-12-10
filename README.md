# CS 506 Final Project
Edaad Azman, Jason Anghad, Anahita Joshi, Pavana Manoj, Zac Lan

# Project Overview 

**PROJECT DEMO VIDEO INCLUDED IN RESULTS SECTION**

**Description of Project**
- The project aims to predict the box office performance of a movie by analyzing both public sentiment and engagement metrics related to its trailer. Public discussions, particularly on platforms like YouTube and Twitter, generate valuable data on how audiences react to trailers. By combining sentiment analysis with engagement indicators (e.g., comment volume, likes, view count), we aim to create a model that estimates a movie's box office earnings within a short time frame after the trailer release.

**Goals**
- The objective is to predict whether a movie will perform strongly at the box office by analyzing the public's initial response to its trailer. 
- The project aims to use sentiment, engagement metrics, and additional features such as genre and budget to predict the movie's opening weekend box office revenue.  

# Instructions to Build and Run the Project

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

  1. Navigate to the `scrapers/twitter-scraper` directory
  2. Create a .env file and add X username and password:   
  ```env
  TWITTER_USERNAME=username
  TWITTER_PASSWORD=password
	```
3. Navigate to `main.ipynb` in the same directory

4. Run the scraper on the virtual environment with desired parameters, example:

    ```python

    USER_UNAME = os.environ['TWITTER_USERNAME']
	USER_PASSWORD = os.environ['TWITTER_PASSWORD']

	scraper = Twitter_Scraper(
		username=USER_UNAME,
		password=USER_PASSWORD,
		since_date="2023-10-20",
		until_date="2023-10-22"
		# max_tweets=10,
		# scrape_username="elonmusk",
		# scrape_hashtag="something",
		# scrape_query="something",
		# scrape_latest=False,
		# scrape_top=True,
		# scrape_poster_details=True
	)

	```
5. Example for running the custom query and max tweets:

	```python

    scraper.scrape_tweets(
    max_tweets=1000,
    scrape_query="Saltburn",
    scrape_latest=True,
	)
	
	```
6. Once the scraper runs through every block of code, it should generate a csv with the tweets scraped which can be used for training the models as well as the web page later.

## Step 3: Train the Model and Extract Features

The training process and feature extraction must be run using the provided `final.ipynb` notebook.

1. Execute the notebook cells step by step:
   - Run the notebook in the virtual environment. 
   - Train models using the historical dataset and tweets scraped.
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

# Testing Overview

## Tests Included

### `test_pipeline.py`:

**Purpose:**
To test the core functionalities of the `pipeline.py` module, which handles model loading, sentiment analysis, revenue prediction, and data extraction.

**Tests:**

- **`test_load_model_and_features`**:
  - Validates that the model, genre columns, and feature columns are loaded correctly.
  - Ensures the pipeline can access the necessary components for prediction.

- **`test_get_tweet_sentiment`**:
  - Tests the sentiment analysis process on mock tweets.
  - Ensures the mean sentiment and sentiment list are computed correctly.

- **`test_predict_revenue_for_movie`**:
  - Validates the revenue prediction process.
  - Ensures correct mapping of features and interactions based on user input.

- **`test_extract_tweets_with_sentiments`**:
  - Tests the extraction of sample tweets and their sentiment scores.
  - Verifies that the correct number of tweets is extracted and that sentiment scores are included.

### `test_app.py`:

**Purpose:**
To test the Flask application (`app.py`) for its ability to handle GET and POST requests.

**Tests:**

- **`test_index_get`**:
  - Ensures the index page is accessible via a GET request.
  - Validates a 200 OK response for the landing page.

- **`test_index_post`**:
  - Tests the submission of user input (movie name, budget, genre, tweets CSV) via a POST request.
  - Ensures the result page is rendered correctly after submission.
  - Simulates the full workflow: input data → sentiment analysis → revenue prediction → rendering of the result.


## GitHub Workflow Overview

The GitHub workflow (`python-tests.yml`) automates the testing process to ensure code quality and functionality in a continuous integration/continuous deployment (CI/CD) pipeline.

### Key Steps in the Workflow:

- **Trigger Conditions:**
  - The workflow runs on any `push` or `pull_request` event to the `main` branch.
  - Ensures that any new code or changes are automatically tested before merging.

- **Environment Setup:**
  - Sets up a Python 3.9 environment.
  - Creates a virtual environment (`venv`), installs dependencies from `requirements.txt`, and upgrades `pip`.

- **Test Execution:**
  - Configures the `PYTHONPATH` to include the project directory.
  - Runs all tests in the `tests/` directory using `pytest`.

- **Result Handling:**
  - Outputs a detailed report of test results.
  - If any test fails, the workflow stops, alerting the developer to fix the issue before proceeding.

# Data Processing and Modeling 

# Visualizations of Data
<img src="https://github.com/anahitajoshi/cs506-final-project/blob/main/data_visualizations/1.png?raw=true" width="400" />

# Results

## Project Demo Video:

https://youtu.be/rTVn0CohDO8?si=6NupoyTiZJy03wgO


## Predictive Performance:

- We calculated the **R² score** on a test set split after training.
- Any positive R² indicates some predictive capability. With optimization, we achieved a reasonable R² score (**>0.5** in some trial runs), indicating that the model can partially explain the variance in revenue outcomes based on budget, genre, and sentiment features.


## From Scraper to Notebook to Interactive Web Page:

1. **Scraping Data:**
   - Data was scraped from Twitter for sentiment analysis and from Box Office Mojo for revenue and budget information.
   - The scraper allows users to input a movie keyword and the desired number of tweets, producing a CSV ready for analysis.

2. **Training the Model:**
   - In `final.ipynb`, we used the scraped data and historical movie datasets to train and optimize models.
   - The outputs, `voting_reg.pkl` (model) and `features.pkl` (feature data), are saved for use in the web application.

3. **Integration with Flask:**
   - The Flask application takes user inputs (movie name, budget, genre, and tweets CSV) and predicts box office revenue.
   - It loads the trained model and features, reconstructs the genre encoding logic, and performs feature engineering to make predictions.


## Significance:

This pipeline demonstrates the **full data science lifecycle**, including:

1. **Data Collection:**
   - Scraping Twitter for sentiment analysis.
   - Extracting revenue and budget information from box office APIs.

2. **Data Cleaning and Feature Engineering:**
   - Handling missing values, formatting data, and encoding genres.
   - Combining budget and sentiment features for interaction terms.

3. **Model Training and Optimization:**
   - Using ensemble models like Gradient Boosting, Random Forest, and XGBoost.
   - Hyperparameter tuning to improve predictive performance.

4. **Interactive Predictions:**
   - Providing a user-friendly interface for real-time predictions.
   - Visualizing results with tables and distribution plots for better interpretability.


## Achievements:

While the initial demonstration focused on a specific movie, the final implementation generalizes to any movie for which the user can provide:

- **A CSV of tweets** (to derive sentiment).
- **A budget value**.
- **A primary genre**.

### Deliverables of the Web Application:

1. Predicted box office performance.
2. Sentiment score derived from tweets.
3. A table of sample tweets and their respective sentiment scores.
4. A distribution plot of sentiment scores, showcasing the number of tweets in each range.

By achieving these deliverables, we fulfilled our original goal of predicting box office revenue from early sentiment and metadata.
