import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

st.title('California Housing Data (1990)')

# Load the dataset
df = pd.read_csv('housing.csv')


population_filter = st.slider('Minimal Median House Price:', 0, 500001, 20000)  # min, max, default
# Multi-select for ocean proximity
type_filter = st.sidebar.multiselect(
    'Choose the location type',
    df['ocean_proximity'].unique(),  # options
    df['ocean_proximity'].unique())  # defaults to all

# Radio button for income level filter
income_level = st.radio(
    "Choose Income Level:",
    ('Low (≤ 2.5)', 'Medium (> 2.5 & < 4.5)', 'High (> 4.5)')
)

# Filter the DataFrame based on the income level selection
if income_level == 'Low (≤ 2.5)':
    filtered_df = df[df['median_income'] <= 2.5]
elif income_level == 'Medium (> 2.5 & < 4.5)':
    filtered_df = df[(df['median_income'] > 2.5) & (df['median_income'] < 4.5)]
else:
    filtered_df = df[df['median_income'] > 4.5]

# Apply the population and location type filters
filtered_df = filtered_df[(filtered_df['population'] >= population_filter) &
                          (filtered_df['ocean_proximity'].isin(type_filter))]

# Show map of filtered data
st.write("Map View of Filtered Data:")
st.map(filtered_df[['latitude', 'longitude']])

# Histogram of the median house value
st.write("Histogram of Median House Value:")

# Plotting the histogram of median house value
plt.figure(figsize=(10, 6))
plt.hist(filtered_df['median_house_value'], bins=30, edgecolor='black')
plt.xlabel('Median House Value')
plt.ylabel('Frequency')
plt.title('Histogram of Median House Value')
st.pyplot(plt)
