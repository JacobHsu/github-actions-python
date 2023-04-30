import requests
from bs4 import BeautifulSoup
import datetime as dt
import os
import tabulate

def main():
    url = 'https://tw.tradingview.com/markets/stocks-taiwan/market-movers-best-performing/'
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
            code = cells[0].text.strip()[1:]
            price = cells[2].text.strip()
            rating = cells[5].text.strip()
            # Check if the rating is "強力買入"
            if rating == "強力買入":
                codes_and_prices.append((code, price))

    # Print the list of codes and prices
    print(codes_and_prices)


    # 發電報函數
    def send_to_telegram(message):
        # 使用os.environ获取Github仓库的secrets
        apiToken = os.environ.get('TELEGRAM_API_TOKEN')
        chatID = os.environ.get('CHAT_ID')
        apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
        try:
            response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
            print(response.text)
        except Exception as e:
            print(e)

    # 發送消息至telegram
    table_link = 'https://tw.tradingview.com/markets/stocks-taiwan/market-movers-best-performing'
    # 轉換資料為表格
    table = tabulate.tabulate(codes_and_prices, tablefmt='simple')
    current_time = dt.datetime.now().strftime("%Y-%m-%d")
    message = f"日期:{current_time} [強力買入]({table_link}):\n{table}"
    send_to_telegram(message, parse_mode='Markdown')

main()
