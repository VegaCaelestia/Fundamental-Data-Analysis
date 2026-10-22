import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

all_df = pd.read_csv('Dashboard/main_df.csv')

all_df['dteday'] = pd.to_datetime(all_df['dteday'])
all_df.sort_values(by="dteday", inplace=True)
all_df.reset_index(inplace=True, drop=True)

min_date = all_df["dteday"].min()
max_date = all_df["dteday"].max()

with st.sidebar:
    st.title("Bike Sharing Filter")

start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = all_df[(all_df["dteday"] >= pd.to_datetime(start_date)) & 
                 (all_df["dteday"] <= pd.to_datetime(end_date))]

st.title("Dashboard Analisis Penyewaan Sepeda")
