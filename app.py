import streamlit as st
import yfinance as yf
import pandas as pd

from helpers import relative_return

tickers = ('BTC-USD', 'ETH-USD', 'LTC-USD', 'DOGE-USD', 'XRP-USD', 'ADA-USD')
cryptos = ('BTC', 'ETH', 'LTC', 'XRP', 'ADA', 'DOGE')
currencies = ('USD', 'EUR', 'GBP')

screen = st.sidebar.selectbox("Select Feature", ("Download Data", "Compare Returns", "Technicals"), index=1)

st.title(screen)

if screen == "Compare Returns":
    
    # crypto_col, currency_col = st.beta_columns(2)

    # crypto = crypto_col.multiselect('Choose assets', cryptos, ('BTC'))
    # currency = currency_col.selectbox('Choose currency', currencies)

    # for i in range(len(crypto)):
    #     crypto[i] = crypto[i] + '-' + currency

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
    pass