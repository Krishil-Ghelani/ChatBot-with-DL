from flask import render_template, request, redirect, url_for, session

from chatbot.base import app
from chatbot.base.com.dao.category_dao import TableDao
from chatbot.base.com.vo.category_vo import TableVo

import pymysql

print('in controller')
table_obj = TableVo()
dao_obj = TableDao()


@app.route('/', methods=['GET', 'POST'])
def sign_in():
    return render_template('signIn.html')

@app.route('/main', methods=['GET', 'POST'])
def transfer():
    print('in main')
    name = request.form.get('NAME')
    print(name)
    if type(name) == str:
        return redirect(url_for('chat', name=name))

@app.route('/chat', methods=['GET','POST'])
def chat():
    global message
    message = request.form.get("MESSAGE")
    print(message, 'fw')
    connection = pymysql.connect(host='localhost', user='root', password='root', db='pythondb', port=3306,
                                 cursorclass=pymysql.cursors.DictCursor)
    cursor_obj = connection.cursor()
    cursor_obj.execute(f'INSERT INTO prabhatbot (messages)\nVALUES ({message})')
    data = cursor_obj.fetchall
    print(data)
    cursor_obj.close()
    connection.close()

    return render_template('index.html')


#
# @app.route("/savingMessages", methods=['GET', 'POST'])
# def saveMessages():
#
#
#
