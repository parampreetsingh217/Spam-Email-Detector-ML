from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "hello world update 217 " 


if __name__ == '__main__':
    app.run(debug=True)