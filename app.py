import streamlit as st

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(page_title="Smart Health Monitor", layout="wide")

# ---------------------- CUSTOM CSS ----------------------
st.markdown("""
    <style>
        /* Backgrounds */
        .main {
            background-color: #1F1C3F;
            color: #FFFFFF;
            font-family: 'Segoe UI', sans-serif;
        }

        /* Section cards */
        .section {
            background-color: #3C3D50;
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 20px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.25);
        }

        /* Titles */
        h1, h2, h3 {
            color: #B5E6DB;
            margin-bottom: 15px;
        }

        /* Custom divider */
        .divider {
            border: none;
            border-top: 1px solid #B5E6DB;
            margin: 20px 0;
        }

        /* Metrics styling */
        .metric-card {
            background-color: #2B2C40;
            padding: 15px;
            border-radius: 12px;
            text-align: center;
            box-shadow: inset 0 0 5px rgba(181,230,219,0.3);
        }

        .metric-value {
            font-size: 24px;
            font-weight: bold;
            color: #B5E6DB;
        }

        .metric-label {
            font-size: 14px;
            color: #CCCCCC;
        }
    </style>
""", unsafe_allow_html=True)

