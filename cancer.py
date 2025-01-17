import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("Differentiated Thyroid Cancer Recurrence Analysis")

# Load Data
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/gayicon/cancer/main/Thyroid_Diff.csv"
    df = pd.read_csv(url)
    return df

df = load_data()

# Select only numeric columns for correlation
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Check if numeric data exists
if not numeric_df.empty:
    corr_matrix = numeric_df.corr()

    # Correlation Heatmap
    st.subheader("Correlation Heatmap (Numeric Features)")
    fig = px.imshow(
        corr_matrix,
        text_auto=True,
        color_continuous_scale='Viridis',
        title="Correlation Heatmap"
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No numeric data available for correlation.")

