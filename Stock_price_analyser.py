import pandas as pd
import streamlit as st
import yfinance as yf
import datetime

# how to add title on top of the page
st.write(
    """
    # Stock Price Analyser

    Shown are the stock prices of Apple
    """

)

# name for Apple's stock price data .
# AAPL - code for aPPLES COMPANY 
# ticker_symbol = "AAPL"
ticker_symbol = st.text_input("Enter the Stock Symbol",
                              "AAPL",
                              key="placeholder")

# The Ticker module, which allows you to access ticker data 
ticker_data = yf.Ticker(ticker_symbol);

# Creating Columns for input field
col1, col2 = st.columns(2)


# user can select date of their choice
with col1:
    start_date = st.date_input("Starting date", 
                    datetime.date(2019,1,1)
                    )


# user can select date of their choice
with col2:
    end_date = st.date_input("Ending date", 
                    datetime.date(2023,1,1)
                    )


# get historical data
st.write(
        f"""
        # {ticker_symbol}'s Data
        
        """)
ticker_df = ticker_data.history(period="1d", 
                                start=f"{start_date}", 
                                end=f"{end_date}")

st.dataframe(ticker_df)

st.write("""
        ## Daily Closing chart
    """)
## Showcasing charts
st.line_chart(ticker_df.Close)

st.write("""
        ## Daily Volume chart
    """)
## Showcasing charts
st.line_chart(ticker_df.Volume)



