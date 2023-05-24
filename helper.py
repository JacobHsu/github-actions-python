import os
import requests
import datetime as dt
import tabulate

# 發電報函數
def send_to_telegram(codes_and_prices, url):
    # 發送消息至telegram
    table = tabulate.tabulate(codes_and_prices, tablefmt='simple')
    current_time = dt.datetime.now().strftime("%Y-%m-%d")
    message = f"日期:{current_time} [高股息買入]({url}):\n{table}"
    # 使用os.environ获取Github仓库的secrets
    apiToken = os.environ.get('TELEGRAM_API_TOKEN')
    chatID = os.environ.get('CHAT_ID')
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
    try:
        response = requests.post(apiURL, data={'chat_id': chatID, 'text': message, 'parse_mode': 'Markdown'})
        print(response.text)
    except Exception as e:
        print(e)
