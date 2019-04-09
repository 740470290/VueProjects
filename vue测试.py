from flask import Flask, request, render_template,json
from flask import jsonify
from flask_cors import CORS
import sqlite3 as sql
import time

app = Flask(__name__)
# 处理跨域请求
cors = CORS(app, resources={r"/getMsg": {"origins": "*"}})
# CORS(app, supports_credentials=True)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/getMsg', methods=['GET', 'POST'])
def home():
    list = []
    con = sql.connect("mydb")
    cur = con.cursor()
    if request.method == 'POST':
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        user = request.form.get('name')
        # date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        cur.execute("INSERT INTO students (name,ctime) VALUES(?, ?)", (user, date))
        con.commit()
    cur.execute("select * from students")
    ulist = cur.fetchall()
    # ulist得到的是数组,需要转json字典
    for i in ulist:
      car = {'id': i[0], 'name': i[1], 'ctime': i[2]}
      list.append(car)
    # 防止中文json乱码
    app.config['JSON_AS_ASCII'] = False
    return jsonify(list)


# 启动运行
if __name__ == '__main__':
    app.run(debug=True)   # 这样子会直接运行在本地服务器，也即是 localhost:5000
   # app.run(host='your_ip_address') # 这里可通过 host 指定在公网IP上运行
