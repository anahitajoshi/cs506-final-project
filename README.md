# Instructions to Build and Run the Project

This document provides a step-by-step guide to build, run, and reproduce the results of this project.

---

## Prerequisites
Ensure you have the following installed:
- **Python 3.9 or higher**
- **pip** (Python package manager)
- **Make** (for running Makefile commands)

---

## Step 1: Install Dependencies
To set up the environment and install the required dependencies, run the following command:

```bash
make install
```

This command will:
1. Create a Python virtual environment (`venv`).
2. Install all necessary dependencies listed in `requirements.txt`.

---

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

---

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

---

## Step 4: Run the Web Application

To start the Flask web application, run:

```bash
make run
```

This will:
1. Start the Flask development server at `http://0.0.0.0:5001`.
2. You can access the web page in your browser at `http://localhost:5001`.

---

## Step 5: Interact with the Application

1. On the webpage, upload the CSV file of tweets (generated in **Step 2.2**) and enter:
   - **Movie Name**: The name of the movie.
   - **Budget**: The budget of the movie.
   - **Genre**: The primary genre of the movie.
2. Click "Submit" to see:
   - The predicted lifetime revenue for the movie.
   - Sentiment analysis of the uploaded tweets.

---

## Step 6: Run Tests

To ensure the project works as expected, run the tests using:

```bash
make tests
```

This will:
1. Execute unit tests for key functionalities, including model loading, sentiment analysis, revenue prediction, and the web application routes.
2. Verify the robustness and correctness of the application.

---

## Step 7: Clean Up (Optional)

To clean up the environment, remove the virtual environment, and delete any cached files, run:

```bash
make clean
```

This will:
1. Delete the `venv` directory.
2. Remove all `.pyc` files in the project.

---

## Summary of Commands
| Command           | Description                                      |
|--------------------|--------------------------------------------------|
| `make install`     | Installs dependencies and sets up the environment. |
| `make run`         | Starts the Flask web application.               |
| `make tests`       | Runs unit tests for the application.            |
| `make clean`       | Cleans up the environment.                      |

By following these steps, you will successfully build, run, and interact with the project to reproduce the results.
