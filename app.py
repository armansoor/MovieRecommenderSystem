from flask import Flask, render_template, request
import pandas as pd
import pickle

# Load the Iris dataset
iris_df = pd.read_csv('iris.csv')

# Load the trained model
with open('iris_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Create a Flask application
app = Flask(__name__)

# Define a route to the home page
@app.route('/')
def home():
    return render_template('home.html')

# Define a route to handle the form submission
@app.route('/predict', methods=['POST'])
def predict():
    # Get the user input
    sepal_length = request.form['sepal_length']
    sepal_width = request.form['sepal_width']
    petal_length = request.form['petal_length']
    petal_width = request.form['petal_width']

    # Make a prediction using the trained model
    prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

    # Return the predicted species
    return render_template('result.html', species=prediction[0])

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
