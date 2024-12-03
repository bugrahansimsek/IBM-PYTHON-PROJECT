import yfinance as yf
import pandas as pd

# Tesla hisse verilerini çek
tesla_data = yf.Ticker("TSLA")
tesla_stock = tesla_data.history(period="max")

# Veriyi CSV olarak kaydet (opsiyonel)
tesla_stock.to_csv("tesla_stock.csv")

# İlk birkaç satırı görüntüle
print("Tesla Stock Data:")
print(tesla_stock.head())
