# MovieRecommenderSystem
An example code for a movie recommender system using Surprise, which is an open-source Python scikit for building and analyzing recommender systems.

The Dataset https://archive.ics.uci.edu/ml/datasets/iris

In this example, we first load the Iris dataset from a CSV file using pd.read_csv. We also load a trained machine learning model from a Pickle file using pickle.load.

We then define a Flask application and create two routes: one for the home page ('/'), and one to handle the form submission ('/predict'). The home page simply returns an HTML template that contains a form for the user to input their measurements. The form is submitted to the '/predict' route using the POST method.

When the user submits the form, the predict function is called. This function gets the user input from the form using request.form, makes a prediction using the trained model, and returns an HTML template that displays the predicted species.

Finally, we run the Flask application using app.run.

These templates use the Flask templating language to display the predicted species in the result.html template.

To run this example code, you would need to save the Iris dataset to a file called iris.csv and the trained model to a file called iris_model.pkl. You would also need to install Flask using pip install flask.
