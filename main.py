import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Read the Excel file
df = pd.read_excel("crop yield data sheet.xlsx")
df = df.dropna().groupby("Yeild (Q/acre)").sum().reset_index()

melted_df = df.melt(id_vars=['Yeild (Q/acre)'], 
                     var_name='Category', 
                     value_name='Value')

# Now, create a box plot with seaborn
plt.figure(figsize=(12, 6))
box_plot = sns.boxplot(data=melted_df, x='Yeild (Q/acre)', y='Category')
box_plot.set_title('Yield (Q/acre) by Category')
st.pyplot(plt)

corr = df.corr()

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
plt.title('Correlation Heatmap of Factors and Yield')
st.pyplot(plt)

st.bar_chart(df, x = "Yeild (Q/acre)", y = "Rain Fall (mm)")
st.table(df)
