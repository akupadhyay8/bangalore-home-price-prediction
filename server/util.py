import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

# Function to get estimated home price
def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())  # Check if the location exists in data_columns
    except:
        loc_index = -1  # If location doesn't exist, set index to -1

    x = np.zeros(len(__data_columns))  # Create a vector for input features
    x[0] = sqft  # Total square feet
    x[1] = bath  # Number of bathrooms
    x[2] = bhk   # Number of bedrooms
    if loc_index >= 0:
        x[loc_index] = 1  # Set location index in the vector

    return round(__model.predict([x])[0], 2)  # Return the predicted price rounded to 2 decimal places

# Function to return location names
def get_location_names():
    return __locations  # Return the list of locations

# Function to load saved artifacts (model and column names)
def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __data_columns
    global __locations

    try:
        # Load column names from columns.json file
        with open("./artifacts/columns.json", 'r') as f:
            __data_columns = json.load(f)['data_columns']
            __locations = __data_columns[3:]  # Skip first 3 columns (sqft, bath, bhk)

        # Load model from pickle file
        global __model
        with open("./artifacts/banglore_home_prices_model.pickle", 'rb') as f:
            __model = pickle.load(f)

        print("Loading saved artifacts...done")
    except FileNotFoundError as e:
        print(f"Error loading files: {e}")
        exit(1)  # Exit if files are not found
    except Exception as e:
        print(f"Error loading artifacts: {e}")
        exit(1)  # Exit if any other error occurs

# For testing purposes (can be removed in production)
if __name__ == '__main__':
    load_saved_artifacts()  # Ensure artifacts are loaded
    print(get_location_names())  # Print available location names
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))  # Test prediction
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))  # Test prediction with different inputs
    print(get_estimated_price('Kalhalli', 1000, 2, 2))  # Test prediction for another location
    print(get_estimated_price('Ejipura', 1000, 3, 2))  # Test prediction for another location
