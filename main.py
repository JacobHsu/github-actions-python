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

    print("當日收盤價：", close_price)

    # 取得USD/TWD匯率
    ticker = yf.Ticker('TWD=X')
    data = ticker.history(period='1d')
    exchange_rate = round(data['Close'][0], 2)

    print('美元對台幣匯率：', exchange_rate)

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
    message = f"日期:{current_time} '美元對台幣匯率:{exchange_rate}\n當日收盤價:{close_price}"
    send_to_telegram(message)

main()
