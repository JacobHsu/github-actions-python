import requests
import os


def send_to_telegram(message):
    # 使用os.environ获取Github仓库的secrets
    apiToken = os.environ.get('TELEGRAM_API_TOKEN')
    chatID = os.environ.get('CHAT_ID')
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
    try:
        response = requests.post(
            apiURL, data={'chat_id': chatID, 'text': message, 'parse_mode': 'Markdown'})
        print(response.text)
    except Exception as e:
        print(e)


# 發送消息至telegram
url = 'https://www.wantgoo.com/futures/wtxp&'
message = f"{url}:\n"
send_to_telegram(message)


jihsun = 'http://jsjustweb.jihsun.com.tw/z/ze/zeb/zeb.djhtm'
message = f"{jihsun}:\n"
send_to_telegram(message)