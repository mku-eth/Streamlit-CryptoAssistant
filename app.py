import streamlit as st
import yfinance as yf
import pandas as pd

from helpers import relative_return, download_csv

tickers = ('BTC-USD', 'ETH-USD', 'LTC-USD', 'DOGE-USD', 'XRP-USD', 'ADA-USD')
cryptos = ('BTC', 'ETH', 'LTC', 'XRP', 'ADA', 'DOGE')
currencies = ('USD', 'EUR', 'GBP')

screen = st.sidebar.selectbox("Select Feature", ("Download Data", "Compare Returns", "View Technicals", "Generate Predicitons"), index=1)

st.title(screen)

if screen == "Compare Returns":

    crypto = st.multiselect('Choose assets', tickers, ('BTC-USD'))

    start = st.date_input('Start', value = pd.to_datetime('2021-01-01'))
    end = st.date_input('End', value = pd.to_datetime('today'))

    if len(crypto) > 0:
        test = yf.download(crypto, start, end)
        print(test)
        df = relative_return(yf.download(crypto, start, end)['Adj Close'])
        st.header(f'Returns of {crypto}')
        st.line_chart(df)

if screen == "Download Data":
    
    crypto_col, currency_col = st.beta_columns(2)

    crypto = crypto_col.selectbox('Choose assets', cryptos)
    currency = currency_col.selectbox('Choose currency', currencies)

    ticker = crypto + '-' + currency

    start = st.date_input('Start', value = pd.to_datetime('2021-01-01'))
    end = st.date_input('End', value = pd.to_datetime('today'))

    df_price = yf.download(ticker, start, end)

    st.dataframe(df_price)
    st.markdown(download_csv(df_price), unsafe_allow_html=True)

if screen == "View Technicals":
    # Turn indicators like RSI & BOLL on and off
    st.write("In progress 🔨")
    pass

if screen == "Generate Predicitons":
    # Generate simple predicitons using prophet
    st.write("In progress 🔨")
    pass


