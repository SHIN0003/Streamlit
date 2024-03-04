import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title("Crop Yield Data Analysis")

    with st.sidebar:
        st.header("Navigation")
        page_options = ["Overview", "Box Plot", "Heatmap", "Bar Chart", "Data Table"]
        selected_page = st.selectbox(
            label="Choose a page:",
            options=page_options,
        )

    if selected_page == "Overview":
        show_overview()
    elif selected_page == "Box Plot":
        show_box_plot()
    elif selected_page == "Heatmap":
        show_heatmap()
    elif selected_page == "Bar Chart":
        show_bar_chart()
    elif selected_page == "Data Table":
        show_data_table()

def show_overview():
    st.subheader("Overview")
    st.write("This is an overview of the crop yield data analysis.")

def show_box_plot():
    st.subheader("Box Plot")
    df = pd.read_excel("crop yield data sheet.xlsx")
    df = df.dropna().groupby("Yeild (Q/acre)").sum().reset_index()

    melted_df = df.melt(id_vars=['Yeild (Q/acre)'], 
                         var_name='Category', 
                         value_name='Value')

    plt.figure(figsize=(12, 6))
    box_plot = sns.boxplot(data=melted_df, x='Yeild (Q/acre)', y='Category')
    box_plot.set_title('Yield (Q/acre) by Category')
    st.pyplot(plt)

def show_heatmap():
    st.subheader("Heatmap")
    df = pd.read_excel("crop yield data sheet.xlsx")
    df = df.dropna().groupby("Yeild (Q/acre)").sum().reset_index()
    corr = df.corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title('Correlation Heatmap of Factors and Yield')
    st.pyplot(plt)

def show_bar_chart():
    st.subheader("Bar Chart")
    df = pd.read_excel("crop yield data sheet.xlsx")
    df = df.dropna().groupby("Yeild (Q/acre)").sum().reset_index()
    st.bar_chart(df, x = "Yeild (Q/acre)", y = "Rain Fall (mm)")

def show_data_table():
    st.subheader("Data Table")
    df = pd.read_excel("crop yield data sheet.xlsx")
    df = df.dropna().groupby("Yeild (Q/acre)").sum().reset_index()
    df = df.iloc[3:10]
    st.table(df)

if __name__ == "__main__":
    st.set_page_config(
        page_title="Crop Yield Data Analysis", page_icon=":seedling:"
    )
    main()
