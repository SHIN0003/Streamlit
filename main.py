import streamlit as st
import pandas as pd
import altair as alt

# Read the Excel file
df = pd.read_excel("crop yield data sheet.xlsx")
df = df.dropna().groupby("Yeild (Q/acre)").sum().reset_index()
st.bar_chart(df, x = "Yeild (Q/acre)", y = "Rain Fall (mm)")
st.table(df)
