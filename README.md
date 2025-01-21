# Bangalore Home Price Prediction

## Project Overview
The goal of this project is to predict the price of homes in Bangalore based on various features such as area in square foots, number of bedrooms and bathrooms, and other location-related factors.

## The project consists of multiple components:
**Frontend:** A web page built with HTML, CSS, and JavaScript for users to input data and receive predictions.
**Backend:** A Flask server that loads the trained model and serves predictions via an API.
**Machine Learning Model:** A linear regression model trained on a dataset containing real estate data of Bangalore.
**Dataset:** A CSV file with information on home features like area, number of bedrooms, location, and the price of homes.

## Files and Directories
**client/:** Contains the frontend files (HTML, CSS, and JavaScript).
**dataset/:** Contains the dataset (CSV file) used to train the model.
**model/:** Contains the Jupyter notebook for model training, the trained pickle file, and a JSON file with location data.
**server/:** Contains the Flask server that handles API requests and serves predictions.
