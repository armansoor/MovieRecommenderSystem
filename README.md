# Movie Recommender System using Surprise
This is an example code for a movie recommender system using Surprise, an open-source Python scikit for building and analyzing recommender systems.

## Dataset
The dataset used in this example is the MovieLens 100k dataset (https://archive.ics.uci.edu/ml/datasets/iris). This dataset contains ratings of movies by users, as well as demographic information about the users and the movies.

## Usage
1. To use this example code, you will need to install Surprise and Flask using pip.

2. You will also need to download the MovieLens 100k dataset and save it to a file called ratings.csv. You can download the dataset from the MovieLens website.

3. Once you have the dataset and have installed the necessary packages, you can run the Flask application by running the following command:

python app.py

4. This will start the Flask server, and you can access the application by visiting http://localhost:5000 in your web browser.

## Files

This repository contains the following files:

1. app.py: The Flask application that handles user input and displays recommendations.
2. models.py: The code for building and training the recommendation model.
3. utils.py: Utility functions for loading and preprocessing the data.
4. templates/home.html: The HTML template for the home page.
5. templates/result.html: The HTML template for displaying the recommended movies.

## Credit

This example code is based on the tutorial Building a Movie Recommendation Engine in Python using Scikit-Learn.

The code for building the recommendation model using Surprise is based on the Surprise documentation.
