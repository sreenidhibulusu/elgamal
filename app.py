import os

from flask import Flask, render_template
from flask import request
from elgamal import *

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/operation_result", methods=['POST'])
def operation_result():
    val = request.form['the-message']
    msg = main(val)
    key1 = msg[1]
    key2 = msg[2]
    key3 = msg[3]
    key4 = msg[4]
    key5 = msg[5]
    key6 = msg[6]
    return render_template('index.html', calculation_success=True, result=msg, result_1=key1, result_2=key2, result_3=key3, result_4=key4, result_5=key5, result_6=key6)


if __name__ == '__main__':
    app.run()
