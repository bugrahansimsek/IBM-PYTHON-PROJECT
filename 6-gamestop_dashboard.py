import pandas as pd
import matplotlib.pyplot as plt

# Hisse ve gelir verilerini yükle
gamestop_stock = pd.read_csv("gamestop_stock.csv")
gamestop_revenue = pd.read_csv("gamestop_revenue.csv")

# Tarih formatını düzelt
gamestop_revenue["Date"] = pd.to_datetime(gamestop_revenue["Date"])
gamestop_stock["Date"] = pd.to_datetime(gamestop_stock["Date"])

# Grafik oluştur
plt.figure(figsize=(14, 7))
plt.plot(gamestop_stock["Date"], gamestop_stock["Close"], label="GameStop Stock Price")
plt.title("GameStop Stock Price vs Revenue")
plt.xlabel("Date")
plt.ylabel("Stock Price (USD)")
plt.legend()
plt.show()
