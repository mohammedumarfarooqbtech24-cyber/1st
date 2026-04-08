from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    return f"Hello from Python-Flask-Docker app! Timestamp: {timestamp}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')