import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset from the raw GitHub link
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/gayicon/cancer/main/Thyroid_Diff.csv"
    return pd.read_csv(url)

# Load data
df = load_data()

# Streamlit app title
st.title("Differentiated Thyroid Cancer Recurrence Analysis")

# Display dataset preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Select feature for visualization
st.subheader("Interactive Visualization")
selected_feature = st.selectbox("Select a feature to analyze:", df.columns)

# Plot interactive histogram
fig = px.histogram(df, x=selected_feature, title=f"Distribution of {selected_feature}")
st.plotly_chart(fig)

# Add optional filtering
st.subheader("Filter by Feature")
filter_feature = st.selectbox("Select a feature to filter:", df.columns)
filter_value = st.text_input(f"Enter value to filter {filter_feature}:")

if filter_value:
    filtered_df = df[df[filter_feature].astype(str) == filter_value]
    st.dataframe(filtered_df)
    st.subheader(f"Filtered {selected_feature} Distribution")
    fig_filtered = px.histogram(filtered_df, x=selected_feature, title=f"Filtered Distribution of {selected_feature}")
    st.plotly_chart(fig_filtered)
