import streamlit as st
import pandas as pd
import plotly.express as px

# Set Streamlit page configuration
st.set_page_config(page_title="NHANES 2013-2014 Interactive Visualization", layout="wide")

# Title
st.title("NHANES 2013-2014 Age Prediction Subset - Interactive Visualization")

# Load dataset (replace the URL with the actual dataset path)
@st.cache_data
def load_data():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00485/NHANES_2013-2014.csv"
    df = pd.read_csv(url)
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("Filter Data")

# Example filter: Gender if available
if 'Gender' in df.columns:
    gender_options = df['Gender'].unique().tolist()
    selected_gender = st.sidebar.multiselect("Select Gender:", gender_options, default=gender_options)
    df = df[df['Gender'].isin(selected_gender)]

# Example filter: Age range
if 'Age' in df.columns:
    min_age, max_age = int(df['Age'].min()), int(df['Age'].max())
    age_range = st.sidebar.slider("Select Age Range:", min_value=min_age, max_value=max_age, value=(min_age, max_age))
    df = df[(df['Age'] >= age_range[0]) & (df['Age'] <= age_range[1])]

# Interactive Scatter Plot
numeric_columns = df.select_dtypes(include='number').columns.tolist()
x_axis = st.selectbox("X-axis:", numeric_columns)
y_axis = st.selectbox("Y-axis:", numeric_columns, index=1)

fig_scatter = px.scatter(df, x=x_axis, y=y_axis, color='Age', 
                         title=f"Scatter Plot of {x_axis} vs {y_axis}",
                         color_continuous_scale='Viridis', height=600)
st.plotly_chart(fig_scatter, use_container_width=True)

# Correlation Heatmap
if st.checkbox("Show Correlation Heatmap"):
    corr = df[numeric_columns].corr()
    fig_heatmap = px.imshow(corr, text_auto=True, color_continuous_scale='RdBu_r',
                            title="Correlation Heatmap", height=600)
    st.plotly_chart(fig_heatmap, use_container_width=True)

# Histogram for Age Distribution
if 'Age' in df.columns:
    fig_hist = px.histogram(df, x='Age', nbins=30, color_discrete_sequence=['#636EFA'],
                            title="Age Distribution")
    st.plotly_chart(fig_hist, use_container_width=True)

# Instructions
st.markdown("---")
st.markdown("**Instructions:**")
st.markdown("- Use the sidebar filters to explore different subsets of the data.")
st.markdown("- Select variables for the scatter plot using the dropdowns.")
st.markdown("- Check the box to view the correlation heatmap.")

