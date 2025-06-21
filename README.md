# Automated Data Analysis and Visualization Tool

This tool allows you to upload raw data (CSV files) and automatically:
- Generate insights and summaries using natural language (powered by Gemini LLM)
- Create interactive visualizations (Plotly)
- Answer ad-hoc questions about your dataset

## Features
- **Natural Language Insights:** Get concise summaries and key patterns from your data using Google Gemini LLM.
- **Interactive Visualizations:** Easily create scatter, bar, line, and histogram charts with Plotly.
- **Ad-hoc Q&A:** Ask questions about your data and get instant answers.
- **Streamlit UI:** Simple, modern web interface for data upload and exploration.

## Tech Stack
- Python
- Streamlit
- Pandas
- Plotly
- Google Gemini LLM API (`google-generativeai`)

## Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/roboroaster/automated-data-visualizer.git
   cd automated-data-visualizer
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set your Gemini API key:**
   - Edit `app.py` and set your API key in the `GEMINI_API_KEY` variable, or set the `GEMINI_API_KEY` environment variable.

## Usage
1. **Run the app:**
   ```bash
   streamlit run app.py
   ```
2. **Open your browser:**
   - Go to the local URL shown in the terminal (usually http://localhost:8501)
3. **Upload a CSV file:**
   - Preview your data, generate insights, create visualizations, and ask questions!

## License
This project is private. Contact the author for licensing information. 