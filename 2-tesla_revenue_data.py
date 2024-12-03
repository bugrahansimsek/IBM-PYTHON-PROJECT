import requests
from bs4 import BeautifulSoup
import pandas as pd

# Tesla gelir verileri için URL
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, 'html.parser')

# Gelir tablosunu bul
tables = soup.find_all("table")
for table in tables:
    if "Revenue" in table.text:
        revenue_table = table
        break

# Pandas DataFrame oluştur
tesla_revenue = pd.read_html(str(revenue_table))[0]
tesla_revenue.columns = ["Date", "Revenue"]
tesla_revenue = tesla_revenue[tesla_revenue["Revenue"] != "-"]  # Eksik verileri filtrele
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(",", "").astype(float)

# Veriyi CSV olarak kaydet (opsiyonel)
tesla_revenue.to_csv("tesla_revenue.csv", index=False)

# İlk birkaç satırı görüntüle
print("Tesla Revenue Data:")
print(tesla_revenue.head())
