import pandas as pd
import matplotlib.pyplot as plt

# Hisse ve gelir verilerini yükle
tesla_stock = pd.read_csv("tesla_stock.csv")
tesla_revenue = pd.read_csv("tesla_revenue.csv")

# Tarih formatını düzelt
tesla_revenue["Date"] = pd.to_datetime(tesla_revenue["Date"])
tesla_stock["Date"] = pd.to_datetime(tesla_stock["Date"])

# Grafik oluştur
plt.figure(figsize=(14, 7))
plt.plot(tesla_stock["Date"], tesla_stock["Close"], label="Tesla Stock Price")
plt.title("Tesla Stock Price vs Revenue")
plt.xlabel("Date")
plt.ylabel("Stock Price (USD)")
plt.legend()
plt.show()
