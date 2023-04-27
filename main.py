import yfinance as yf
import datetime as dt
import requests
import os

def main():
    # 获取台湾大盘指数的数据
    twii = yf.Ticker("^TWII")

    # 获取当日数据
    data = twii.history(period="1d")

    # 获取当日收盘价，并将其转换为整数
    close_price = int(data["Close"][0])

    # 使用os.environ获取Github仓库的secrets
    tg_api_token = os.environ.get('TELEGRAM_API_TOKEN')
    tg_chat_id = os.environ.get('CHAT_ID')

    # 打印当日收盘价
    print("當日收盤價：", close_price)

    # 發電報函數
    def send_to_telegram(message):
        apiToken = tg_api_token
        chatID = tg_chat_id
        apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
        try:
            response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
            print(response.text)
        except Exception as e:
            print(e)

    # 發送消息至telegram
    current_time = dt.datetime.now().strftime("%Y-%m-%d")
    message = f"日期:{current_time} 當日收盤價:{close_price}"
    send_to_telegram(message)

main()
