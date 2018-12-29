from flask import Flask
from flatfile import flat
from flask import jsonify
app = Flask(__name__)

@app.route('/query/<str:name>')
def hello():
    return jsonify('Hello World!')

if __name__ == '__main__':
    app.run()
'''
get api key
swala.herokuapp.com/api/key/val
send api key
mysql -u root -p

