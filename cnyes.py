import requests
from bs4 import BeautifulSoup
import datetime as dt
import os
import tabulate

def main():
    url = 'https://www.cnyes.com/twstock/a_technical7.aspx'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    table = soup.find('div', {'class': 'TableBox'})
    rows = table.find_all('tr')

    codes_and_prices = []

    filename = 'my_remove_list.txt'
    with open(filename, 'r') as file:
        my_remove_list = file.read()

    for row in rows:
        cols = row.find_all('td')
        if len(cols) > 0:
            code = cols[0].text.strip()
            name = cols[1].text.strip()
            closing_price = cols[2].text.strip()
            avg_price_5_days = cols[3].text.strip()
            if closing_price < avg_price_5_days:
                print(code, name)
                codes_and_prices.append((code, name, closing_price)) if code not in my_remove_list else None

        # Print the list of codes and prices
        print(codes_and_prices)


    # 發電報函數
    def send_to_telegram(message):
        # 使用os.environ获取Github仓库的secrets
        apiToken = os.environ.get('TELEGRAM_API_TOKEN')
        chatID = os.environ.get('CHAT_ID')
        apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
        try:
            response = requests.post(apiURL, data={'chat_id': chatID, 'text': message, 'parse_mode': 'Markdown'})
            print(response.text)
        except Exception as e:
            print(e)

    # 發送消息至telegram
    table = tabulate.tabulate(codes_and_prices, tablefmt='simple')
    current_time = dt.datetime.now().strftime("%Y-%m-%d")
    message = f"日期:{current_time} [均線黃金交叉]({url}):\n{table}"
    send_to_telegram(message)

main()
