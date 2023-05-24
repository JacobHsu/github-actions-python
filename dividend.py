import requests
from bs4 import BeautifulSoup

import re
import helper

def main():
    url = 'https://tw.tradingview.com/markets/stocks-taiwan/market-movers-high-dividend/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the table rows
    table_rows = soup.find_all('tr')

    # Create an empty list to store the codes and prices
    codes_and_prices = []

    filename = 'my_remove_list.txt'
    with open(filename, 'r') as file:
        my_remove_list = file.read()

    # Loop through each row and extract the data
    for row in table_rows:
        # Find the cells in the row
        cells = row.find_all('td')
        # Check if the row has cells
        if len(cells) > 0:
            # Extract the data from the cells
            code = cells[0].text.strip()[1:] 
            price = cells[2].text.strip()
            rating = cells[5].text.strip()
            # Check if the rating is "買入"
            if rating == "買入":
                stock = re.search(r'\d+', code).group()
                codes_and_prices.append((code, price)) if stock not in my_remove_list else None

    # Print the list of codes and prices
    print(codes_and_prices)
    helper.send_to_telegram(codes_and_prices)

main()
