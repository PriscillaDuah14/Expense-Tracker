from flask import Flask, jsonify, request

app = Flask(__name__)


# endpoint for home
@app.route('/')
def home():
    return 'Welcome to Flask'




# Have backend server run
if __name__ == '__main__':
    app.run(debug=True)