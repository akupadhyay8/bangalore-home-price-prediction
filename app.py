import streamlit as st
import joblib
import json
import numpy as np
import base64
import os

st.set_page_config(page_title="🏠 Bangalore House Price Predictor")

# Load artifacts
def load_saved_artifacts():
    with open('server/artifacts/columns.json', 'r') as f:
        data_columns = json.load(f)['data_columns']
        locations = data_columns[3:]

    model = joblib.load('server/artifacts/banglore_home_prices_model.pkl')
    return data_columns, locations, model

data_columns, location_list, model = load_saved_artifacts()

# Predict function
def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(model.predict([x])[0], 2)

# Function to encode image to base64 for background
def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Set background image using local path
def set_background(image_path):
    base64_image = get_base64_of_image(image_path)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{base64_image}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ✅ Image path 
image_path = "Image/Background.jpg"
set_background(image_path)

# UI Heading
st.markdown("<h1 style='text-align: center; color: white;'>🏡 Bangalore House Price Prediction</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: white;'>Enter details below to estimate the property price</h4>", unsafe_allow_html=True)

# Input form
with st.container():
    location = st.selectbox("Select Location", sorted(location_list))
    sqft = st.number_input("Total Square Feet Area", min_value=300, max_value=10000, step=50)
    bhk = st.selectbox("Number of Bedrooms (BHK)", [1, 2, 3, 4, 5])
    bath = st.selectbox("Number of Bathrooms", [1, 2, 3, 4])

    if st.button("Estimate Price"):
        price = get_estimated_price(location, sqft, bhk, bath)
        st.success(f"💰 Estimated Price: ₹ {price} Lakhs")

# Footer
st.markdown("""
    <hr style="border: 1px solid white;">
    <p style="text-align: center; color: lightgray;">
        Developed by Abhishek Kumar | Powered by Machine Learning
    </p>
""", unsafe_allow_html=True)
