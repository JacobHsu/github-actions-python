import yfinance as yf
import datetime as dt
import requests

# 获取台湾大盘指数的数据
twii = yf.Ticker("^TWII")

# 获取当日数据
data = twii.history(period="1d")

# 获取当日收盘价，并将其转换为整数
close_price = int(data["Close"][0])

# 打印当日收盘价
print("当日收盘价：", close_price)

# 發電報函數
def send_to_telegram(message):
    apiToken = '5913409909:AAGvbMsLo-rqqCjM0X9uS56jVrVhMiCmcZw'
    chatID = '453495889'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

# 發送消息至telegram
current_time = dt.datetime.now().strftime("%Y-%m-%d")
message = f"現在時間:{current_time}當日收盤價:{close_price}"
send_to_telegram(message)
