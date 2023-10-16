import requests
from bs4 import BeautifulSoup

url = 'https://tw.tradingview.com/markets/stocks-taiwan/market-movers-high-dividend/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the table rows
table_rows = soup.find_all('tr')
codes_and_prices = []
# Loop through each row and extract the data
for row in table_rows:
    # Find the cells in the row
    cells = row.find_all('td')
    # Check if the row has cells
    if len(cells) > 0:
        # Extract the data from the cells

        if cells[0].text[:5].isdigit():
            code = cells[0].text.strip()[1:]
        else:
            code = cells[0].text.strip() 
            
        price = cells[2].text.strip()
        rating = cells[12].text.strip()

        # Check if the rating is "買入"
        if rating == "強力買入" or rating == "買入":
            codes_and_prices.append((code, price))

# Print the list of codes and prices
print(codes_and_prices)