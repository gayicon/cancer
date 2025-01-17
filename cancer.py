import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset from the raw GitHub link
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/gayicon/cancer/main/Thyroid_Diff.csv"
    return pd.read_csv(url)

# Load data
df = load_data()

# Streamlit app title
st.title("📊 Differentiated Thyroid Cancer Recurrence Analysis")

# Sidebar navigation
st.sidebar.title("Visualization Options")
viz_option = st.sidebar.radio(
    "Select Visualization",
    ["Correlation Heatmap", "Category Distribution", "Scatter Plot Analysis"]
)

# 1. Correlation Heatmap
if viz_option == "Correlation Heatmap":
    st.subheader("🔎 Correlation Heatmap of Numerical Features")
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    corr_matrix = df[numeric_cols].corr()

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

# 2. Category Distribution (Pie Chart)
elif viz_option == "Category Distribution":
    st.subheader("🟠 Category Distribution")
    categorical_cols = df.select_dtypes(include=['object']).columns
    selected_cat_feature = st.selectbox("Select a categorical feature:", categorical_cols)

    fig_pie = px.pie(
        df,
        names=selected_cat_feature,
        title=f"Distribution of {selected_cat_feature}",
        hole=0.4
    )
    st.plotly_chart(fig_pie)

# 3. Scatter Plot Analysis
elif viz_option == "Scatter Plot Analysis":
    st.subheader("📈 Scatter Plot Analysis")
    num_features = df.select_dtypes(include=['float64', 'int64']).columns

    x_axis = st.selectbox("Select X-axis feature:", num_features)
    y_axis = st.selectbox("Select Y-axis feature:", num_features)
    color_feature = st.selectbox("Select feature for color coding:", df.columns)

    fig_scatter = px.scatter(
        df,
        x=x_axis,
        y=y_axis,
        color=color_feature,
        size_max=10,
        title=f"{x_axis} vs {y_axis} Colored by {color_feature}",
        opacity=0.7
    )
    st.plotly_chart(fig_scatter)
