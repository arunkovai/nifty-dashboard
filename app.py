import streamlit as st
import pandas as pd

st.title("NIFTY 50 Dashboard")

df = pd.read_csv("NIFTY50_Weekly_Aggregated.csv")

st.write(df.head())
