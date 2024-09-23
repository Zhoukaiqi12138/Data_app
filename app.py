import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


st.title('California Housing Data (1990)')
df = pd.read_csv('housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
price_filter = st.slider('Minimal Population (Millions):', 0.0, 500001, 200000)  # min, max, default

# create a multi select
type_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

income_level = st.radio(
    "Choose Income Level:",
    ('Low (≤ 2.5)', 'Medium (> 2.5 & < 4.5)', 'High (> 4.5)')
)

# Filter the DataFrame based on radio button selection
if income_level == 'Low (≤ 2.5)':
    filtered_df = df[df['median_income'] <= 2.5]
elif income_level == 'Medium (> 2.5 & < 4.5)':
    filtered_df = df[(df['median_income'] > 2.5) & (df['median_income'] < 4.5)]
else:
    filtered_df = df[df['median_income'] > 4.5]



# show on map
st.map(df)

st.write("Map View of Filtered Data:")
st.map(filtered_df[['latitude', 'longitude']])

# Histogram of the median house value
st.write("Histogram of Median House Value:")

# Plotting the histogram
plt.figure(figsize=(10, 6))
plt.hist(filtered_df['median_house_value'], bins=30, edgecolor='black')
plt.xlabel('Median House Value')
plt.ylabel('Frequency')
plt.title('Histogram of Median House Value')