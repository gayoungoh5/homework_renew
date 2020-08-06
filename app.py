from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbhomework

@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    option_receive = request.form['option_give']
    quantity_receive = request.form['quantity_give']
    address_receive = request.form['address_give']
    number_receive = request.form['number_give']

    order = {
        'name': name_receive,
        'option': option_receive,
        'quantity': quantity_receive,
        'address': address_receive,
        'number': number_receive
    }

    db.orders.insert_one(order)

    return jsonify({'result': 'success', 'msg': '서버에 연결되었습니다.'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():

    order_list = list(db.orders.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'orders': order_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)