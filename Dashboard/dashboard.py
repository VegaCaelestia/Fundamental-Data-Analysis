import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

main_df = pd.read_csv('main_df.csv')

main_df['dteday'] = pd.to_datetime(main_df['dteday'])

min_date = main_df['dteday'].min()
max_date = main_df['dteday'].max()

with st.sidebar:
    st.title("Filter Data")
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

filtered_df = main_df[(main_df['dteday'] >= pd.to_datetime(start_date)) & 
                      (main_df['dteday'] <= pd.to_datetime(end_date))]

st.title("Dashboard Analisis Penyewaan Sepeda")

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("1. Musim apa yang memiliki rata-rata jumlah peminjaman sepeda harian paling tinggi sepanjang tahun 2011–2012?")
    
    season_df = filtered_df.groupby('season_x')['cnt_y'].mean().reset_index()
    season_df.rename(columns={'season_x': 'season', 'cnt_y': 'avg_rentals'}, inplace=True)
    season_df['season'] = season_df['season'].str.capitalize()
    
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(
        x='season', 
        y='avg_rentals', 
        data=season_df.sort_values(by='avg_rentals', ascending=False), 
        palette='Blues_r', 
        ax=ax
    )
    ax.set_title("Rata-rata Penyewaan Berdasarkan Musim", fontsize=14)
    ax.set_xlabel("Musim", fontsize=12)
    ax.set_ylabel("Rata-rata Penyewaan", fontsize=12)
    st.pyplot(fig)
    st.write("Dari grafik di atas, dapat diketahui bahwa musim gugur memiliki rata-rata jumlah peminjaman sepeda harian paling tinggi sepanjang tahun 2011–2012.")
    

with col_b:
    st.subheader("2. Bagaimana perbandingan rata-rata jumlah peminjaman sepeda harian antara hari kerja (workingday = 1) dan hari libur/akhir pekan (workingday = 0) selama 2011–2012?")
    
    workingday_df = filtered_df.groupby('workingday_x')['cnt_y'].mean().reset_index()
    workingday_df.rename(columns={'workingday_x': 'workingday', 'cnt_y': 'avg_rentals'}, inplace=True)
    workingday_df['workingday'] = workingday_df['workingday'].str.capitalize()
    
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(
        x='workingday', 
        y='avg_rentals', 
        data=workingday_df, 
        palette='Blues', 
        ax=ax
    )
    ax.set_title("Rata-rata Penyewaan: Hari Kerja vs Akhir Pekan", fontsize=14)
    ax.set_xlabel("Kategori Hari", fontsize=12)
    ax.set_ylabel("Rata-rata Penyewaan", fontsize=12)
    st.pyplot(fig)
    st.write("Dari grafik di atas, dapat diketahui bahwa rata-rata peminjaman sepeda harian lebih tinggi pada hari kerja (workingday = 1) dibandingkan dengan hari libur/akhir pekan (workingday = 0) selama tahun 2011–2012.")
