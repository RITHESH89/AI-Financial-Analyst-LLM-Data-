import yfinance as yf
from langchain.chat_models import ChatOpenAI


def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="5d")

    latest_price = hist["Close"].iloc[-1]
    prev_price = hist["Close"].iloc[-2]

    change = latest_price - prev_price
    percent_change = (change / prev_price) * 100

    return {
        "price": round(latest_price, 2),
        "change": round(change, 2),
        "percent_change": round(percent_change, 2)
    }


def generate_analysis(data, ticker):
    llm = ChatOpenAI(temperature=0)

    prompt = f"""
    You are a financial analyst.

    Analyze the stock {ticker} based on:
    Price: {data['price']}
    Change: {data['change']}
    Percent Change: {data['percent_change']}%

    Give:
    - Trend (Bullish/Bearish)
    - Short explanation
    - Simple advice (Buy/Hold/Sell)
    """

    response = llm.predict(prompt)
    return response
