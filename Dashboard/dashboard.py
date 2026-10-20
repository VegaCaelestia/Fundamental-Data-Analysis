import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")


st.title("Dashboard Analisis Penyewaan Sepeda")
st.markdown("Dashboard interaktif sederhana untuk menyajikan hasil analisis data penyewaan sepeda.")


@st.cache_data
def load_data():
    df = pd.read_csv('Dashboard/main_df.csv')
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

    st.sidebar.header("Filter Data")
    year_filter = st.sidebar.multiselect(
        "Pilih Tahun:",
        options=df['dteday'].dt.year.unique(),
        default=df['dteday'].dt.year.unique(),
    filtered_df = df[df['dteday'].dt.year.isin(year_filter)]
    )
    
    daily_df = filtered_df.drop_duplicates(subset=['dteday'])
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Hari Data", len(daily_df))
    with col2:
        st.metric("Rata-rata Penyewaan Harian", f"{daily_df['cnt_y'].mean():.2f}")

    st.header("Hasil Analisis & Kesimpulan")

    col_a, col_b = st.columns(2)
    
    with col_a:
        st.subheader("1. Pengaruh Musim terhadap Penyewaan")
        st.write("Musim gugur (Fall) memiliki rata-rata jumlah peminjaman sepeda harian paling tinggi sepanjang tahun 2011–2012.")
        
        fig, ax = plt.subplots(figsize=(8, 6))
        season_df = daily_df.groupby('season_x')['cnt_y'].mean().reset_index()
        season_df.rename(columns={'season_x': 'season', 'cnt_y': 'avg_rentals'}, inplace=True)
        season_df['season'] = season_df['season'].str.capitalize()
        
        sns.barplot(
            x='season', 
            y='avg_rentals', 
            data=season_df.sort_values(by='avg_rentals', ascending=False), 
            palette='Blues_r',
            ax=ax
        )
        
        ax.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Musim', fontsize=14)
        ax.set_xlabel('Musim', fontsize=12)
        ax.set_ylabel('Rata-rata Penyewaan', fontsize=12)
        st.pyplot(fig)

    with col_b:
        st.subheader("2. Perbandingan Hari Kerja vs Akhir Pekan")
        st.write("Rata-rata peminjaman sepeda harian lebih tinggi pada hari kerja selama tahun 2011–2012.")
        
        fig, ax = plt.subplots(figsize=(8, 6))
        workingday_df = daily_df.groupby('workingday_x')['cnt_y'].mean().reset_index()
        workingday_df.rename(columns={'workingday_x': 'workingday', 'cnt_y': 'avg_rentals'}, inplace=True)
        workingday_df['workingday'] = workingday_df['workingday'].str.capitalize()

        sns.barplot(
            data=workingday_df, 
            x='workingday', 
            y='avg_rentals', 
            palette='Blues', 
            ax=ax
        )
        ax.set_title("Rata-rata Penyewaan: Hari Kerja vs Akhir Pekan", fontsize=14)
        ax.set_xlabel("Kategori Hari", fontsize=12)
        ax.set_ylabel("Rata-rata Jumlah Penyewaan", fontsize=12)
        st.pyplot(fig)
