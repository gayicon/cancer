import pandas as pd
import plotly.express as px
import streamlit as st

# Streamlit App Title
st.title("Differentiated Thyroid Cancer Recurrence Analysis")

# Load dataset from GitHub
@st.cache_data
def load_data():
    url = "https://github.com/gayicon/cancer/blob/main/Thyroid_Diff.csv"
    return pd.read_csv(url)

# Load the data
df = load_data()

# Show dataset preview
st.subheader("Dataset Preview")
st.write(df.head())

# Basic dataset information
st.subheader("Dataset Summary")
st.write(df.describe())

# User selects feature for analysis
feature = st.selectbox("Select a Feature for Analysis", df.columns)

# Check for 'Recurrence' column
if 'Recurrence' in df.columns:
    # Interactive bar plot
    fig = px.histogram(df, x=feature, color='Recurrence',
                       barmode='group',
                       title=f'Recurrence Distribution by {feature}',
                       labels={'Recurrence': 'Recurrence Status'},
                       color_discrete_sequence=['green', 'red'])
    
    # Display the plot
    st.plotly_chart(fig)
else:
    st.warning("The dataset must contain a 'Recurrence' column for analysis.")
