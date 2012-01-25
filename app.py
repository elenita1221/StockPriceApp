import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'What\'s up, Lance?'

@app.route('/stock')
def stock():
    return 'What is the stock price?'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
