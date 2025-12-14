import streamlit as st
import pandas as pd
import joblib

#  FIRST Streamlit command – must be here, only once
st.set_page_config(
    page_title="Air Quality & Pollution Prediction",
    page_icon="🌫️",
    layout="wide"
)

MODEL_PATH = "models/xgb_o3_aqi_model.joblib"

@st.cache_resource
def load_model():
    data = joblib.load(MODEL_PATH)
    return data["model"], data["features"]

model, feature_cols = load_model()

# ---------- Helper: AQI category ----------
def aqi_category(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups"
    elif aqi <= 200:
        return "Unhealthy"
    elif aqi <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"

# ---------- Streamlit UI ----------
st.title("🌫️ Air Quality & Pollution Prediction")
st.write(
    """
    This app uses the **XGBoost regression model** trained on US EPA pollution data  
    to predict **Ozone Air Quality Index (O3_AQI)** from other pollutant measurements.
    """
)

st.markdown("### 1. Input pollutant measurements")

col1, col2 = st.columns(2)

with col1:
    no2_mean = st.number_input("NO₂ Mean (ppb)", min_value=0.0, max_value=150.0, value=20.0, step=0.5)
    no2_aqi  = st.number_input("NO₂ AQI",        min_value=0.0, max_value=200.0, value=30.0, step=1.0)
    so2_mean = st.number_input("SO₂ Mean (ppb)", min_value=0.0, max_value=50.0,  value=3.0,  step=0.1)
    so2_aqi  = st.number_input("SO₂ AQI",        min_value=0.0, max_value=200.0, value=10.0, step=1.0)

with col2:
    o3_mean  = st.number_input("O₃ Mean (ppm)",  min_value=0.0, max_value=0.20, value=0.03, step=0.001)
    co_mean  = st.number_input("CO Mean (ppm)",  min_value=0.0, max_value=10.0, value=0.5,  step=0.1)
    co_aqi   = st.number_input("CO AQI",         min_value=0.0, max_value=200.0, value=5.0,  step=1.0)

if st.button("🔮 Predict Ozone AQI"):
    # build one-row dataframe in the same column order as training
    input_dict = {
        "NO2_Mean": no2_mean,
        "NO2_AQI":  no2_aqi,
        "O3_Mean":  o3_mean,
        "SO2_Mean": so2_mean,
        "SO2_AQI":  so2_aqi,
        "CO_Mean":  co_mean,
        "CO_AQI":   co_aqi,
    }

    X_new = pd.DataFrame([input_dict])[feature_cols]
    pred_aqi = float(model.predict(X_new)[0])
    category = aqi_category(pred_aqi)

    st.markdown("### 2. Predicted Ozone AQI")
    st.metric(label="Predicted O₃ AQI", value=f"{pred_aqi:.1f}")
    st.write(f"**Air Quality Category:** `{category}`")

    st.info(
        "Interpretation based on US EPA AQI breakpoints.\n"
    )

st.markdown("---")
st.caption("Capstone Project · Air Quality & Pollution Prediction · Sai Nithin Reddy Kasireddy")
