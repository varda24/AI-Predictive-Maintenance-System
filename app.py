import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("models/predictive_model.pkl")

st.set_page_config(page_title="AI Predictive Maintenance", layout="centered")

st.title("🔧 AI-Powered Predictive Maintenance System")

# Inputs
temperature = st.slider("Temperature", 0.0, 100.0, 25.0)
fuel_price = st.slider("Fuel Price", 0.0, 5.0, 2.5)
cpi = st.slider("CPI", 100.0, 250.0, 150.0)
unemployment = st.slider("Unemployment", 0.0, 15.0, 5.0)
size = st.number_input("Store Size", value=150000)

type_val = st.selectbox("Store Type", ["A", "B", "C"])
type_encoded = {"A": 0, "B": 1, "C": 2}[type_val]

year = st.number_input("Year", value=2012)
month = st.slider("Month", 1, 12, 6)

md1 = st.number_input("MarkDown1", value=0.0)
md2 = st.number_input("MarkDown2", value=0.0)
md3 = st.number_input("MarkDown3", value=0.0)
md4 = st.number_input("MarkDown4", value=0.0)
md5 = st.number_input("MarkDown5", value=0.0)

is_holiday = st.selectbox("Is Holiday?", [0, 1])

# Predict
if st.button("Predict Failure"):

    input_data = np.array([[is_holiday, temperature, fuel_price,
                            md1, md2, md3, md4, md5,
                            cpi, unemployment,
                            type_encoded, size, year, month]])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ FAILURE DETECTED!")
    else:
        st.success("✅ System Operating Normally")