import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
plt.style.use('dark_background')

def create_df_yr(df):
  #the function to get the year DataFrame
  df_year = df.groupby('year').instant.nunique().reset_index()
  df_year.rename(
    columns={
      'instant': 'sum'
    },
    inplace=True,
  )

  return df_year


def create_df_holiday(df):
  #the function to get the holiday DataFrame
  df_holiday = df.groupby('holiday').instant.nunique().reset_index()
  df_holiday.rename(
    columns={
      'instant': 'sum'
    },
    inplace=True,
  )

  return df_holiday


def create_df_working_day(df):
  #the function to get the working day DataFrame
  df_workingday = df.groupby('workingday').instant.nunique().reset_index()
  df_workingday.rename(
    columns={
      'instant': 'sum'
    },
    inplace=True,
  )

  return df_workingday


def create_df_weathercond(df):
  #the function to get the weathersit DataFrame
  df_weathercond = df.groupby('weather_condition').instant.nunique().reset_index()
  df_weathercond.rename(
    columns={
      'instant': 'sum'
    },
    inplace=True,
  )

  return df_weathercond

def create_df_season(df):
  #the function to get the season DataFrame
  df_season = df.groupby('season').instant.nunique().reset_index()
  df_season.rename(
    columns={
      'instant': 'sum'
    },
    inplace=True,
  )

  return df_season

def sidebar(df):
  #the function to create sidebar"""
  df['date'] = pd.to_datetime(df['date'])
  min_date = df['date'].min()
  max_date = df['date'].max()

  with st.sidebar:
    st.image('./assets/bike_sharing.jpg')

    def on_change():
      st.session_state.date = date

    date = st.date_input(
      label='Time Span',
      value=[min_date, max_date],
      min_value=min_date,
      max_value=max_date,
      on_change=on_change
    )

    return date


def year(df):
  #the function to create totals of bike sharing by year
  st.subheader('Year')

  fig, ax = plt.subplots(figsize=(20, 12.6))
  plt.grid(color='whitesmoke', linestyle='dashed', linewidth=1.5)
  plt.margins(0.1)
  sns.barplot(
    data=df.sort_values(by='year', ascending=False),
    x='sum',
    y='year',
    palette=['dodgerblue', 'orange'],
    orient='h',
    ax=ax,
  )

  ax.set_title(
    'Total of Bike Sharing by Year',
    loc='center',
    fontsize=50,
    pad=25,
  )
  ax.set_xlabel('Total', fontsize=30)
  ax.set_ylabel('Year', fontsize=30)
  ax.tick_params(axis='x', labelsize=25)
  ax.tick_params(axis='y', labelsize=25)
  ax.bar_label(ax.containers[0], fontsize=30, padding=20)
  st.pyplot(fig)


def month(df):
  #the function to create totals of bike sharing by month
  st.subheader('Month')

  fig, ax = plt.subplots(figsize=(20, 12))
  plt.grid(color='whitesmoke', linestyle='dashed', linewidth=1.5)
  plt.margins(0.1)
  sns.barplot(
    data=df.sort_values(by='month', ascending=False),
    x='count',
    y='month',
    palette=['darkgoldenrod', 'navajowhite', 'peru', 'linen'],
    orient='h',
    ax=ax,
  )

  ax.set_title(
    'Total of Bike Sharing by Month',
    loc='center',
    fontsize=50,
    pad=25,
  )
  ax.set_xlabel('Total', fontsize=30)
  ax.set_ylabel('Month', fontsize=30)
  ax.tick_params(axis='x', labelsize=25)
  ax.tick_params(axis='y', labelsize=25)
  ax.bar_label(ax.containers[0], fontsize=30, padding=20)
  st.pyplot(fig)


def hour(df):
  #the function to create totals of bike sharing by hour
  st.subheader('Hour')

  fig, ax = plt.subplots(figsize=(20, 12))
  plt.grid(color='whitesmoke', linestyle='dashed', linewidth=1.5)
  plt.margins(0.1)
  sns.barplot(
    data=df.sort_values(by='hr', ascending=False),
    x='cnt',
    y='hr',
    palette=['lightcoral', 'orange', 'yellow', 'lightgreen', 'lightskyblue', 'violet', 'lightpink'],
    orient='h',
    ax=ax,
  )

  ax.set_title(
    'Total of Bike Sharing by Hour',
    loc='center',
    fontsize=50,
    pad=25,
  )
  ax.set_xlabel('Hour', fontsize=30)
  ax.set_ylabel('Total', fontsize=30)
  ax.tick_params(axis='x', labelsize=25)
  ax.tick_params(axis='y', labelsize=25)
  ax.bar_label(ax.containers[0], fontsize=24, padding=20)
  st.pyplot(fig)


def holiday(df):
  #the function to create totals of bike sharing by holiday
  st.write('Holiday')

  fig, ax = plt.subplots(figsize=(16, 18))
  plt.grid(color='whitesmoke', linestyle='dashed', linewidth=1.5)
  plt.margins(0.1)
  sns.barplot(
    data=df.sort_values(by='holiday', ascending=False),
    x='holiday',
    y='sum',
    palette=['maroon', 'goldenrod'],
    ax=ax,
  )

  ax.set_title(
    'Total of Bike Sharing by Holiday',
    loc='center',
    fontsize=50,
    pad=25,
  )
  ax.set_xlabel(None)
  ax.set_ylabel('Total', fontsize=40)
  ax.tick_params(axis='x', labelsize=35)
  ax.tick_params(axis='y', labelsize=35)
  ax.bar_label(ax.containers[0], fontsize=30, padding=20)
  st.pyplot(fig)


def working_day(df):
  #the function to create totals of bike sharing by workingday
  st.write('Working Day')

  fig, ax = plt.subplots(figsize=(16, 18))
  plt.grid(color='whitesmoke', linestyle='dashed', linewidth=1.5)
  plt.margins(0.1)
  sns.barplot(
    data=df.sort_values(by='workingday', ascending=False),
    x='workingday',
    y='sum',
    palette=['lightskyblue', 'lightcoral'],
    ax=ax,
  )

  ax.set_title(
    'Total of Bike Sharing by Working Day',
    loc='center',
    fontsize=50,
    pad=25,
  )
  ax.set_xlabel(None)
  ax.set_ylabel('Total', fontsize=40)
  ax.tick_params(axis='x', labelsize=35)
  ax.tick_params(axis='y', labelsize=35)
  ax.bar_label(ax.containers[0], fontsize=30, padding=20)
  st.pyplot(fig)


def weathercond(df):
  #the function to create totals of bike sharing by weather condition
  st.subheader('Weather Condition')

  fig, ax = plt.subplots(figsize=(20, 10))
  plt.grid(color='whitesmoke', linestyle='dashed', linewidth=1.5)
  plt.margins(0.1)
  sns.barplot(
    data=df.sort_values(by='weather_condition', ascending=False),
    x='sum',
    y='weather_condition',
    palette=['darkgoldenrod', 'navajowhite', 'peru', 'linen'],
    orient='h',
    ax=ax,
  )
  
  ax.set_title(
    'Total of Bike Sharing by Weather Condition',
    loc='center',
    fontsize=50,
    pad=25,
  )
  ax.set_xlabel('Total', fontsize=30)
  ax.set_ylabel('Weather', fontsize=30)
  ax.tick_params(axis='x', labelsize=25)
  ax.tick_params(axis='y', labelsize=25)
  ax.bar_label(ax.containers[0], fontsize=30, padding=20)
  st.pyplot(fig)


def season(df):
  #the function to create totals of bike sharing by season
  st.subheader('Season')

  fig, ax = plt.subplots(figsize=(20, 10))
  plt.grid(color='whitesmoke', linestyle='dashed', linewidth=1.5)
  plt.margins(0.1)
  sns.barplot(
    data=df.sort_values(by='season', ascending=False),
    x='sum',
    y='season',
    palette=['lightskyblue', 'orange', 'yellow', 'navajowhite'],
    orient='h',
    ax=ax,
  )

  ax.set_title(
    'Total of Bike Sharing by Season',
    loc='center',
    fontsize=50,
    pad=25,
  )
  ax.set_xlabel('Total', fontsize=30)
  ax.set_ylabel('Season', fontsize=30)
  ax.tick_params(axis='x', labelsize=25)
  ax.tick_params(axis='y', labelsize=25)
  ax.bar_label(ax.containers[0], fontsize=30, padding=20)
  st.pyplot(fig)

