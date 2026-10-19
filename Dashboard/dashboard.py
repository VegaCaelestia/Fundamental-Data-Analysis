
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv('main_df.csv')

# Menentukan fungsi helper yang adaptif dengan nama kolom yang ada di dataset
def get_column_name(df, options):
    for opt in options:
        if opt in df.columns:
            return opt
    return None

def create_season_rentals_df(df):
    df_copy = df.copy()
    
    # Deteksi nama kolom yang sesuai
    season_col = get_column_name(df_copy, ['season_x', 'season_y', 'season'])
    cnt_col = get_column_name(df_copy, ['cnt_x', 'cnt_y', 'cnt'])
    
    if not season_col or not cnt_col:
        raise KeyError(f"Kolom untuk season/cnt tidak ditemukan. Kolom yang ada: {list(df_copy.columns)}")
    
    # Jika datanya sudah berupa label teks (seperti 'spring', 'summer') kita cukup merapikan huruf kapitalnya
    if df_copy[season_col].dtype == 'object':
        df_copy['season_label'] = df_copy[season_col].str.capitalize()
    else:
        season_mapping = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
        df_copy['season_label'] = df_copy[season_col].map(season_mapping)
        
    season_df = df_copy.groupby('season_label')[cnt_col].mean().reset_index()
    season_df.rename(columns={cnt_col: 'avg_rentals'}, inplace=True)
    return season_df

def create_workingday_rentals_df(df):
    df_copy = df.copy()
    
    # Deteksi nama kolom yang sesuai
    wd_col = get_column_name(df_copy, ['workingday_x', 'workingday_y', 'workingday'])
    cnt_col = get_column_name(df_copy, ['cnt_x', 'cnt_y', 'cnt'])
    
    if not wd_col or not cnt_col:
        raise KeyError(f"Kolom untuk workingday/cnt tidak ditemukan. Kolom yang ada: {list(df_copy.columns)}")
    
    if df_copy[wd_col].dtype == 'object':
        df_copy['workingday_label'] = df_copy[wd_col].str.title()
    else:
        workingday_mapping = {0: 'Weekend/Holiday', 1: 'Working Day'}
        df_copy['workingday_label'] = df_copy[wd_col].map(workingday_mapping)
        
    workingday_df = df_copy.groupby('workingday_label')[cnt_col].mean().reset_index()
    workingday_df.rename(columns={cnt_col: 'avg_rentals'}, inplace=True)
    return workingday_df

# Memproses data menggunakan helper function di atas
season_rentals = create_season_rentals_df(df)
workingday_rentals = create_workingday_rentals_df(df)

# --- Visualisasi Streamlit ---
st.title('Bike Sharing Dashboard 🚲')
st.markdown('Dashboard sederhana untuk menganalisis tren peminjaman sepeda selama tahun 2011–2012.')

# Pertanyaan 1
st.subheader('1. Rata-rata Peminjaman Sepeda Berdasarkan Musim')
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(
    x='season_label',
    y='avg_rentals',
    data=season_rentals.sort_values(by='avg_rentals', ascending=False),
    palette='Blues_r',
    ax=ax
)
ax.set_title('Rata-rata Peminjaman Sepeda Harian per Musim', fontsize=15)
ax.set_xlabel('Musim', fontsize=12)
ax.set_ylabel('Rata-rata Jumlah Peminjaman', fontsize=12)
st.pyplot(fig)

# Pertanyaan 2
st.subheader('2. Perbandingan Peminjaman Sepeda: Hari Kerja vs Akhir Pekan/Hari Libur')
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(
    x='workingday_label',
    y='avg_rentals',
    data=workingday_rentals.sort_values(by='avg_rentals', ascending=False),
    palette='Set2',
    ax=ax2
)
ax2.set_title('Rata-rata Peminjaman Sepeda: Hari Kerja vs Akhir Pekan', fontsize=15)
ax2.set_xlabel('Kategori Hari', fontsize=12)
ax2.set_ylabel('Rata-rata Jumlah Peminjaman', fontsize=12)
st.pyplot(fig2)
