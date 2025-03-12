# Bangalore Home Price Prediction

## Project Overview
The goal of this project is to predict the price of homes in Bangalore based on various features such as area in square foots, number of bedrooms and bathrooms, and other location-related factors. This project predicts home prices in Bangalore using machine learning, specifically the Linear Regression algorithm. The dataset, containing features like area, number of bedrooms, and location, was preprocessed through data cleaning, handling missing values, feature engineering, and scaling. Exploratory Data Analysis (EDA) helped identify key correlations, guiding feature selection. The model was trained using the scikit-learn library, evaluated for accuracy with metrics like Mean Squared Error and R-squared, and fine-tuned using cross-validation. After training, the model was serialized with Pickle and integrated into a Flask backend, where users can input property details via a frontend built with HTML, CSS, and JavaScript to receive real-time price predictions.

## The project consists of multiple components:
- **Frontend:** A web page built with HTML, CSS, and JavaScript for users to input data and receive predictions.
- **Backend:** A Flask server that loads the trained model and serves predictions via an API.
- **Machine Learning Model:** A linear regression model trained on a dataset containing real estate data of Bangalore.
- **Dataset:** A CSV file with information on home features like area, number of bedrooms, location, and the price of homes.

## Files and Directories

```
ML Project/
 ├── client
 │    ├── index.html
 │    ├── styoe.css
 │    └── script.js
 ├── DataSet/
 │    ├── Bengaluru_House_Data.csv
 ├── Model/
 │    ├── bhp.ipynb
 │    └── columns.json
 ├── server/
 │    ├── artifacts/
 │    		├── banglore_home_prices_model.pickle
 │    		└── columns.json
 └── server.py
 └── util.py
```

- **client/:** Contains the frontend files (HTML, CSS, and JavaScript).
- **dataset/:** Contains the dataset (CSV file) used to train the model.
- **model/:** Contains the Jupyter notebook for model training, the trained pickle file, and a JSON file with location data.
- **server/:** Contains the Flask server that handles API requests and serves predictions.
