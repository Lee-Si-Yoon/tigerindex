import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify
from note import init

app = Flask(__name__)

@app.route('/')
def index():
    datas = init()[0]
    summed = init()[1]
    return render_template('index.html',
                            datas = datas,
                            summed = summed)

if __name__ == '__main__':
    app.run()
