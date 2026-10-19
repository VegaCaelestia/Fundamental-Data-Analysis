import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

season_rentals = create_season_rentals_df(df)
workingday_rentals = create_workingday_rentals_df(df)

st.title('Bike Sharing Dashboard 🚲')
st.markdown('Dashboard sederhana untuk menganalisis tren peminjaman sepeda selama tahun 2011–2012.')


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
