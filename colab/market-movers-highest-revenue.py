import requests
from bs4 import BeautifulSoup

url = 'https://tw.tradingview.com/markets/stocks-usa/market-movers-highest-revenue/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the table rows
table_rows = soup.find_all('tr')

# Create an empty list to store the codes and prices
codes_and_prices = []



# Loop through each row and extract the data
for row in table_rows:
    # Find the cells in the row
    cells = row.find_all('td')
    # Check if the row has cells
    if len(cells) > 0:
        # Extract the data from the cells

        code = cells[0].text.strip()
   
        price = cells[2].text.strip()
        rating = cells[12].text.strip()
        print(rating)
        # Check if the rating is "強力買入"
        if rating == "強力買入":
            codes_and_prices.append((code, price))

def find_last_uppercase(word):
    first_word = re.search(r'\w+', word).group()
    uppercase_positions = [m.end() - 1 for m in re.finditer(r'[A-Z]', first_word)]
    idx = max(uppercase_positions)
    word = word[:idx] + '|' + word[idx:]
    return word

# Print the list of codes and prices
print(codes_and_prices)
