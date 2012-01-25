import os
import urllib
from flask import Flask, render_template

app = Flask(__name__)

def __request(symbol, stat):
    url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (symbol, stat)
    return urllib.urlopen(url).read().strip().strip('"')

@app.route('/')
def hello():
    return 'What\'s up, Lance?'

@app.route('/stock/')
def default_stock():
    return 'Please enter a stock ticker symbol...'

@app.route('/stock/<symbol>')
def stock(symbol=None):
    # p = __request(symbol, 'l1c1va2xj1b4j4dyekjm3m4rr5p5p6s7').split(',')[0]
    p = __request(symbol, 'l1')
    # return '%s : %s' % (symbol, p)
    return render_template('stock.html', s=symbol, p=p)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
