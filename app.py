import streamlit as st
from dotenv import load_dotenv
from utils import get_stock_data, generate_analysis

load_dotenv()

st.set_page_config(page_title="AI Financial Analyst", layout="centered")

st.title("📊 AI Financial Analyst")
st.write("Get AI-powered stock insights instantly")

ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA)")

if ticker:
    with st.spinner("Fetching data..."):
        data = get_stock_data(ticker.upper())

    st.subheader("📈 Stock Data")
    st.write(f"Price: ${data['price']}")
    st.write(f"Change: {data['change']} ({data['percent_change']}%)")

    with st.spinner("Generating AI analysis..."):
        analysis = generate_analysis(data, ticker)

    st.subheader("🤖 AI Analysis")
    st.write(analysis)
