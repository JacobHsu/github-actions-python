import twstock
import requests
import os

def main():

    def best_four_point_to_buy(stockid):
        stock = twstock.Stock(stockid)
        bp = twstock.BestFourPoint(stock).best_four_point()
        if bp[0]:
            print('買進訊號', stockid)
            print(bp)
            # 發送消息至telegram
            message = f"買進訊號:{stockid}\n{bp}"
            send_to_telegram(message)
        else:
            print('無買進訊號', stockid)


    # 發電報函數
    def send_to_telegram(message):
        apiToken = os.environ.get('TELEGRAM_API_TOKEN')
        chatID = os.environ.get('CHAT_ID')
        apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
        try:
            response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
            print(response.text)
        except Exception as e:
            print(e)

    # 發送消息至telegram
    # 上市股票
    for stockid in ['0050','1440','2002','2614']: 
        best_four_point_to_buy(stockid)

main()
