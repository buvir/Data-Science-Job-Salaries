
import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.title('Data Science Salary Explorer & Predictor')

# Load dataset
ds_salaries = pd.read_csv("Data Science Job Salaries.csv")

ds_salaries.drop('Unnamed: 0', axis=1, inplace=True)
ds_salaries.head()



# --- Section 2: Salary Prediction ---
st.header("Predict Data Science & Other Jobs Salary")

# Load model and feature columns
model = joblib.load('salary_predictor.joblib')
model_features = joblib.load('model_features.joblib')

experience_level = st.selectbox('Experience Level', ['Entry-Level/Junior', 'Mid-level/Intermediate', 'Senior-level/Expert', 'Executive-level/Director'])
employment_type = st.selectbox('Employment Type', ['Full-time', 'Part-time', 'Contract', 'Freelance'])
remote_ratio = st.selectbox('Remote Ratio', ['No remote work', 'Partially remote', 'Fully remote'])
company_size = st.selectbox('Company Size', ['Small(<50)', 'Medium(50-250)', 'Large(>250)'])
job_title_pred = st.selectbox('Job Title for Prediction', sorted(ds_salaries['job_title'].unique()))

# Prepare input for prediction
input_dict = {
    'experience_level': [experience_level],
    'employment_type': [employment_type],
    'remote_ratio': [remote_ratio],
    'company_size': [company_size],
    'job_title': [job_title_pred]
}
input_df = pd.DataFrame(input_dict)
input_encoded = pd.get_dummies(input_df)
for col in model_features:
    if col not in input_encoded.columns:
        input_encoded[col] = 0
input_encoded = input_encoded[model_features]

if st.button('Predict Salary'):
    prediction = model.predict(input_encoded)[0]
    st.success(f'Predicted Salary (USD): ${prediction:,.0f}')



# --- Section 1: Data Exploration ---
st.header("Dataset Summary & Visualization")

# Show summary statistics
st.subheader("Summary Statistics")
st.write(ds_salaries.describe())

# Line chart of all salaries
st.subheader("Salary Trend (USD)")
st.line_chart(ds_salaries['salary_in_usd'])

# Filter by job title and show bar chart
st.subheader("Explore Salaries by Job Title")
job_filter = st.selectbox('Select Job Title for Visualization', ds_salaries['job_title'].unique())
filtered_data = ds_salaries[ds_salaries['job_title'] == job_filter]
st.write(filtered_data)
st.bar_chart(filtered_data['salary_in_usd'])