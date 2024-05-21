# 自行撰寫之程式碼
from flask import Flask, request, render_template,send_file,jsonify
import os
import csv
import secrets
from datetime import datetime
from PIL import Image
# import numpy as np
import time
from sql_func import insert_data, get_data
import json
import multiprocessing
headdir = './'
app = Flask(__name__)
# target_folder=headdir


@app.route('/', methods=['GET'])
def test():
    return 'get OK', 200
@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('index.html'), 200
@app.route('/upload_data', methods=['GET'])
def upload_data():
    # 從查詢字串中獲取參數
    table_name = request.args.get('group_name')
    name = request.args.get('key')
    age = request.args.get('value')
    print(datetime.now())
    # 檢查必要的參數是否存在
    if not all([table_name, name, age]):
        return jsonify({'error': '缺少必要的參數'}), 400
    
    # 呼叫insert_data函數插入資料
    try:
        age = float(age)  # 確保age是浮點數
        message = insert_data(table_name, name, age)
        return jsonify({'message': message}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/get_data', methods=['POST'])
def get_data_backend():
    user = request.json['user']
    data = {'time': [], 'value': []}
    data = get_data(user)
    return jsonify(data)
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug = True)
