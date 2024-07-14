import time
from pytrends.request import TrendReq
from flask import Flask, render_template, jsonify
import json
# Khởi tạo pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# Đặt từ khóa bạn muốn tìm kiếm
kw_list = ["Python", "Java","C#","JavaScript"]

# Truy vấn dữ liệu với thời gian chờ giữa các yêu cầu
def get_trends_data(kw_list):
    pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m', geo='', gprop='')
    time.sleep(5)  # Thêm thời gian chờ 5 giây
    return pytrends.interest_over_time()

trends_data = get_trends_data(kw_list)
print(trends_data)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    with open('trends_data.json') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
