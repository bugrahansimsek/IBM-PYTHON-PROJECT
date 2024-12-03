import requests
from bs4 import BeautifulSoup
import pandas as pd

# GameStop gelir verileri için URL
url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, 'html.parser')

# Gelir tablosunu bul
tables = soup.find_all("table")
for table in tables:
    if "Revenue" in table.text:
        revenue_table = table
        break

# Pandas DataFrame oluştur
gamestop_revenue = pd.read_html(str(revenue_table))[0]
gamestop_revenue.columns = ["Date", "Revenue"]
gamestop_revenue = gamestop_revenue[gamestop_revenue["Revenue"] != "-"]  # Eksik verileri filtrele
gamestop_revenue["Revenue"] = gamestop_revenue["Revenue"].str.replace(",", "").astype(float)

# Veriyi CSV olarak kaydet (opsiyonel)
gamestop_revenue.to_csv("gamestop_revenue.csv", index=False)

# İlk birkaç satırı görüntüle
print("GameStop Revenue Data:")
print(gamestop_revenue.head())
