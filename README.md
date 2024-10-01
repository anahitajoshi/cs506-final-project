# CS 506 Final Project
Edaad Azman, Jason Anghad, Anahita Joshi, Pavana Manoj, Zac Lan

** Description **
The project aims to predict the box office performance of a movie by analyzing both public sentiment and engagement metrics related to its trailer. Public discussions, particularly on platforms like YouTube and Twitter, generate valuable data on how audiences react to trailers. By combining sentiment analysis with engagement indicators (e.g., comment volume, likes, view count), we aim to create a model that estimates a movie's box office earnings within a short time frame after the trailer release.

** Goals **
- The objective is to predict whether a movie will perform strongly at the box office by analyzing the public's initial response to its trailer. 
- The project aims to use sentiment, engagement metrics, and additional features such as genre and budget to predict the movie's opening weekend box office revenue.  

** Data needed, how to collect **
- Trailer data from YouTube. Comments, views, likes
- Scraping social media sites (Twitter, Reddit) for sentiment analysis
- Getting theater release data from boxofficeMojo
- If it’s a franchise, maybe data for the success of the previous installments 

** How to model data **
- Use VADER or BERT models to get polarity scores for data
- Linear regression and random forest for modeling opening weekend revenue based on polarity scores and other engagement metrics

** Plan to visualize data **
- Heatmaps to visualize the relationship between sentiment, engagement, and franchise history. 
- Line graphs to show the trend sentiment changes between trailer release and movie release 

** Test plan **
- Collect data on various different types of movies ranging from blockbusters to smaller hits and also based on genre. 
- Time-Based Testing: Use trailers released before a specific date as training data and those released after as test data
- Withhold 20% of the collected data as a test set to evaluate model performance

