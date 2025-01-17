import pandas as pd
import plotly.express as px
import streamlit as st

# Set Streamlit page title
st.title("Differentiated Thyroid Cancer Recurrence Analysis")

# Upload Dataset
uploaded_file = st.file_uploader("Upload the Thyroid Cancer Dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    # Load the dataset
    df = pd.read_csv(uploaded_file)
    
    # Show the dataset
    st.subheader("Dataset Preview")
    st.write(df.head())

    # Basic statistics
    st.subheader("Dataset Summary")
    st.write(df.describe())

    # Select column for analysis
    feature = st.selectbox("Select Feature for Analysis", df.columns)

    # Check if the dataset contains a 'Recurrence' column
    if 'Recurrence' in df.columns:
        # Interactive Bar Chart
        fig = px.histogram(df, x=feature, color='Recurrence',
                           barmode='group',
                           title=f'Recurrence vs {feature}',
                           labels={'Recurrence': 'Recurrence Status'},
                           color_discrete_sequence=['green', 'red'])
        st.plotly_chart(fig)
    else:
        st.warning("The dataset must contain a 'Recurrence' column for analysis.")
else:
    st.info("Please upload the dataset to proceed.")
