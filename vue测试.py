from flask import Flask,request
from flask import jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app, supports_credentials=True)//应对跨域请求
@app.route('/')
def helloworld():
    # if(request.args.get('callback')==None):
    call=request.args.get('callback')
    return call+'()'
@app.route('/getMsg', methods=['GET', 'POST'])
def home():
    list = [
      {'id': '1', 'name': '宝马', 'ctime': 'Sun Apr 07 2019 14:07:35 GMT+0800 (中国标准时间)'},
      {'id': '2', 'name': '玛莎拉蒂', 'ctime': 'Sun Apr 07 2019 14:07:35 GMT+0800 (中国标准时间)'},
      {'id': '3', 'name': '奔驰', 'ctime': 'Sun Apr 07 2019 14:07:35 GMT+0800 (中国标准时间)'}
    ]
    app.config['JSON_AS_ASCII'] = False
    return jsonify(list)
# 启动运行
if __name__ == '__main__':
    app.run(debug=True)   # 这样子会直接运行在本地服务器，也即是 localhost:5000
   # app.run(host='your_ip_address') # 这里可通过 host 指定在公网IP上运行
