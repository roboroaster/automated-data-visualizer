import streamlit as st
import pandas as pd
import plotly.express as px
import google.generativeai as genai
import os

# Set your Gemini API key here or use an environment variable
GEMINI_API_KEY = "AIzaSyDgeYoS9kPvb5c9VS9eP7r24_bsLVlzKk4"
genai.configure(api_key=GEMINI_API_KEY)

st.set_page_config(page_title="Automated Data Analysis & Visualization Tool", layout="wide")
st.title("Automated Data Analysis & Visualization Tool")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Data Preview")
    st.dataframe(df.head())

    # Generate summary and insights using Gemini LLM
    with st.spinner("Generating insights with Gemini..."):
        prompt = f"""
        You are a data analyst. Given the following dataset (first 10 rows):\n{df.head(10).to_csv(index=False)}\n\nProvide a summary of the dataset, key insights, and any interesting patterns you notice. Be concise and use natural language.
        """
        try:
            model = genai.GenerativeModel('gemini-2.5-flash')
            response = model.generate_content(prompt)
            summary = response.text
        except Exception as e:
            summary = f"Error generating insights: {e}"
    st.markdown("### Insights & Summary")
    st.write(summary)

    # Visualization selection
    st.markdown("### Create Visualizations")
    columns = df.columns.tolist()
    chart_type = st.selectbox("Select chart type", ["Scatter", "Bar", "Line", "Histogram"])
    x_axis = st.selectbox("X-axis", columns)
    y_axis = st.selectbox("Y-axis", columns)
    if st.button("Generate Chart"):
        fig = None
        if chart_type == "Scatter":
            fig = px.scatter(df, x=x_axis, y=y_axis)
        elif chart_type == "Bar":
            fig = px.bar(df, x=x_axis, y=y_axis)
        elif chart_type == "Line":
            fig = px.line(df, x=x_axis, y=y_axis)
        elif chart_type == "Histogram":
            fig = px.histogram(df, x=x_axis)
        if fig:
            st.plotly_chart(fig, use_container_width=True)

    # Ad-hoc question answering
    st.markdown("### Ask a Question about Your Data")
    user_question = st.text_input("Type your question (e.g., 'What is the average value of column X?')")
    if st.button("Get Answer") and user_question:
        with st.spinner("Thinking..."):
            prompt = f"""
            You are a data analyst. Given the following dataset (first 10 rows):\n{df.head(10).to_csv(index=False)}\n\nUser question: {user_question}\n\nAnswer in detail, using calculations or reasoning as needed.
            """
            try:
                model = genai.GenerativeModel('gemini-2.5-flash')
                response = model.generate_content(prompt)
                answer = response.text
            except Exception as e:
                answer = f"Error: {e}"
        st.write(answer)
else:
    st.info("Please upload a CSV file to get started.") 