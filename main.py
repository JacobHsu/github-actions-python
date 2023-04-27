import yfinance as yf

# 获取台湾大盘指数的数据
twii = yf.Ticker("^TWII")

# 获取当日数据
data = twii.history(period="1d")

# 获取当日收盘价，并将其转换为整数
close_price = int(data["Close"][0])

# 打印当日收盘价
print("当日收盘价：", close_price)
