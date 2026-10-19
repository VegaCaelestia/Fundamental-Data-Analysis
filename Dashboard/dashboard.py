import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
# Set page config
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")
 
# Title
st.title("📊 Dashboard Analisis Penyewaan Sepeda")
st.markdown("Dashboard interaktif sederhana untuk menyajikan hasil analisis data penyewaan sepeda.")
 
# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('Dashboard/main_df.csv')
    df['dteday'] = pd.to_datetime(df['dteday'])
    
    # Membuat kolom 'season' otomatis jika belum ada
    if 'season' not in df.columns:
        def assign_season(month):
            if month in [3, 4, 5]: return 2      # Musim Semi
            elif month in [6, 7, 8]: return 3   # Musim Panas
            elif month in [9, 10, 11]: return 4 # Musim Gugur
            else: return 1                      # Musim Dingin
        df['season'] = df['dteday'].dt.month.apply(assign_season)
        
    # Membuat kolom 'workingday' otomatis jika belum ada
    if 'workingday' not in df.columns:
        df['workingday'] = (df['dteday'].dt.dayofweek < 5).astype(int)
        
    return df
 
try:
    df = load_data()
except Exception as e:
    st.error(f"Gagal memuat data: {e}")
    df = None
 
if df is not None:
    # Sidebar filter
    st.sidebar.header("Filter Data")
    year_filter = st.sidebar.multiselect(
        "Pilih Tahun:",
        options=df['dteday'].dt.year.unique(),
        default=df['dteday'].dt.year.unique()
    )
    
    # Filter data berdasarkan tahun
    filtered_df = df[df['dteday'].dt.year.isin(year_filter)]
 
    # Menampilkan metrik sederhana
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Transaksi/Data", len(filtered_df))
    with col2:
        st.metric("Rata-rata Penyewaan Harian", f"{filtered_df['cnt'].mean():.2f}")
 
    st.markdown("---")
 
    # Pertanyaan 1 & 2
    st.header("📌 Hasil Analisis & Kesimpulan")
 
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.subheader("1. Pengaruh Musim terhadap Penyewaan")
        st.write("**Kesimpulan:** Musim gugur memiliki rata-rata jumlah peminjaman sepeda harian paling tinggi sepanjang tahun 2011–2012.")
        
        fig, ax = plt.subplots(figsize=(8, 6))
        season_df = filtered_df.groupby('season')['cnt'].mean().reset_index()
        
        season_names = {1: 'Musim Semi', 2: 'Musim Panas', 3: 'Musim Gugur', 4: 'Musim Dingin'}
        season_df['season_name'] = season_df['season'].map(season_names)
        
        sns.barplot(
            x='season_name', 
            y='cnt', 
            data=season_df, 
            palette=['#87CEEB', '#FFA500', '#FF4500', '#4682B4'],
            ax=ax
        )
        
        ax.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Musim', fontsize=14)
        ax.set_xlabel('Musim', fontsize=12)
        ax.set_ylabel('Rata-rata Penyewaan', fontsize=12)
        st.pyplot(fig)
 
    with col_b:
        st.subheader("2. Perbandingan Hari Kerja vs Akhir Pekan")
        st.write("**Kesimpulan:** Rata-rata peminjaman sepeda harian lebih tinggi pada hari kerja selama tahun 2011–2012.")
        
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.barplot(data=filtered_df, x='workingday', y='cnt', ax=ax, palette='Blues')
        ax.set_xticklabels(['Akhir Pekan / Libur', 'Hari Kerja'])
        ax.set_title("Rata-rata Penyewaan: Hari Kerja vs Akhir Pekan")
        ax.set_xlabel("Kategori Hari")
        ax.set_ylabel("Rata-rata Jumlah Penyewaan")
        st.pyplot(fig)
