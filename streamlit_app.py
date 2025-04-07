import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image
import requests
from io import BytesIO
import time
import json

# Load Lottie animation
import streamlit_lottie
from streamlit_lottie import st_lottie

# Set page config
st.set_page_config(page_title="Veggie Price Predictor", layout="wide", page_icon="🥦")

# Load animation from URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Sample Lottie animation
lottie_veggie = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_bu3xvx.json")

# Mock sample data (to replace with real model + data)
data = pd.DataFrame({
    'Vegetable': ['Tomato', 'Spinach', 'Carrot', 'Broccoli', 'Potato'],
    'Avg_Price': [12.5, 8.0, 10.2, 14.3, 7.5],
    'Predicted_Date': ['2025-04-08']*5
})

# Mock image URLs (replace with your own or use local assets)
veggie_images = {
    "Tomato": "https://source.unsplash.com/600x400/?tomato",
    "Spinach": "https://source.unsplash.com/600x400/?spinach",
    "Carrot": "https://source.unsplash.com/600x400/?carrot",
    "Broccoli": "https://source.unsplash.com/600x400/?broccoli",
    "Potato": "https://source.unsplash.com/600x400/?potato",
}

# App title
st.markdown("""
    <style>
        .main {
            background-color: #0f0f0f;
            color: white;
        }
        .block-container {
            padding-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🥦 Veggie Price Predictor")
st.subheader("Accurate, Creative and Easy-to-Use Pricing Tool")

# Sidebar
with st.sidebar:
    st_lottie(lottie_veggie, height=200)
    st.markdown("**Select a vegetable and a model to predict pricing trends.**")
    selected_veg = st.selectbox("Choose a Vegetable", data['Vegetable'].unique())
    model = st.selectbox("Select Prediction Model", [
        "Linear Regression",
        "Decision Tree",
        "Random Forest",
        "SVR",
        "XGBoost",
        "Prophet"
    ])
    st.markdown("---")
    if st.button("Predict"):
        with st.spinner("Crunching the numbers..."):
            time.sleep(2)  # simulate prediction

        result = data[data["Vegetable"] == selected_veg].iloc[0]

        # Layout
        col1, col2 = st.columns([1, 1])

        with col1:
            st.image(veggie_images[selected_veg], caption=selected_veg, use_column_width=True)

        with col2:
            st.markdown(f"### 🥗 Prediction Results for {selected_veg}")
            st.markdown(f"**Model Used:** {model}")
            st.markdown(f"**Predicted Avg Price:** R{result['Avg_Price']:.2f}")
            st.markdown(f"**Expected Date:** {result['Predicted_Date']}")

            # Sample chart
            chart_data = pd.DataFrame({
                "Day": ["Yesterday", "Today", "Tomorrow"],
                "Price": [result["Avg_Price"] * 0.95, result["Avg_Price"], result["Avg_Price"] * 1.05]
            })
            fig = px.line(chart_data, x="Day", y="Price", title=f"{selected_veg} Price Trend")
            st.plotly_chart(fig, use_container_width=True)

            st.success("Prediction complete!")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit | © 2025 Your Name")
