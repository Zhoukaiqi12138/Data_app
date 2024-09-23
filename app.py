import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


st.title('California Housing Data(1990) by Junjie Zheng')
df = pd.read_csv('housing.csv')

price_filter = st.slider('Minimal Median House Price', 0.0, 500001, 200000)

# create a multi select
location_type_filter = st.sidebar.multiselect(
     'Choose the location Type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# create a radio button
income_level = st.sidebar.radio(
    "Choose income level",
    ("Low", "Medium", "High"),
)

if income_level == 'Low':
    df = df[df['median_income'] < 2.5]
elif income_level == 'Medium':
    df = df[(df['median_income'] >= 2.5) & (df['median_income'] < 4.5)]
else:
    df = df[df['median_income'] >= 4.5]

# filter by price
df = df[df.population >= price_filter]

# filter by locationtype
df = df[df.ocean_proximity.isin(location_type_filter)]

# show dataframe
st.subheader('See more filters in the slidebar:')

# show on map
st.map(df)

# show the plot
st.subheader('Histogram of Median House Value')
fig, ax = plt.subplots()
df['median_house_value'].hist(bins=30, ax=ax)
ax.set_xlabel('Median House Value')
ax.set_ylabel('Frequency')
st.pyplot(fig)
