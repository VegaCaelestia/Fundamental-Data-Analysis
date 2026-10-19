
"""
# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# 
# # Set page config
# st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")
# 
# # Title
# st.title("📊 Dashboard Analisis Penyewaan Sepeda")
# st.markdown("Dashboard interaktif sederhana untuk menyajikan hasil analisis data penyewaan sepeda.")
# 
# # Load Data
# @st.cache_data
# def load_data():
#     # Membaca data dari file yang tersedia
#     df = pd.read_csv('/content/main_df.csv')
#     df['dteday'] = pd.to_datetime(df['dteday'])
#     return df
# 
# try:
#     df = load_data()
# except Exception as e:
#     st.error(f"Gagal memuat data: {e}")
#     df = None
# 
# if df is not None:
#     # Sidebar filter
#     st.sidebar.header("Filter Data")
#     year_filter = st.sidebar.multiselect(
#         "Pilih Tahun:",
#         options=df['dteday'].dt.year.unique(),
#         default=df['dteday'].dt.year.unique()
#     )
# 
#     # Filter data berdasarkan tahun
#     filtered_df = df[df['dteday'].dt.year.isin(year_filter)]
# 
#     # Menampilkan metrik sederhana
#     col1, col2 = st.columns(2)
#     with col1:
#         st.metric("Total Transaksi/Data", len(filtered_df))
#     with col2:
#         st.metric("Rata-rata Penyewaan Harian", f"{filtered_df['cnt'].mean():.2f}")
# 
#     st.markdown("---")
# 
#     # Pertanyaan 1 & 2
#     st.header("📌 Hasil Analisis & Kesimpulan")
# 
#     col_a, col_b = st.columns(2)
# 
#     with col_a:
#         st.subheader("1. Pengaruh Musim terhadap Penyewaan")
#         st.write("**Kesimpulan:** Musim gugur memiliki rata-rata jumlah peminjaman sepeda harian paling tinggi sepanjang tahun 2011–2012.")
#         # Contoh visualisasi sederhana (jika kolom musim ada, atau tampilkan trend keseluruhan harian)
#         fig, ax = plt.subplots(figsize=(6, 4))
#         sns.lineplot(data=filtered_df, x='dteday', y='cnt', ax=ax, color='orange')
#         ax.set_title("Tren Penyewaan Sepeda Harian")
#         ax.set_xlabel("Tanggal")
#         ax.set_ylabel("Jumlah Penyewaan")
#         plt.xticks(rotation=45)
#         st.pyplot(fig)
# 
#     with col_b:
#         st.subheader("2. Perbandingan Hari Kerja vs Akhir Pekan")
#         st.write("**Kesimpulan:** Rata-rata peminjaman sepeda harian lebih tinggi pada hari kerja selama tahun 2011–2012.")
#         # Tambahkan visualisasi boxplot sederhana
#         fig, ax = plt.subplots(figsize=(6, 4))
#         if 'workingday' in filtered_df.columns:
#             sns.barplot(data=filtered_df, x='workingday', y='cnt', ax=ax, palette='Blues')
#             ax.set_xticklabels(['Akhir Pekan / Libur', 'Hari Kerja'])
#         else:
#             # fallback jika kolom workingday tidak langsung terdeteksi
#             filtered_df['is_weekday'] = filtered_df['dteday'].dt.dayofweek < 5
#             sns.barplot(data=filtered_df, x='is_weekday', y='cnt', ax=ax, palette='Blues')
#             ax.set_xticklabels(['Akhir Pekan', 'Hari Kerja'])
#         ax.set_title("Rata-rata Penyewaan: Hari Kerja vs Akhir Pekan")
#         ax.set_xlabel("Kategori Hari")
#         ax.set_ylabel("Rata-rata Jumlah Penyewaan")
#         st.pyplot(fig)
