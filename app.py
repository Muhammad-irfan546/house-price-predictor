import streamlit as st
import numpy as np
import pickle

with open("house_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="House Price Predictor",
                   page_icon="🏠", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
    }
    h1 {
        color: #f5a623 !important;
        text-align: center;
        font-size: 2.8rem !important;
        font-weight: 900 !important;
        text-shadow: 2px 2px 10px rgba(245,166,35,0.5);
    }
    p { color: #a8dadc !important; text-align: center; }
    div.stButton > button {
        background: linear-gradient(90deg, #f5a623, #e94560);
        color: white !important;
        font-size: 1.3rem !important;
        font-weight: 900 !important;
        border-radius: 50px !important;
        padding: 15px 40px !important;
        border: none !important;
        width: 100% !important;
        margin-top: 20px !important;
        box-shadow: 0px 5px 20px rgba(245,166,35,0.5) !important;
    }
    div.stButton > button:hover {
        transform: scale(1.05) !important;
    }
    .stSelectbox label, .stSlider label,
    .stNumberInput label {
        color: #f5a623 !important;
        font-weight: bold !important;
        font-size: 1rem !important;
    }
    hr { border-color: #f5a623 !important; border-width: 2px !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🏠 House Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p>Predict house prices using Random Forest AI</p>",
            unsafe_allow_html=True)
st.divider()

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""<div style="background:rgba(245,166,35,0.2);
    border-radius:15px; padding:15px; text-align:center;
    border:1px solid #f5a623">
    <h3 style="color:#f5a623;margin:0">🌲</h3>
    <p style="color:white;margin:0;font-size:0.9rem">Random Forest</p>
    </div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div style="background:rgba(233,69,96,0.2);
    border-radius:15px; padding:15px; text-align:center;
    border:1px solid #e94560">
    <h3 style="color:#e94560;margin:0">📊</h3>
    <p style="color:white;margin:0;font-size:0.9rem">545 Houses Trained</p>
    </div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""<div style="background:rgba(56,239,125,0.2);
    border-radius:15px; padding:15px; text-align:center;
    border:1px solid #38ef7d">
    <h3 style="color:#38ef7d;margin:0">🎯</h3>
    <p style="color:white;margin:0;font-size:0.9rem">12 Features Used</p>
    </div>""", unsafe_allow_html=True)

st.divider()
st.markdown("<h3 style='color:#f5a623;text-align:center'>Enter House Details</h3>",
            unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    area = st.number_input("📐 Area (sqft)", min_value=500,
                           max_value=20000, value=5000, step=100)
    bedrooms = st.selectbox("🛏️ Bedrooms", [1, 2, 3, 4, 5, 6])
    bathrooms = st.selectbox("🚿 Bathrooms", [1, 2, 3, 4])
    stories = st.selectbox("🏢 Stories (Floors)", [1, 2, 3, 4])
    parking = st.selectbox("🚗 Parking Spaces", [0, 1, 2, 3])
    mainroad = st.selectbox("🛣️ Main Road", ["yes", "no"])

with col2:
    guestroom = st.selectbox("🛋️ Guest Room", ["yes", "no"])
    basement = st.selectbox("🏚️ Basement", ["yes", "no"])
    hotwaterheating = st.selectbox("🔥 Hot Water Heating", ["yes", "no"])
    airconditioning = st.selectbox("❄️ Air Conditioning", ["yes", "no"])
    prefarea = st.selectbox("⭐ Preferred Area", ["yes", "no"])
    furnishingstatus = st.selectbox("🛋️ Furnishing Status",
                                    ["furnished", "semi-furnished", "unfurnished"])

st.divider()

if st.button("🏠 Predict House Price"):

    def encode_yn(val):
        return 1 if val == "yes" else 0

    furnish_map = {"furnished": 2, "semi-furnished": 1, "unfurnished": 0}

    features = np.array([[
        area, bedrooms, bathrooms, stories,
        encode_yn(mainroad), encode_yn(guestroom), encode_yn(basement),
        encode_yn(hotwaterheating), encode_yn(airconditioning),
        parking, encode_yn(prefarea), furnish_map[furnishingstatus]
    ]])

    prediction = model.predict(features)[0]

    st.markdown(f"""
        <div style="background:linear-gradient(90deg,#f5a623,#e94560);
        border-radius:20px; padding:30px; text-align:center; margin:20px 0">
        <h1 style="color:white;margin:0">🏠 Predicted Price</h1>
        <h1 style="color:white;margin:0;font-size:3rem">
        PKR {prediction:,.0f}</h1>
        <p style="color:white;margin:0;font-size:1.1rem">
        ≈ PKR {prediction/1000000:.2f} Million</p>
        </div>
    """, unsafe_allow_html=True)

    if prediction >= 7000000:
        st.markdown("""<div style="background:linear-gradient(90deg,#11998e,#38ef7d);
        border-radius:15px;padding:20px;text-align:center;margin-top:10px">
        <h2 style="color:white;margin:0">💎 LUXURY PROPERTY!</h2>
        <p style="color:white;margin:0">High end premium house</p>
        </div>""", unsafe_allow_html=True)
    elif prediction >= 4000000:
        st.markdown("""<div style="background:linear-gradient(90deg,#f7971e,#ffd200);
        border-radius:15px;padding:20px;text-align:center;margin-top:10px">
        <h2 style="color:white;margin:0">🏡 MID RANGE PROPERTY</h2>
        <p style="color:white;margin:0">Good value for money!</p>
        </div>""", unsafe_allow_html=True)
    else:
        st.markdown("""<div style="background:linear-gradient(90deg,#e94560,#c0392b);
        border-radius:15px;padding:20px;text-align:center;margin-top:10px">
        <h2 style="color:white;margin:0">🏘️ AFFORDABLE PROPERTY</h2>
        <p style="color:white;margin:0">Budget friendly option!</p>
        </div>""", unsafe_allow_html=True)

st.divider()
st.markdown("""<div style="text-align:center">
<p style="color:#a8dadc">Built with ❤️ by
<span style="color:#f5a623;font-weight:bold">Muhammad Irfan</span>
using Streamlit & Scikit-learn</p>
</div>""", unsafe_allow_html=True)
