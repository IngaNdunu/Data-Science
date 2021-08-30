import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime
from datetime import date, timedelta
today = date.today()
import streamlit as st
import yfinance as yf

d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=360)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2





data = yf.download("ABG.JO", start=start_date, end= end_date,
                   group_by="ticker")
data1 = yf.download("NED.JO", start=start_date, end= end_date,
                   group_by="ticker")
data2 = yf.download("FSR.JO", start=start_date, end= end_date,
                   group_by="ticker")

fig, ax = plt.subplots() 
 
ax = data["Close"].plot(figsize=(12, 8), title=" Stock Prices of Some Companies in S.A", fontsize=20, label="Closing Price",color = "red"),data1["Close"].plot(figsize=(12, 8), title=" Stock Prices of Some Companies in S.A", fontsize=20, label="Closing Price"),data2["Close"].plot(figsize=(12, 8), title=" Stock Prices Of Some Companies in S.A", fontsize=20, label="Closing Price",color = "violet")

plt.legend()
plt.grid()
st.pyplot(fig)


