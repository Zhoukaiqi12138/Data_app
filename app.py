import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Load dataset
st.title('California Housing Data (1990)')
df = pd.read_csv('housing.csv')

# Population filter (slider)
population_filter = st.slider('Minimal Population:', 0, int(df['population'].max()), 20000)

# Ocean proximity filter (multiselect)
type_filter = st.sidebar.multiselect(
    'Choose the location type',
    df['ocean_proximity'].unique(), 
    df['ocean_proximity'].unique())

# Income level filter (radio button)
income_level = st.radio(
    "Choose Income Level:",
    ('Low (≤ 2.5)', 'Medium (> 2.5 & < 4.5)', 'High (> 4.5)')
)

# Filter the DataFrame based on income level
if income_level == 'Low (≤ 2.5)':
    filtered_df = df[df['median_income'] <= 2.5]
elif income_level == 'Medium (> 2.5 & < 4.5)':
    filtered_df = df[(df['median_income'] > 2.5) & (df['median_income'] < 4.5)]
else:
    filtered_df = df[df['median_income'] > 4.5]

# Apply population and location type filters
filtered_df = filtered_df[(filtered_df['population'] >= population_filter) & 
                          (filtered_df['ocean_proximity'].isin(type_filter))]

# Display map
st.write("Map View of Filtered Data:")
st.map(filtered_df[['latitude', 'longitude']])

# Display histogram
st.write("Histogram of Median House Value:")
plt.figure(figsize=(10, 6))
plt.hist(filtered_df['median_house_value'], bins=30, edgecolor='black')
plt.xlabel('Median House Value')
plt.ylabel('Frequency')
plt.title('Histogram of Median House Value')
st.pyplot(plt)
