from flask import render_template, request, redirect, url_for

from chatbot.base import app
from chatbot.base.com.dao.category_dao import TableDao
from chatbot.base.com.vo.category_vo import TableVo

print('in controller')
table_obj = TableVo()
dao_obj = TableDao()


@app.route('/', methods=['GET', 'POST'])
def sign_in():
    return render_template('signIn.html')

@app.route('/main', methods=['GET', 'POST'])
def transfer():
    name = request.form.get('NAME')
    if type(name) == str:
        return redirect(url_for('chat', name=name))

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    return render_template('index.html')

