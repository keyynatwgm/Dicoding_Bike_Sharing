"""
Author: Kezia Natalia
Date: 04/03/2023
This is the main.py module.
Usage:
- Main streamlit file dan run the streamlit dashboard
"""

import datetime
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from dashboard.function import (
  create_df_yr, create_df_holiday, create_df_working_day,
  create_df_weathercond, create_df_season, sidebar, year,
  month, hour, holiday, working_day, weathercond, season,
)


if __name__ == '__main__':
  st.header('🚴🏻‍♂️ Bike Sharing Dashboard 🚴🏻‍♂️')

  DF_CLEAN_PATH = 'dashboard/bike_data_clean.csv'
  DF_HOUR_PATH = 'data/hour.csv'

  df = pd.read_csv(DF_CLEAN_PATH)
  df_hour = pd.read_csv(DF_HOUR_PATH)

  date = sidebar(df)
  if len(date) == 2:
    df_main = df[
      (df["date"] >= str(date[0])) & (df["date"] <= str(date[1]))
    ]
  else:
    df_main = df[
      (df["date"] >= str(st.session_state.date[0])) & (
        df["date"] <= str(st.session_state.date[1])
      )
    ]

  with st.container():
    st.subheader('Time Based Statistics')
    tab_year, tab_month, tab_hour = st.tabs(['Year', 'Month', 'Hour'])
    df_year = create_df_yr(df_main)

    with tab_year:
      year(df_year)

    with tab_month:
      month(df_main)

    with tab_hour:
      hour(df_hour)

  with st.container():
    st.subheader('Statistics based on Holidays and Workingday')
    col_holiday, col_workingday = st.columns([1, 1])

    with col_holiday:
      df_holiday = create_df_holiday(df_main)
      holiday(df_holiday)

      with st.expander('note'):
        st.write(
          """
          `Not Holiday`: Bukan hari libur  
          `Holiday`: Hari libur (tanggal merah)
          """
        )

    with col_workingday:
      df_workingday = create_df_working_day(df_main)
      working_day(df_workingday)

      with st.expander('Note'):
        st.write(
          """
          `Working Day`: Hari kerja  
          `Holiday`: Hari libur
          """
        )

  with st.container():
    df_weathercond = create_df_weathercond(df_main)
    weathercond(df_weathercond)

    with st.expander('Note'):
      st.write(
        """
        `Mist + Cloudy`: Berkabut dan berawan  
        `Light Snow`: Sedikit bersalju  
        `Clear`: Cuaca cerah
        """
      )

  with st.container():
    df_season = create_df_season(df_main)
    season(df_season)

    with st.expander('Note'):
      st.write(
        """
        `Winter`: Musim Dingin  
        `Summer`: Musim Panas  
        `Spring`: Musim Semi  
        `Fall`: Musim Gugur
        """
      )

  main_df = df[(df["date"] >= str(date[0])) & (df["date"] <= str(date[0]))]

  ##Correlation
  st.subheader("Correlation")
  fig_correlation, ax = plt.subplots(figsize=(24, 10))

  correlation = df.corr(numeric_only=True)
  mask = np.triu(np.ones_like(correlation, dtype=bool))

  sns.heatmap(
      correlation,
      annot=True,
      mask=mask,
      cmap="mako",
      center=0,
      annot_kws={"size": 16},
      fmt=".2f")
  plt.title("Correlation Heatmap", fontsize=21)

  st.pyplot(fig_correlation)
  with st.expander('Note'):
      st.write(
        """
        * `atemp` dan `temp` sangat berkorelasi (0.99).
        * `humidity` memiliki korelasi lemah dengan temp dan atemp (0.13 dan 0.14).
        * `casual` cukup berkorelasi dengan `temp` dan `atemp` (0.54), dan sedikit negatif dengan `humidity` (-0.072).
        * `registered` memiliki pola yang sama seperti casual, dan berkorelasi moderat dengan `casual` (0.39).
        * `total_count` berkorelasi kuat dengan `temp`, `atemp`, `casual`, dan `registered` (0.63, 0.63, 0.67, dan 0.94), dan sedikit negatif dengan `humidity` (-0.092).
        """
      )

  year_now = datetime.date.today().year
  NAME = "[Kezia Natalia](https://www.linkedin.com/in/kezia-natalia-wgm/ 'Kezia Natalia | LinkedIn')"
  COPYRIGHT = 'Copyright © ' + str(year_now) + ' ' + NAME
  st.caption(COPYRIGHT)